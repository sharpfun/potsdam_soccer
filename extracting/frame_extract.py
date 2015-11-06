#!/usr/bin/env python

## frame_extract.py
## Identifies Kicktionary/Verbnet LexicalUnit matches from ticker Tree objects.
## 1. First look up only roots in Kicktionary directly
## 2. Then try roots and objects
## 3. Then try roots in Verbnet and with these roots' corresponding Verbnet 
##      frames, try to match back to Kicktionary.
##

from __future__ import division
import sys

import nltk, copy, collections, xml.sax
from bs4 import BeautifulSoup

from kicktionary import *
from verbnet import *
from ticker import *

reload(sys)
sys.setdefaultencoding('utf8')


class PossibleLU(object):

    def __init__(self):
        self.tree = None
        self.lexical_units = None

    def sentence(self):
        s = ""
        for node in self.tree.nodes:
            s = s + node.word + " "
        return s

    def __repr__(self):
        return "{" + ",".join(self.lexical_units) + "}"


def kicktionary_lookup_possible_lu(kicktionary, verbnet, ticker, verbose):
    if verbose: print "Looking up tree roots in Kicktionary..."

    res = []

    for tree in ticker:
        # Initialize list of Kicktionary LexicalUnit matches for current ticker.
        found_lus = []
        prev_node = None
        for node in tree.nodes:
            is_lu_found = False
            # Search for lexical units like 'free-kick' or 'kick-off'.
            if prev_node != None:
                prev_node_type = None
                if prev_node.pos.startswith('VB'):
                    prev_node_type = 'v'
                elif prev_node.pos.startswith('NN'):
                    prev_node_type = 'n'
                for lu in kicktionary:
                    if lu.lu_id.replace("_","-").startswith(prev_node.lemma + "-" + node.lemma + "."):
                        if prev_node_type != None: 
                            prev_node_lu = prev_node.lemma + "." + prev_node_type
                            while len(found_lus) > 0 and found_lus[-1] == prev_node_lu:
                                found_lus.pop()
                        # Add lu_id to list of found_lus for current ticker.
                        found_lus.append(lu.lu_id)
                        if verbose:
                            print str(tree.tree_id) + " cool matches: " + lu.lu_id + "." + lu.wordclass + " " + lu.wordclass
                        is_lu_found = True

            # Search for LexicalUnit of basic type.
            if is_lu_found == False:
                for lu in kicktionary:
                    if node.lemma == lu.lemma:
                        if ((lu.wordclass == 'v' and node.pos.startswith("VB")) or (lu.wordclass == 'n' and node.pos.startswith('NN'))):
                            # Add to list of found_lus for current ticker.
                            found_lus.append(lu.lemma+"."+lu.wordclass);
                            if verbose: print str(tree.tree_id) + " matches: " + lu.lemma + " " + lu.wordclass    
            prev_node = node
#                        else:
#
#                            # Search in Verbnet
#                            for vb in verbnet:
#                                if vb.lemma == tree.root:
#                                    possibleLUs = [lu for lu in #kicktionary if lu.lemma == vb.frame]
#                                    if len(possibleLUs) >= 1:
#                                        if len(possibleLUs) == 1:
#                                            tree.lexical_unit = possibleLUs[0]
#                                            if verbose: print "Tree " #+ str(tree.tree_id) + " root matches Kicktionary lexical unit (via #Verbnet frame): " + tree.lexical_unit.lemma

        plu = PossibleLU()
        plu.tree = tree
        plu.lexical_units = found_lus

        if verbose:
            print plu.sentence()
            print "set of lexical units:"
            print plu.lexical_units
            print ""

        res.append(plu)

    ## TODO: find when the tree root matches more than one Kicktionary lexical 
    ## unit and somehow disambiguate
    return res

def remove_duplicate_sequent_lus(possible_lus):
    for plu in possible_lus:
        res = []
        for k in plu.lexical_units:
            if len(res)==0 or res[-1] != k:
                res.append(k)
        plu.lexical_units = res

def do_asp_facts(possible_lus, output_file):
    f = open(output_file,'w')
    output_prefix = output_file.split("/")[-1]

    for plu in possible_lus:
        if len(plu.lexical_units) == 0: continue
        print plu.sentence()
        s = ""
        for i in range(len(plu.lexical_units)):
            s += str(i)+". "+plu.lexical_units[i]+"   "
        print s

        print "Type priority with sentence split, such as '0-5:3;6-8:6' or '3'."
        lu_priority = sys.stdin.readline().strip()
        group_index = 0

        for group_lus_indexes in lu_priority.split(";"):
            if len(group_lus_indexes)==0:
                break
            if group_lus_indexes=='-1':
                print ""
                break
            lexical_units_range_and_main_lexical_unit = group_lus_indexes.split(":")

            if len(lexical_units_range_and_main_lexical_unit) == 2:
                lexical_units_range_split = lexical_units_range_and_main_lexical_unit[0].split("-")
                lexical_units_range = range(
                    int(lexical_units_range_split[0]),
                    int(lexical_units_range_split[1])+1)
                main_lexical_unit = int(lexical_units_range_and_main_lexical_unit[1])
            else:
                lexical_units_range = range(0,len(plu.lexical_units))
                main_lexical_unit = int(lexical_units_range_and_main_lexical_unit[0])

            for k in lexical_units_range:
                s = ""
                s += 'lu("'+output_prefix + "_" + str(plu.tree.tree_id) + '_' + str(group_index) + '","'
                s += plu.lexical_units[k]+'",'
                s += str(1 if k == main_lexical_unit else 0)+').'
                print s
                f.write(s+"\n")
                f.flush()

            group_index+=1
            print ""
            f.write("\n")

    f.close()

def order_lu(possible_lus, luorder_file):
    luorder = [line.rstrip('\n') for line in open(luorder_file).readlines()]
    luorder.reverse()
    for plu in possible_lus:
        plu.lexical_units = sorted(plu.lexical_units, key=lambda x: not(x in luorder) and 1 or -luorder.index(x))

