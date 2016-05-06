#!/usr/bin/env python
# -*- coding: utf-8 -*-

## ticker.py
## Reads in a parsed ticker feed in dependency tree conll format, converts this
## information to tree format, and returns a list of ticker Tree objects.
##

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
        return "n({},{},{})".format(self.head, self.lemma, self.type)
    
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
        self.object = None
        self.subject = None

    def __str__(self):
        return "t({},{})".format(self.root, self.nodes)

    __repr__ = __str__


def read_ticker(parsed_ticker, verbose, language):
    if verbose: print "Reading ticker..."

    # Read in a parsed ticker and populate ticker Tree objects.
    rawsentences = open(parsed_ticker).read().replace("Ö","O")	\
				                             .replace("á","a")	\
										     .replace("í","i")	\
											 .replace("é","e")	\
											 .split("\n\n")
    trees = []
    ticker = re.search(".*\/parsed\/([A-z-]*)~?\.parsed", parsed_ticker)
    ticker = ticker.group(1) #"\'" + parsed_ticker + "\'" #ticker.group(1)
    minutes = [0]

    for rawsentence in rawsentences:
        lines = rawsentence.split('\n')

        if len(lines) == 1:
            cells = lines[0].split("\t")
            if len(cells) > 1:
                if cells[5] == "CD":
                    minutes.pop()
                    minutes.append(cells[1])

        else:
            tree = Tree()
            tree.minute = minutes[0]
            tree.ticker = ticker
            # NOTE: English parses don't have "form."
            # 		Types are different between English and German,
            # 		i.e. ROOT vs. --
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

                    # Using "head == 0" so it works for German *or* English.
                    if cells[9] == "0":
                        tree.root = cells[3]
                        tree.root_pos = cells[5]
                        tree.root_id = cells[0]
                        tree.root_lemma = cells[3]

                    tree.nodes.append(node)

            # The parsed conll file might have empty lines at the end, so need 
			# to test to make sure we don't add empty tree objects.
            if tree.root != None: trees.append(tree)

    # Propogate tree_id attribute.
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

