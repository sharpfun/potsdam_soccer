#!/usr/bin/env python

# Reads in the kicktionary xml file and returns a list of LexicalUnit objects

from bs4 import BeautifulSoup

class LexicalUnit(object):

	def __init__(self):
		self.lemma = None
		self.scenario = None
		self.frame = None
		self.lang = None
		self.lu_id = None
		self.wordclass = None
		self.super_scenario = None
		self.synset = None
		self.frynset = None
		self.arguments = []

	def __str__(self):
		return self.lemma.replace("\n", " ") if self.lemma else "-"

	__repr__ = __str__


# TODO: read in possible arguments for each lexical unit (?)
#class Argument(object):
#
#    def __init__(self):
#        self.name = None
#        self.type = None

def read_kicktionary(kicktionary_xml, verbose, language):
	if verbose: print "Reading Kicktionary..."
	
	kicktionary = []
	soup = BeautifulSoup(open(kicktionary_xml), "xml")
	lus = soup("LEXICAL-UNIT")

	for item in lus:
		lu = LexicalUnit()
		lu.lemma = item.string
		lu.scenario = item["scenario"]
		lu.frame = item["frame"]
		lu.lang = item["lang"]
		lu.lu_id = item["lu-id"]
		lu.wordclass = item["wordclass"]
		lu.super_scenario = item["super-scenario"]
		lu.synset = item["synset"]
		#lu.frynset = item["frynset"]
		lu.arguments = []
		if language == lu.lang: kicktionary.append(lu)

	if verbose: print "Read in " + str(len(kicktionary)) + " lexical units"

	return kicktionary

