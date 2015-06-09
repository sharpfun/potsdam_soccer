#!/usr/bin/env python

# Defines class "Verb" and function "read_verbnet()."
# Reads in Verbnet xml files and returns list of Verb objects.

import os
from bs4 import BeautifulSoup

# TODO: Add in other useful attributes from Verbnet .xml files.
class Verb(object):

    def __init__(self):
        self.lemma = None
        self.frame = None


# TODO: read in possible arguments for each lexical unit (?).      
#class Argument(object):
#
#    def __init__(self):
#        self.name = None
#        self.type = None


def read_verbnet(verbnet_folder, verbose, language):
    if verbose: print "Reading Verbnet..."
   
    verbnet = []
    for filename in os.listdir(verbnet_folder):
        soup = BeautifulSoup(open(verbnet_folder + "/" + filename), "xml")
        verb = soup("MEMBER")

        frame_raw = soup("VNCLASS")[0]["ID"]
        sep = '-'
        frame = frame_raw.split(sep, 1)[0]
   
        for item in verb:
            vb = Verb()
            vb.lemma = item["name"]
            vb.frame = frame
            vb.siblings = [i for i in verb if i != vb ]
            verbnet.append(vb)

        #print "(%s, Frame: %s)" % (vb.lemma, vb.frame)
  
    if verbose: print "Read in " + str(len(verbnet)) + " verbs"   
       
    return verbnet