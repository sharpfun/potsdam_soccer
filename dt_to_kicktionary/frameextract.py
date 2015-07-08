#!/usr/bin/env python

# Main script for identifying Kicktionary (and Verbnet) frames for ticker sentences
# 1. First look up only roots in Kicktionary directly
# 2. Then look up roots and objects
# 3. Then look up roots in Verbnet
# 4. With Verbnet frames, look up in Kicktionary again

from __future__ import division
from bs4 import BeautifulSoup
import nltk, copy, collections, xml.sax
from kicktionary import *
from ticker import *
from verbnet import *
from sys import stdin
import sys

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

def kicktionary_lookup_possible_lu(kicktionary, ticker, verbose):
    if verbose: print "Looking up tree roots in Kicktionary..."
    
    res = []

    for tree in ticker:
        found_lus = []
        prev_node = None
        for node in tree.nodes:
            is_lu_found = False
            # searching for lexical units like free-kick or kick-off
            if prev_node != None:
                prev_node_type = None
                if prev_node.pos.startswith('VB'):
                    prev_node_type = 'v'
                elif prev_node.pos.startswith('NN'):
                    prev_node_type = 'n'
                for lu in kicktionary:
                    if lu.lu_id.replace("_","-").startswith(prev_node.lemma+"-"+node.lemma+"."):
                        if prev_node_type != None:
                            prev_node_lu = prev_node.lemma + "." + prev_node_type
                            while len(found_lus) > 0 and found_lus[-1] == prev_node_lu:
                                found_lus.pop()
                        found_lus.append(lu.lu_id);
                        if verbose: 
                            print str(tree.tree_id) + " cool matches: " + lu.lu_id + "." + lu.wordclass + " " + lu.wordclass
                        is_lu_found = True
            
            # usual one word lexical unit search
            if is_lu_found == False:
                for lu in kicktionary:
                    if node.lemma == lu.lemma:
                        if ((lu.wordclass == 'v' and node.pos.startswith("VB")) or
                            (lu.wordclass == 'n' and node.pos.startswith('NN'))):
                            found_lus.append(lu.lemma+"."+lu.wordclass);
                            if verbose: print str(tree.tree_id) + " matches: " + lu.lemma + " " + lu.wordclass
            prev_node = node
        
        plu = PossibleLU()
        plu.tree = tree
        plu.lexical_units = found_lus

        if verbose:
            print plu.sentence()
            print "set of lexical units:"
            print plu.lexical_units
            print ""

        res.append(plu)
    ## TODO: find when the tree root matches more than one Kicktionary lexical unit
    ## and somehow disambiguate
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

        print "type priority with sentence split, for example '0-5:3;6-8:6' or just '3':"
        lu_priority = stdin.readline().strip()
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
                s += 'lu("'+output_prefix+"_"+str(plu.tree.tree_id)+'_'+str(group_index)+'","'
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


def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="../data/kicktionary.xml")
    parser.add_option("--ticker", dest="ticker", help="location of parsed ticker conll file", default="../data/p2_kamil.parsed")
    parser.add_option("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
    parser.add_option("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder
    parser.add_option("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="../data/verbnet")
    parser.add_option("--luorder", dest="luorder", help="location of folder with lexical unit order file", default="../data/luorder")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language

    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    ticker = read_ticker(options.ticker, verbose, language)
    # verbnet = read_verbnet(options.verbnet)
    
    possible_lus = kicktionary_lookup_possible_lu(kicktionary, ticker, verbose)
    #order_lu(possible_lus, options.luorder)

    remove_duplicate_sequent_lus(possible_lus)

    order_lu(possible_lus, options.luorder)

    for plu in possible_lus:
        print plu.sentence()
        print plu.lexical_units

<<<<<<< HEAD
    luorder = [line.rstrip('\n') for line in open(options.luorder).readlines()]
    ticker_with_lus = kicktionary_lookup_possible_lu(kicktionary, ticker, verbose, luorder)
    
=======
    #do_asp_facts(possible_lus, options.ticker+".lp")

>>>>>>> 5c1b44361b1186dad923cd51eaf286944b8c2abc
if __name__ == "__main__":
    main()
