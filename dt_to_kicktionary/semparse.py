#!/usr/bin/env python

<<<<<<< HEAD
"""
Simple script to:
1. read in trees from parsed tickers
2. read in Kicktionary lexicon
3. (for now) just do a lookup of the tree ROOT in the Kicktionary
"""
=======
# Main script for identifying Kicktionary (and Verbnet) frames for ticker sentences
# 1. First look up only roots in Kicktionary directly
# 2. Then look up roots and objects
# 3. Then look up roots in Verbnet
# 4. With Verbnet frames, look up in Kicktionary again
>>>>>>> b14ea6e82cb7622676e3714a2a5e0d8fe3fa607b

from __future__ import division
from bs4 import BeautifulSoup
import nltk, copy, collections, xml.sax
<<<<<<< HEAD

"""
DEFINE CLASSES
"""
class Node(object):
    def __init__(self):
        self.node_id = 0
        self.word = None
        self.lemma = None
        self.pos = None
        self.head = None
        self.type = None

class Tree(object):
    def __init__(self):
        self.tree_id = 0
        self.nodes = []
        self.root = None
        self.object = None
        self.subject = None

class LexicalUnit(object):
    def __init__(self):
        self.scenario = None
        self.frame = None
        self.lang = None
        self.lu_id = None
        self.wordclass = None
        self.super_scenario = None
        self.synset = None
        self.frynset = None
        self.arguments = []       
        
class Argument(object):
    def __init__(self):
        self.name = None
        self.type = None

"""
READ IN KICTIONARY
"""
kicktionary = []

soup = BeautifulSoup(open("All_LUs-GrpG.xml"), "xml")
lus = soup("LEXICAL-UNIT")

for item in lus:
    lu = LexicalUnit()
    
    lu.lemma = item.string
    lu.scenario = item["scenario"]
    lu.frame = item["frame"]
    lu.lang = item["lang"]
    lu.lu_id = item["lu-id"]
    lu.wordclass = item["wordclass"]
    lu.super_scenario = item["super-scenario"]
    lu.synset = item["synset"]
    #lu.frynset = item["frynset"]
    lu.arguments = []    

    kicktionary.append(lu)
    
print kicktionary[0].lemma

print len(kicktionary)

"""
OPEN AND SPLIT PARSED FILE
"""
fhand = open("p2.parsed")
raw = fhand.read()

rawsentences = raw.split("\n\n")

"""
READER
"""
trees = []

ids = 0

for rawsentence in rawsentences:
    
    tree = Tree()
    ids += ids
    tree.tree_id = ids
    
    lines = rawsentence.split('\n')
    
    # English parses don't have "form"
    # Types are different between English and German
    # i.e. ROOT vs. --
    for line in lines:
        
        cells = line.split("\t")

        if len(cells) > 1:
            node = Node()
            
            node.node_id = cells[0]
            node.word = cells[1]
            node.lemma = cells[3]
            node.pos = cells[5]
            node.form = cells[7]
            node.head = cells[9]
            node.type = cells[11]
          
        tree.nodes.append(node)
          
    trees.append(tree)

# save initial graphs in safe list for reference
initial_trees = copy.deepcopy(trees)


""" 
READER TESTING

for i in range(len(trees[0].nodes)):
    print trees[0].nodes[i].type

# Print the heads
for tree in trees:
    for i in range(len(tree.nodes)):
        if tree.nodes[i].head == "0":
            print tree.nodes[i].word
"""  

# Simple test - for how many sentences is the head directly in the kicktionary?

heads = []

for tree in trees:
    for i in range(len(tree.nodes)):
        if tree.nodes[i].head == "0":
            heads.append(tree.nodes[i].lemma)

print heads
            
entries = []

for entry in kicktionary:
    if entry.lang == "en":
        entries.append(entry.lemma)
    
print entries

match = []

for head in heads:
    for entry in entries:
        if unicode(head, errors="ignore") == entry:
            match.append(head)
            
print match
    
=======
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
    parser.add_option("--verbnet", dest="verbnet", help="location of verbnet xml files", default="../data/verbnet")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language
        
    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    ticker = read_ticker(options.ticker, verbose, language)
    # verbnet = read_verbnet(options.verbnet)

    ticker_with_lus = kicktionary_lookup(kicktionary, ticker, verbose)

if __name__ == "__main__":
    main()
>>>>>>> b14ea6e82cb7622676e3714a2a5e0d8fe3fa607b

