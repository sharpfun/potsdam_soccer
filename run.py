#!/usr/bin/env python

## run.py
##d

import sys
import argparse

import extracting.kicktionary
import extracting.verbnet
import extracting.ticker
import extracting.frame_extract
import extracting.arguments
import reasoning.asp_conversion
import reasoning.solver

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
    parser.add_argument("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="data/kicktionary.xml")
    parser.add_argument("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="data/verbnet")
    parser.add_argument("--tickers", dest="tickers", help="location of parsed ticker conll file", default=['data/parsed/p5.parsed'], nargs="*")
    parser.add_argument("--language", dest="language", help="language of tickers (en or de)", default="en")
    parser.add_argument("--luorder", dest="luorder", help="location of folder with lexical unit order file", default="data/lu_order")
    args = parser.parse_args()

    verbose = args.verbose
    language = args.language

    # Retreieve lu_order information.
    luorder = [line.rstrip('\n') for line in open(args.luorder).readlines()]

    # Print list of tickers being read in.
    print "Using the following tickers: ", args.tickers

    events = []
    for ticker in args.tickers:
        # Get list of LexicalUnit objects.
        kicktionary = extracting.kicktionary.read_kicktionary(args.kicktionary, verbose, language)

        # Get list of Verbnet objects.
        verbnet = extracting.verbnet.read_verbnet(args.verbnet, verbose, language)

        # Reads in a parsed ticker feed in dependency tree conll format and returns a list of ticker Tree objects.
        # NOTE: The ticker scraping and parsing is part of pre-processing and is not done within this program.
        ticker = extracting.ticker.read_ticker(ticker, verbose, language)

		# TODO: incorporate Verbnet into frame_extract.py
        # TODO: INJECT INFORMATION WHERE THERE ARE EMPTY SETS.
        # Reads in a ticker Tree object and returns a list of sets of possible LexicalUnits, 
        # each set corresponding to one sentence in the ticker.
        ticker_with_lus = extracting.frame_extract.kicktionary_lookup_possible_lu(kicktionary, verbnet, ticker, verbose)
                
        # Iterate over all sets of possible LexicalUnits in the list of ticker 
		# sentences and return a selection of event objects for each sentence, 
		# ready for translation to asp.
        events.extend(extracting.arguments.find_arguments(ticker, ticker_with_lus, kicktionary, verbose))

    #print reasoning.asp_conversion.to_asp(events)

    # converts each event object into asp format
    # then resolves event issues, processes.
    asp = reasoning.solver.solve(events)
    
    # What we want to do with the result?
    print "\n".join(map(str,asp))

if __name__ == "__main__":
    main()

