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

def kicktionary_lookup_possible_lu(kicktionary, ticker, verbose, luorder):
    luorder.reverse()
    print luorder
    if verbose: print "Looking up tree roots in Kicktionary..."
    
    for tree in ticker:
        #print sentence
        s = ""
        for node in tree.nodes:
            s = s + node.word + " "
        print s

        found_lus = []
        for node in tree.nodes:
            for lu in kicktionary:
                if node.lemma == lu.lemma:
                    if ((lu.wordclass == 'v' and node.pos.startswith("VB")) or
                        (lu.wordclass == 'n' and (node.pos == 'NN' or node.pos == 'NNS'))):
                        found_lus.append(lu.lemma+"."+lu.wordclass);
                        print str(tree.tree_id) + " matches: " + lu.lemma + " " + lu.wordclass
                    #tree.lexical_unit = lu
        
        found_lus = sorted(found_lus, key=lambda x: not(x in luorder) and 1 or -luorder.index(x))
        
        print "ordered set of lexical units:"
        print found_lus
        print ""
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
    parser.add_option("--luorder", dest="luorder", help="location of folder with lexical unit order file", default="../data/luorder")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language
        
    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    ticker = read_ticker(options.ticker, verbose, language)
    # verbnet = read_verbnet(options.verbnet)

    luorder = [line.rstrip('\n') for line in open(options.luorder).readlines()]
    ticker_with_lus = kicktionary_lookup_possible_lu(kicktionary, ticker, verbose, luorder)

if __name__ == "__main__":
    main()

