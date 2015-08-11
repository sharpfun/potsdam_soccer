#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reads in a parsed ticker feed in dependency tree conll format
# And returns a list of Tree objects

# TODO: clean up tokenization for input files (punctuation, contractions like "couldn't"...)
# as they are leading to incorrect readings of part of speech

# TODO: the minute marks should somehow be added to each tree so that it can be used later in the ASP representation

import re

class Node(object):

    def __init__(self):
        self.node_id = 0
        self.word = None
        self.lemma = None
        self.pos = None
        self.head = None
        self.type = None
    
    def __str__(self):
        return "({},{},{})".format(self.head, self.lemma, self.type)
    __repr__ = __str__


class Tree(object):

    def __init__(self):
        self.ticker = None
        self.minute = None
        self.tree_id = 0
        self.nodes = []
        self.pos_list = []
        self.root = None
        self.root_pos = None
        self.root_id = None
        self.root_lemma = None
        self.lexical_unit = None
        self.object = None # TODO, if necessary
        self.subject = None # TODO, if necessary

    def __str__(self):
        return "({},{})".format(self.root, self.nodes)
    
def build_tree(lines, ticker):
    tree = Tree()     
    tree.minute = minutes[0]
    tree.ticker = ticker
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
            tree.pos_list.append(cells[5])
            node.form = cells[7]
            node.head = cells[9]
            node.type = cells[11]
                    
            # using "head == 0" so that it works for German or English
            if cells[9] == "0":
                tree.root = cells[3]
                tree.root_pos = cells[5]
                tree.root_id = cells[0]
                tree.root_lemma = cells[3]          
                
        tree.nodes.append(node)
            
    # sometimes the parsed conll file might have empty lines at the end
    # so need test to make sure we don't add empty trees
    if tree.root != None: return tree

minutes = [0]

def read_ticker(parsed_ticker, verbose, language):
    if verbose: print "Reading ticker..."

    # open and split the file
    rawsentences = open(parsed_ticker).read().replace("Ö","O").replace("á","a").replace("í","i").replace("é","e").split("\n\n")
    trees = []
    ticker = re.search(".*/(p[0-9])[\_a-zA-Z]*\.parsed", parsed_ticker)
    ticker = ticker.group(1)
    
    
    for rawsentence in rawsentences:
        # check for sentences that should be split - conjunctions or "who" with finite verbs on each side
        to_split = re.search("VBZ(\n|.)*(\n).*(and|but|who)(\n|.)*VBZ", rawsentence)
        print rawsentence
        print "===================="
        
        lines = rawsentence.split('\n')
        
        if len(lines) == 1:
            cells = lines[0].split("\t")
            if len(cells) > 1:
                if cells[5] == "CD":
                    minutes.pop()
                    minutes.append(cells[1])
                    
        elif to_split != None:
            split = re.sub("(.*VBZ)(\n|.)*(\n)(.*)(and|but|who)(\n|.)*(VBZ.*)", "\1\2\3\n\4\5\6\7", rawsentence)
            print split

        else:
            trees.append(build_tree(lines, ticker))

    
    # and add IDs
    ids = len(trees)
    for tree in trees:
        ids -= 1
        tree.tree_id = ids
      
    if verbose:
        roots = []
        for tree in trees:
            roots.append(tree.root)
        print "Ticker trees have these roots: \n" + "  \n".join(map(str,trees))
    
    return trees