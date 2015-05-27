#!/usr/bin/env python

"""
Simple script to:
1. read in trees from parsed tickers
2. read in Kicktionary lexicon
3. (for now) just do a lookup of the tree ROOT in the Kicktionary
"""

from __future__ import division
from bs4 import BeautifulSoup
import nltk, copy, collections, xml.sax

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
    

