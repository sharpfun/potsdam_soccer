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
import os
from os.path import isfile, join
from time import gmtime, strftime
import shutil
from subprocess import call


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
    parser.add_argument("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="data/kicktionary.xml")
    parser.add_argument("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="data/verbnet")
    parser.add_argument("--tickers", dest="tickers", help="location of tickers folder", default='data/input', nargs="*")
    # parser.add_argument("--language", dest="language", help="language of tickers (en or de)", default="en")
    parser.add_argument("--luorder", dest="luorder", help="location of folder with lexical unit order file", default="data/lu_order")
    args = parser.parse_args()

    verbose = args.verbose

    # we support only english for now
    language = "en"  # args.language

    datetime_str = strftime("%Y-%m-%d %H-%M", gmtime())

    # list files
    ticker_files_list = [f for f in os.listdir(args.tickers) if isfile(join(args.tickers, f))]

    # create all required folders
    input_folder_path = join("data", "output", datetime_str, "in")
    output_folder_path = join("data", "output", datetime_str, "out")
    parsed_folder_path = join("data", "output", datetime_str, "parsed")
    os.makedirs(input_folder_path)
    os.makedirs(output_folder_path)
    os.makedirs(parsed_folder_path)

    # copy files to input folder (to have copy of source)
    for ticker_filename in ticker_files_list:
        shutil.copy2(join(args.tickers, ticker_filename), join(input_folder_path, ticker_filename))

    # move all tickers to parser/tmp/
    parser_tmp_folder = join("parser", "tmp")

    try:
        shutil.rmtree(parser_tmp_folder)
    except:
        pass

    os.makedirs(parser_tmp_folder)

    for ticker_filename in ticker_files_list:
        shutil.copy2(join(args.tickers, ticker_filename), join(parser_tmp_folder, ticker_filename))
        call(["./parse.sh", join("tmp", ticker_filename)], cwd=join(os.getcwd(), "parser"))

    for ticker_filename in ticker_files_list:
        try:
            parsed_filename = ticker_filename+".parsed"
            shutil.copy2(join(parser_tmp_folder, parsed_filename), join(parsed_folder_path, parsed_filename))
        except:
            print "Ticker "+ticker_filename+" wasn't parsed"
            pass

    #try:
    #    shutil.rmtree(parser_tmp_folder)
    #except:
    #    pass

    # Print list of tickers being read in.
    # print "Using the following tickers: ", args.tickers

    # Get list of LexicalUnit objects.
    kicktionary = extracting.kicktionary.read_kicktionary(args.kicktionary, verbose, language)

    # Get list of Verbnet objects.
    verbnet = extracting.verbnet.read_verbnet(args.verbnet, verbose, language)

    events = []
    for ticker_filename in ticker_files_list:
        ticker_file_path = join(parsed_folder_path, ticker_filename + ".parsed")
        # Reads in a parsed ticker feed in dependency tree conll format and returns a list of ticker Tree objects.
        # NOTE: The ticker scraping and parsing is part of pre-processing and is not done within this program.
        ticker = extracting.ticker.read_ticker(ticker_file_path, verbose, language)

        # TODO: incorporate Verbnet into frame_extract.py
        # TODO: INJECT INFORMATION WHERE THERE ARE EMPTY SETS.
        # Reads in a ticker Tree object and returns a list of sets of possible LexicalUnits, 
        # each set corresponding to one sentence in the ticker.
        ticker_with_lus = extracting.frame_extract.kicktionary_lookup_possible_lu(kicktionary, verbnet, ticker, verbose)

        # order lexical units, for now only en
        extracting.frame_extract.order_lu(ticker_with_lus, args.luorder)

        # Iterate over all sets of possible LexicalUnits in the list of ticker 
        # sentences and return a selection of event objects for each sentence,
        # ready for translation to asp.
        events.extend(extracting.arguments.find_arguments(ticker, ticker_with_lus, kicktionary, verbose))

    # print reasoning.asp_conversion.to_asp(events)

    # converts each event object into asp format
    # then resolves event issues, processes.
    asp = reasoning.solver.solve(events)
    
    # What we want to do with the result?
    print "\n".join(map(str,asp))

if __name__ == "__main__":
    main()

