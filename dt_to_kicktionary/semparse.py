#!/usr/bin/env python

# Main script for identifying Kicktionary (and Verbnet) frames for ticker sentences
# 1. First look up only roots in Kicktionary directly
# 2. Then look up roots and objects
# 3. Then look up roots in Verbnet
# 4. With Verbnet frames, look up in Kicktionary again

from __future__ import division
from bs4 import BeautifulSoup
import nltk, copy, collections, xml.sax
from kicktionary import *
from ticker import *
from verbnet import *

def kicktionary_lookup(kicktionary, ticker, verbose):
    if verbose: print "Looking up tree roots in Kicktionary..."
    
    for tree in ticker:
        for lu in kicktionary:
            if tree.root == lu.lemma:
                tree.lexical_unit = lu
                if verbose: print "Tree " + str(tree.tree_id) + " root matches Kicktionary lexical unit: " + tree.lexical_unit.lemma
    ## TODO: find when the tree root matches more than one Kicktionary lexical unit
    ## and somehow disambiguate
    
    return ticker
               
def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="../data/kicktionary.xml")
    parser.add_option("--ticker", dest="ticker", help="location of parsed ticker conll file", default="../data/p2.parsed")
    parser.add_option("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
    parser.add_option("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder
    parser.add_option("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="../data/verbnet")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language
        
    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    ticker = read_ticker(options.ticker, verbose, language)
    # verbnet = read_verbnet(options.verbnet)

    ticker_with_lus = kicktionary_lookup(kicktionary, ticker, verbose)

if __name__ == "__main__":
    main()

