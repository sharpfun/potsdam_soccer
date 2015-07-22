#!/usr/bin/env python

# Master Script For Testing #

import optparse

import sys
sys.path.insert(0, 'ticker_to_kicker')
from verbnet import *
from ticker import *
from sem_parse import *
from kicktionary import *
from frame_extract import *
from arguments import *

sys.path.insert(0, 'kicker_to_asp')
from asp_conversion import to_asp

def main():
	parser = optparse.OptionParser()
	parser.add_option("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="data/kicktionary.xml")
	parser.add_option("--ticker", dest="ticker", help="location of parsed ticker conll file", default="data/p4.parsed")
	parser.add_option("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
	parser.add_option("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder
	parser.add_option("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="data/verbnet")
	parser.add_option("--luorder", dest="luorder", help="location of folder with lexical unit order file", default="data/lu_order")
	(options, args) = parser.parse_args()

	verbose = options.verbose
	language = options.language

	kicktionary = read_kicktionary(options.kicktionary, verbose, language)
	#verbnet = read_verbnet(options.verbnet)
	ticker = read_ticker(options.ticker, verbose, language)
	#ticker_with_lus = kicktionary_lookup_possible_lu(kicktionary, ticker, verbose)
	#luorder = [line.rstrip('\n') for line in open(options.luorder).readlines()]
	events = find_arguments(ticker, verbose)
	asp = to_asp(events)

    #for event in events:
		#if event.frame != None and event.frame != "":
			#print event.ticker
			#print event.minute
			#print event.text
			#print event.arguments
			#print ""

if __name__ == "__main__":
    main()

