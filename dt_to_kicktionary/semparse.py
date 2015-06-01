#!/usr/bin/env python

# Master script. Identifies Kicktionary and Verbnet matches of ticker sentences.
# 1. Look up roots in Kicktionary.
# 2. Look up root-object pairs in Kicktionary.
# 3. Look up roots in Verbnet via Verbnet frame in Kicktionary.
#       This means: Can we match the tree root to a Verbnet verb, get it's 
#       Verbnet frame, and then match *this* frame to Kicktionary? In this way, 
#       we have an *indirect* root-->kictionary relation VIA the frame.
# 4. Look up roots via frame siblings in Kicktionary.
#       This means: Can we mateh the tree root to a Verbnet verb, iterate over
#       it's siblings, and then match *this* sibling to Kicktionary? In this
#       way, we have an *indirect* root-->kictionary relation VIA the sibling.

from __future__ import division
import optparse

from bs4 import BeautifulSoup
import nltk

from ticker import *
from kicktionary import *
from verbnet import *

def lookup(kicktionary, verbnet, ticker, verbose):
    if verbose: print "Looking up tree roots in Kicktionary..."
    if verbose: print "Looking up root-object pairs in Kicktionary..."
    if verbose: print "Looking up tree roots in Verbnet..."
    if verbose: print "Looking up tree roots (via Verbnet) in Kicktionary..."

    for tree in ticker:
        possibleLUs = [lu for lu in kicktionary if lu.lemma == tree.root]
        # 4-Step Classification:
        # 1. Look up root in Kicktionary.
        if len(possibleLUs) >= 1:
            if len(possibleLUs) == 1:
                tree.lexical_unit = possibleLUs[0]
                if verbose: print "Tree " + str(tree.tree_id) + " root matches Kicktionary lexical unit: " + tree.lexical_unit.lemma
            else:
                # how to determine??
                if verbose: print "Tree " + str(tree.tree_id) + " root with possible LUs: ", possibleLUs
        # 2. Look up root-object pairs in Kicktionary.
        else:
            # Find the arguments of the root.
            root_id = [int(node.node_id) for node in tree.nodes if int(node.head) == 0][0]
            arguments = [node for node in tree.nodes if int(node.head) == root_id and node.type == "OBJ"]
            # Look for OBJ in Kicktionary.
            possibleLUs = [lu for lu in kicktionary if lu.lemma == arguments[0].lemma] if arguments else []
            if len(possibleLUs) >= 1:
                if len(possibleLUs) == 1:
                    tree.lexical_unit = possibleLUs[0]
                    if verbose: print "Tree " + str(tree.tree_id) + " root matches Kicktionary lexical unit: " + tree.lexical_unit.lemma
                else:
                    # how to determine??
                    if verbose: print "Tree " + str(tree.tree_id) + " root with possible LUs: ", possibleLUs
        # 3. Look up roots in Verbnet via Verbnet frame in Kicktionary.
        # a. Root-->Verbnet.Verb-->Verbnet.Frame-->Kicktionary.
        # b. Root--> Verbnet.Verb-->Verbnet.Sibling-->Kicktionary.
            else:
                for vb in verbnet:
                    if vb.lemma == tree.root:
                        possibleLUs = [lu for lu in kicktionary if lu.lemma == vb.frame]
                        if len(possibleLUs) >= 1:
                            if len(possibleLUs) == 1: 
                                tree.lexical_unit = possibleLUs[0]
                                if verbose: print "Tree " + str(tree.tree_id) + " root matches (via Verbnet frame) Kicktionary unit: " + tree.lexical_unit.lemma
                            else: 
                                pass # <-- how to determine??
 #                       else: 
 #                           tree.lexical_unit == vb
 #                           if verbose: print "Tree " + str(tree.tree_id) + " root matches Verbnet lexical unit: " + tree.lexical_unit.lemma
    
    return ticker

def main():
    parser = optparse.OptionParser()
    parser.add_option("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="../data/kicktionary.xml")
    parser.add_option("--ticker", dest="ticker", help="location of parsed ticker conll file", default="../data/p2.parsed")
    parser.add_option("--verbose", dest="verbose", help="print helpful messages about the progress", default=True)
    parser.add_option("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder
    parser.add_option("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="../data/verbnet")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language
    
    #raw_input()
    ticker = read_ticker(options.ticker, verbose, language)
    #raw_input()
    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    #raw_input()
    verbnet = read_verbnet(options.verbnet, verbose, language)

    matches = lookup(kicktionary, verbnet, ticker, verbose)
    #print matches

if __name__ == "__main__":
    main()
