#!/usr/bin/env python

# Main script, identifies Kicktionary and Verbnet frames for ticker sentences.
# 1. Look up roots in Kicktionary.
# 2. Look up root-object pairs in Kicktionary.
# 3. Look up roots in Verbnet.
# 4. Look up Verbnet frame-members in Kicktionary, recursively.
# 5. Last Resort: If no frame-member match is found, use (3) as match.

from __future__ import division
import collections
import copy
import optparse
import xml.sax

from bs4 import BeautifulSoup
import nltk

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
    # TODO: find when the tree root matches more than one Kicktionary lexical unit and somehow disambiguate.
    
    return ticker

# Added Root-->Verbnet.Frame.Member-->Kicktionary LU Lookup, and Root-->Verbnet lookup.
#def verbnet_lookup(verbnet, ticker, verbose):
#    if verbose: print "Looking up tree roots in Verbnet..."
#
#    for tree in ticker:
#        for vb in verbnet:
#            member_match = _frame_member_lookup(vb, kicktionary)
#            if member_match != None:
#                tree.lexical_unit = member_match
#                if verbose: print "Tree " + str(tree.tree_id) + " root (via verbnet frame-member relation) matches Kicktionary lexical unit: " + tree.lexical_unit.lemma
#            elif tree.root == vb.lemma:
#                tree.lexical_unit = vb
#                if verbose: print "Tree " + str(tree.tree_id) + " root matches Verbnet lexical unit: " + tree.lexical_unit.lemma

#    return ticker

#def _frame_member_lookup(vb, kicktionary):
#    if verbose: print "Looking up Verbnet frame-members in Kicktionary..."
#    for fm in 

def main():
    parser = optparse.OptionParser()
    parser.add_option("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="../data/kicktionary.xml")
    parser.add_option("--ticker", dest="ticker", help="location of parsed ticker conll file", default="../data/p2.parsed")
    parser.add_option("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
    parser.add_option("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder.
    parser.add_option("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="../data/verbnet")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language
        
    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    ticker = read_ticker(options.ticker, verbose, language)
    verbnet = read_verbnet(options.verbnet, verbose, language)

    ticker_with_lus = kicktionary_lookup(kicktionary, ticker, verbose)
    # TODO: Add ticker_with_verbs.

if __name__ == "__main__":
    main()
