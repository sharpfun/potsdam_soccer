#!/usr/bin/env python

## verbnet.py
## Reads in Verbnet xml files and returns list of LexicalUnit objects.
##

import os

from bs4 import BeautifulSoup


class Verb(object):

    def __init__(self):
        self.lemma = None
        self.frame = None


def read_verbnet(verbnet_folder, verbose, language):
    if verbose: print "Reading Verbnet..."

	# Define list of Verb objects.
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

    if verbose: print "Read in " + str(len(verbnet)) + " verbs"

    return verbnet

