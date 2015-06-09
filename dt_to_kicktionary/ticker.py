#!/usr/bin/env python

# Reads in a parsed ticker feed in dependency tree conll format
# And returns a list of Tree objects

# TODO: clean up tokenization for input files (punctuation, contractions like "couldn't"...)
# as they are leading to incorrect readings of part of speech

# TODO: the minute marks should somehow be added to each tree so that it can be used later in the ASP representation

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
        self.tree_id = 0
        self.nodes = []
        self.root = None
        self.lexical_unit = None
        self.object = None # TODO, if necessary
        self.subject = None # TODO, if necessary

    def __str__(self):
        return "({},{})".format(self.root, self.nodes)


def read_ticker(parsed_ticker, verbose, language):
    if verbose: print "Reading ticker..."
    
    # open and split the file
    rawsentences = open(parsed_ticker).read().split("\n\n")
    trees = []
    ids = 0
    
    for rawsentence in rawsentences:
    
        tree = Tree()
        ids += 1
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
                
                # using "head == 0" so that it works for German or English
                if cells[9] == "0":
                    tree.root = cells[3]
          
            tree.nodes.append(node)
        
        # sometimes the parsed conll file might have empty lines at the end
        # so need test to make sure we don't add empty trees
        if tree.root != None: trees.append(tree)
      
    if verbose:
        roots = []
        for tree in trees:
            roots.append(tree.root)
        print "Ticker trees have these roots: \n" + "  \n".join(map(str,trees))
    
    return trees