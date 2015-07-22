#!/usr/bin/env python

from frame_extract import *
from ticker import *
import re

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
        
def find_arguments(ticker, possible_lus, verbose):
    if verbose: print "Identifying arguments..."
    
    events = []
    
    for item in possible_lus:
        tree = item.tree
        if item.lexical_units: lu0 = item.lexical_units[0]
        lu1 = None
        if len(item.lexical_units) > 1: lu1 = item.lexical_units[1]
        if True: #tree.lexical_unit != None:
            event = Event()
            event.ticker = tree.ticker
            event.minute = tree.minute
            event.event_id = tree.tree_id
            #event.frame = "" 
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
                    event.inanimate_obj = get_inanimate_object(node, tree)
            
            # get specific arguments for different events
            if tree.root_lemma == "replace": event.frame = "Substitute"
            if tree.root_lemma == "assist" or tree.nodes[0].lemma == "assist": event.frame = "Pass"
            if tree.root_lemma == "cross": event.frame = "Pass"
            if tree.root_lemma == "pass": event.frame = "Pass"
            if tree.root_lemma == "foul": event.frame = "Foul"
            if tree.root_lemma == "goal" and len(tree.nodes) > 1: event.frame = "Goal"
            if tree.nodes[0].lemma == "goal": event.frame = "Goal"
            if re.search("goal\skick", event.text) : event.frame = "Set_Piece" # to make sure goal kicks are not mixed with goals
            if event.text.startswith("SUBSTITUTION") : event.frame = "Substitute"
            if event.text.startswith("BOOKING") : event.frame = "Sanction"

            
            # otherwise look at lexical units passed from frameextract and get frames from there, looking at first and second lus
            if event.frame == None: event.frame = find_frame(lu0)
            if event.frame == None and lu1: event.frame = find_frame(lu1)                
            
            if event.frame == "Substitute":
                if event.agent != None: event.arguments["SUBSTITUTE"] = event.agent
                if event.animate_obj != None: event.arguments["SUBSTITUTED_PLAYER"] = event.animate_obj
                else:
                    # SUBSTITUTION: Meyler comes on for Livermore 
                    substituted = re.search("comes\son\sfor\s([A-Z][a-z]+(\s[A-Z][a-z\']+)?)", event.text)
                    if substituted: event.arguments["SUBSTITUTED_PLAYER"] = substituted.group(1)
            
            if event.frame == "Pass":
                if event.agent != None: event.arguments["PASSER"] = event.agent
                
                # Assist Ahmed El Mohamady
                elif tree.ticker == "p3":
                    passer = re.search("Assist\s([A-Z][a-z\']+(\s[A-Z][a-z\']+)?(\s[A-Z][a-z\']+)?)", event.text)
                    if passer: event.arguments["PASSER"] = passer.group(1)
                # A pass by Mesut Ozil ends up in no man's land
                else:
                    passer = re.search("(pass|cross)\s(by|from)\s([A-Z][a-z\']+(\s[A-Z][a-z\']+)?(\s[A-Z][a-z\']+)?)", event.text)
                    if passer: event.arguments["PASSER"] = passer.group(3)
                recipient = re.search("to\s([A-Z][a-z]+(\s[A-Z][a-z]+)?)", event.text)
                if recipient: event.arguments["RECIPIENT"] = recipient.group(1)
                
            if event.frame == "Foul":
                if event.agent != None and re.search("(blow|whistle|referee)", event.text) == None: event.arguments["OFFENDER"] = event.agent
                if event.animate_obj != None and re.search("(blow|whistle|referee)", event.text) == None: event.arguments["OFFENDED_PLAYER"] = event.animate_obj
                
            if event.frame == "Challenge":
                if event.agent != None: event.arguments["OPPONENT_PLAYER"] = event.agent
                if event.animate_obj != None: event.arguments["PLAYER_WITH_BALL"] = event.animate_obj
                
            if event.frame == "Intercept":
                if event.agent != None: event.arguments["INTERCEPTOR"] = event.agent
                
            if event.frame == "Shot":
                if event.agent != None: event.arguments["SHOOTER"] = event.agent
                
            if event.frame == "Intervene":
                if event.agent != None: event.arguments["INTERVENING_PLAYER"] = event.agent
                
            if event.frame == "Set_Piece":
                if event.agent != None: event.arguments["EXECUTING_PLAYER"] = event.agent
                
            if event.frame == "Sanction":
                # BOOKING: N'Doye
                offender = re.search("BOOKING:\s([A-Z][a-z\']+(\s[A-Z][a-z\']+)?)", event.text)
                if offender: event.arguments["OFFENDER"] = offender.group(1)
                elif event.agent != None and re.search("(blow|whistle|referee)", event.text) == None: event.arguments["OFFENDER"] = event.agent
                # Yellow Card Jake Livermore
                elif tree.ticker == "p3":
                    offender = re.search("Yellow\sCard(\s)?([A-Z][a-z\']+(\s[A-Z][a-z\']+)?(\s[A-Z][a-z\']+)?)", event.text)
                    if offender: event.arguments["OFFENDER"] = offender.group(2)
                
            if event.frame == "Chance":
                # What a chance for Aluko !
                player = re.search("(chance|opportunity)\sfor\s([A-Z][a-z\']+(\s[A-Z][a-z\']+)?)", event.text)
                if player: event.arguments["PLAYER"] = player.group(2)
                elif event.agent != None: event.arguments["PLAYER"] = event.agent
                
            if event.frame == "Offside":
                if event.agent != None: event.arguments["OFFENDER"] = event.agent
                # Dame N'Doye (Hull City) is adjudged offside . 
                elif event.animate_obj != None: event.arguments["OFFENDER"] = event.animate_obj
                
            if event.frame == "Goal":
                # Ramsey sends a pass to Sanchez who...
                if event.agent and re.search("(sends\sa)?\spass", event.text):
                    scorer = re.search("(sends\sa)?\spass(es)?\s(the\sball\s)?to\s([A-Z][a-z\']+(\s[A-Z][a-z\']+)?)", event.text)
                    if scorer: event.arguments["SCORER"] = scorer.group(4)
                elif len(tree.nodes) == 4:
                    # GOAL ! ALEXIS ! 
                    scorer = re.search("!\s([A-z\']+(\s[A-z\']+)?)\s!", event.text)
                    if scorer: event.arguments["SCORER"] = scorer.group(1)
                elif len(tree.nodes) == 3:
                    # Goal Aaron Ramsey
                    scorer = re.search("Goal\s([A-z\']+(\s[A-z\']+)?)", event.text, re.UNICODE)
                    if scorer: event.arguments["SCORER"] = scorer.group(1)
                elif event.agent != None: event.arguments["SCORER"] = event.agent
                         
            events.append(event)
    # return a list of events with arguments identified
    return events
