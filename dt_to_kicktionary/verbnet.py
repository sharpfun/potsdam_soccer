#!/usr/bin/env python

# Reads in the verbnet xml files and returns a list of verbnet objects

import os
from bs4 import BeautifulSoup

class Verb(object):
    def __init__(self):
        self.lemma = None
        self.frame = None
        self.grouping = None

# TODO: read in possible arguments for each lexical unit (?)        
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
    
        for item in verb:
            vb = Verb()
        
            vb.lemma = item["name"]
            #vb.grouping = item["grouping"]
            vb.arguments = []
            
            frame = soup("VNCLASS")
            #for item in frame:
            #    vb.frame = frame["ID"]
            
            #print vb.lemma
            verbnet.append(vb)        
   
    if verbose: print "Read in " + str(len(verbnet)) + " verbnet verbs"    
        
    return verbnet