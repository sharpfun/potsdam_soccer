#!/usr/bin/env python

# Defines Verb class and read_verbnet() function.
# Reads in Verbnet xml files and returns list of Verb objects.

import os

from bs4 import BeautifulSoup


# TODO: Add in other useful attributes from Verbnet .xml files.
class Verb(object):

    def __init__(self):
        self.lemma = None
        self.frame = None


# TODO: read in possible arguments for each lexical unit (?).      
class Argument(object):

    def __init__(self):
        self.name = None
        self.type = None


def read_verbnet(verbnet_folder, verbose, language):
    if verbose: print "Reading Verbnet..."
   
    verbnet = []
    for filename in os.listdir(verbnet_folder):
        if verbose: print "Loading Verb net file " + filename
        soup = BeautifulSoup(open(verbnet_folder + "/" + filename), "xml")
        verb = soup("MEMBER")
        frame = soup("VNCLASS")
   
        for item in verb:
            vb = Verb()
            vb.lemma = item["name"]
            vb.frame = frame["ID"]
            print "%s + (%s)" % vb.lemma, vb.frame
            verbnet.append(vb)     
  
    if verbose: print "Read in " + str(len(verbnet)) + " verbnet verbs"   
       
    return verbnet
