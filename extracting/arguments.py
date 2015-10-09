#!/usr/bin/env python

from frame_extract import *
from ticker import *
import re

# Returns a list of events with arguments identified

class Event(object):

    def __init__(self):
        self.ticker = None
        self.minute = None
        self.event_id = None
        self.frame = None
        self.text = None
        self.tree = None
        self.agent = None
        self.animate_obj = None
        self.inanimate_obj = None
        self.arguments = {}

    def __str__(self):
        return "Event(id={},frame={},time={})".format(
            self.event_id,self.frame,self.minute)

    __repr__ = __str__
        
def previous_node(node, tree):
    for n in tree.nodes:
        if int(n.node_id) == int(node.node_id) - 1:
            return n

def next_node(node, tree):
    for n in tree.nodes:
        if int(n.node_id) == int(node.node_id) + 1:
            return n

def parent(node, tree):
    for n in tree.nodes:
        if int(n.node_id) == int(node.head):
            return n

def child(node, tree):
    for n in tree.nodes:
        if int(n.head) == int(node.node_id):
            return n

def get_agent(node, tree):
    # if the root is a noun or a past participle, the agent is likely a by-agent
    if tree.root_pos.startswith("N") or tree.root_pos == "VBN" or tree.root_lemma == "be":
        if previous_node(node, tree):
            if previous_node(node,tree).lemma == ("by" or "from") and node.pos.startswith("N"):
                if next_node(node, tree):
                    if next_node(node, tree).pos == "NNP": # check if it's multi-word
                        return node.word + " " + next_node(node, tree).word
                else:
                    return node.word
    # if the root is an active verb
    elif tree.root_pos.startswith("V") and tree.root_lemma != "be":
        if parent(node, tree):
            if parent(node, tree).node_id == tree.root_id and node.type == "SBJ" and node.pos == "NNP":
                # doesn't work because of common nouns: or (previous_node(node,tree) == None and node.pos !="PRP")):
                agent = node.word
                if previous_node(node, tree):
                    if previous_node(node, tree).pos == "NNP" and previous_node(node,tree).lemma != "substitution:":
                        agent = previous_node(node, tree).word + " " + agent
                if next_node(node, tree):
                    if next_node(node, tree).pos == "NNP":
                        agent = agent + " " + next_node(node, tree).word
                return agent

def get_animate_object(node, tree):
    # basically just check for OBJ and pos NNP
    if node.type == "OBJ" and node.pos == "NNP":
        obj = node.word
        if previous_node(node, tree):
            if previous_node(node, tree).pos == "NNP":
                obj = previous_node(node, tree).word + " " + obj
        if next_node(node, tree):
            if next_node(node, tree).pos == "NNP":
                obj = obj + " " + next_node(node, tree).word
        return obj
    # if the sentence is passive, the subject is really the object
    elif tree.root_lemma == "be" and "VBN" in tree.pos_list:
        if parent(node, tree):
            if parent(node, tree).node_id == tree.root_id and node.type == "SBJ" and (node.pos == "NNP" or previous_node(node,tree) == None):
                obj = node.word
                if previous_node(node, tree):
                    if previous_node(node, tree).pos == "NNP":
                        obj = previous_node(node, tree).word + " " + obj
                if next_node(node, tree):
                    if next_node(node, tree).pos == "NNP":
                        agent = obj + " " + next_node(node, tree).word
                return obj

def get_inanimate_object(node, tree):
    # basically just check for OBJ and pos NN
    if node.type == "OBJ" and node.pos == "NN":
        obj = node.word
        if previous_node(node, tree):
            if previous_node(node, tree).pos == "NN":
                obj = previous_node(node, tree).word + " " + obj
        if next_node(node, tree):
            if next_node(node, tree).pos == "NN":
                obj = obj + " " + next_node(node, tree).word
        return obj

def find_frame(lu):
    # mapping of lexical units to frames
    if lu.startswith("shot"): return "Shot"
    elif lu.startswith("effort"): return "Shot"
    elif lu.startswith("attempt"): return "Shot"
    elif lu.startswith("head"): return "Shot"
    # did not map to "Shot_Supports as most examples were direct shots
    elif lu.startswith("unleash"): return "Shot"
    elif lu.startswith("strike"): return "Shot"

    elif lu.startswith("pass"): return "Pass"
    elif lu.startswith("cross"): return "Pass"
    elif lu.startswith("through-ball"): return "Pass"

    elif lu.startswith("intercept"): return "Intercept"

    elif lu.startswith("offside"): return "Offside"

    elif lu.startswith("foul"): return "Foul"

    elif lu.startswith("clear"): return "Intervene"
    elif lu.startswith("block"): return "Intervene"
    elif lu.startswith("save"): return "Intervene"

    elif lu.startswith("free-kick"): return "Set_Piece"
    elif lu.startswith("corner"): return "Set_Piece"
    elif lu.startswith("set-piece"): return "Set_Piece"

    elif lu.startswith("tackle"): return "Challenge"

    elif lu.startswith("opportunity"): return "Chance"
    elif lu.startswith("chance"): return "Chance"

    elif lu.startswith("yellow"): return "Sanction"
    elif lu.startswith("red"): return "Sanction"

    elif lu.startswith("goal."): return "Goal"

    else: return None

def find_arguments(ticker, verbose):
    if verbose: print "Identifying arguments..."
    
    events = []
    
    for item in possible_lus:
        tree = item.tree
        lu0, lu1 = None, None
        
        if item.lexical_units: lu0 = item.lexical_units[0]
        if len(item.lexical_units) > 1: lu1 = item.lexical_units[1]
        if True: #tree.lexical_unit != None:
            event = Event()
            event.ticker = tree.ticker
            event.minute = tree.minute
            event.event_id = tree.tree_id
            event.frame = "" #tree.lexical_unit
            event.tree = tree
            event.text = ""
            # get generic agents and objects
            for node in tree.nodes:
                event.text = event.text + node.word + " " # get just text
                if get_agent(node, tree) != None:
                    event.agent = get_agent(node, tree)
                if get_animate_object(node, tree) != None:
                    event.animate_obj = get_animate_object(node, tree)
                if get_inanimate_object(node, tree) != None:
                    event.inanimate_obj = get_animate_object(node, tree)
                #means = get_means(node, tree)
        
                #if agent != None: print "agent is", agent
                #if obj != None: print "object is", obj
            
            # get specific arguments for different events
            # test first with substitutions
            if tree.root_lemma == "replace": event.frame = "Substitute"
            if tree.root_lemma == "assist": event.frame = "Pass"
            if tree.root_lemma == "pass": event.frame = "Pass"
            if tree.root_lemma == "foul": event.frame = "Foul"
            if tree.root_lemma == "goal" and len(tree.nodes) > 1: event.frame = "Goal"
            if tree.nodes[0].lemma == "goal": event.frame = "Goal"
            if re.search("goal\skick", event.text) : event.frame = "Set_Piece" # to make sure goal kicks are not mixed with goals
            if event.text.startswith("SUBSTITUTION") : event.frame = "Substitute"
            if event.text.startswith("BOOKING") : event.frame = "Sanction"

            
            # otherwise look at lexical units passed from frameextract and get frames from there, looking at first and second lus
            if event.frame == None and lu0: event.frame = find_frame(lu0, kicktionary)
            if event.frame == None and lu1: event.frame = find_frame(lu1, kicktionary)                
            
            if event.frame == "Substitute":
                if event.agent != None: event.arguments["SUBSTITUTE"] = event.agent
                if event.animate_obj != None: event.arguments["SUBSTITUTED_PLAYER"] = event.animate_obj
            
            if event.frame == "Pass":
                if event.agent != None: event.arguments["PASSER"] = event.agent
                recipient = re.search("to\s([A-Z][a-z]+(\s[A-Z][a-z]+)?)", event.text) # or look for inanimate indirect object generally?
                if recipient: event.arguments["RECIPIENT"] = recipient.group(1)
                
            if event.frame == "Foul":
                if event.agent != None: event.arguments["OFFENDER"] = event.agent
                if event.animate_obj != None: event.arguments["OFFENDED_PLAYER"] = event.animate_obj
            
            events.append(event)
    # return a list of events with arguments identified    
    return events
        
# for testing
def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="../data/kicktionary.xml")
    parser.add_option("--ticker", dest="ticker", help="location of parsed ticker conll file", default="../data/p5.parsed")
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

    return events

if __name__ == "__main__":
    main()
 
