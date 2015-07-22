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
        # b. ??? Root--> Verbnet.Verb-->Verbnet.Sibling-->Kicktionary.
            else:
                # TO DO: Reverse look-up order
                for vb in verbnet:
                    if vb.lemma == tree.root:
                        possibleLUs = [lu for lu in kicktionary if lu.lemma == vb.frame]
                        if len(possibleLUs) >= 1:
                            if len(possibleLUs) == 1:
                                tree.lexical_unit = possibleLUs[0]
                                if verbose: print "Tree " + str(tree.tree_id) + " root matches Kicktionary lexical unit (via Verbnet frame): " + tree.lexical_unit.lemma
                            else:
                                pass # <-- how to determine??
                        else:
                            pass # <-- what next??

    return ticker

