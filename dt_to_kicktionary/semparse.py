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
        possibleLUs = [lu for lu in kicktionary if lu.lemma == tree.root]
        # classification in 3 steps:
        # 1. we find at least one LU for the root
        if len(possibleLUs) >= 1:
            if len(possibleLUs) == 1:
                tree.lexical_unit = possibleLUs[0]
                if verbose: print "Tree " + str(tree.tree_id) + " root matches Kicktionary lexical unit: " + tree.lexical_unit.lemma
<<<<<<< HEAD
    # TODO: find when the tree root matches more than one Kicktionary lexical unit and somehow disambiguate.
=======
            else:
                # how to determine??
                if verbose: print "Tree " + str(tree.tree_id) + " root with possible LUs: ", possibleLUs
        # 2. find LU for arguments of the root
        else:
            # find the arguments of the root
            root_id = [int(node.node_id) for node in tree.nodes if int(node.head) == 0][0]
            arguments = [node for node in tree.nodes if int(node.head) == root_id and node.type == "OBJ"]
            # look for OBJ in kicktionary instead
            possibleLUs = [lu for lu in kicktionary if lu.lemma == arguments[0].lemma] if arguments else []
            if len(possibleLUs) >= 1:
                if len(possibleLUs) == 1:
                    tree.lexical_unit = possibleLUs[0]
                    if verbose: print "Tree " + str(tree.tree_id) + " root matches Kicktionary lexical unit: " + tree.lexical_unit.lemma
                else:
                    # how to determine??
                    if verbose: print "Tree " + str(tree.tree_id) + " root with possible LUs: ", possibleLUs
        # 3. case, when there is no match with at least the root
            else:
                # here comes clays verbnet part
                pass #<- placeholder
>>>>>>> 9f0e3b068d611bb105821fee0cde2c3364fe4364
    
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
    parser.add_option("--verbose", dest="verbose", help="print helpful messages about the progress", default=True)
    parser.add_option("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder.
    parser.add_option("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="../data/verbnet")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language
        
    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    #print kicktionary
    ticker = read_ticker(options.ticker, verbose, language)
<<<<<<< HEAD
    verbnet = read_verbnet(options.verbnet, verbose, language)

    ticker_with_lus = kicktionary_lookup(kicktionary, ticker, verbose)
    # TODO: Add ticker_with_verbs.
=======
    #raw_input()
    #print ticker
    #raw_input()
    # verbnet = read_verbnet(options.verbnet)

    ticker_with_lus = kicktionary_lookup(kicktionary, ticker, verbose)
    #print ticker_with_lus
>>>>>>> 9f0e3b068d611bb105821fee0cde2c3364fe4364

if __name__ == "__main__":
    main()
