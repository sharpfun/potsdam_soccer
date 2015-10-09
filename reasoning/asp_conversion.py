#!/usr/bin/env python

from meta_scrape import meta_scrape
import string
import re

import extracting.arguments

def to_asp(events, write=False, display=False):
    def conv(x):
        if x:
            return x.lower().replace(".", "").replace(" ", "_")
        else:
            return "none"

    team_one, team_two, player_data, bench_data = meta_scrape()

    asp = []
    ## META SECTION ##
    # Match Statistics Initialization.
    asp.extend((    '#const maxScore=20.',
                    'score(0..maxScore).',
                    'time(0,0).'
                    ))

    # Teams --> FROM METADATA
    asp.extend((    'team({},1).'.format(team_one),
                    'team({},2).'.format(team_two)
                    ))

    # Players & Their Teams: Team One --> FROM METADATA
    for p,t in player_data:
        asp.append( 'player({},{}).'.format(conv(p),conv(t)))

    for b,t in bench_data:
        asp.append( 'bench({},{}).'.format(conv(b),conv(t)))

    ## FOR EASE OF USE DOWN THE ROAD... ##
    asp.extend((    'player(P) :- player(P,T).',
                    'team(T)   :- player(P,T).',
                    'bench(P)  :- bench(P,T).'
                    ))

    ## FLUENTS ##
    asp.extend((    'fluent(score(S,T)) :- score(S), team(T).',
                    'fluent(ball(P))    :- player(P).',
                    'fluent(player(P))  :- player(P).',
                    'fluent(player(P))  :- bench(P).',
                    'fluent(bench(P))   :- player(P).',
                    'fluent(bench(P))   :- bench(P).'
                    ))

    ## INITS ##
    asp.extend((    'init(score(0,T))    :- team(T).',
                    'init(player(P))     :- player(P).',
                    'init(bench(P))      :- bench(P).',
                    'init(neg(ball(P)))  :- player(P).'
                    ))

    ####################
    noneCtr = 0
    ## DYNAMIC ACTION!!!
    for event in events:
        tickerId = int(event.event_id)
        tickerSrc = conv(event.ticker)
        # convert time argument.
        time = map(int,re.findall(r"\d+",str(event.minute)))
        aspTime = time[0]*100
        if len(time) == 2:
            aspTime += time[1]
        tickerFrame = conv(event.frame)

        asp.append('ticker({},{},{},{}).'.format(
            tickerId,tickerSrc,tickerFrame,aspTime))

        # Operations on Time variable.
        #
        for arg,argval in event.arguments.iteritems():
            asp.append('attribute({},{},{},{},{}).'.format(
                tickerId,tickerSrc,tickerFrame,
                conv(arg), conv(argval)))

        if tickerFrame == "none":
            noneCtr += 1

    #print "Nones:", noneCtr
    #print "ratio:", float(noneCtr)/len(events)
    #raw_input()

    if write:
        with open('game_instance.lp','w+') as f:
            f.write("\n".join(asp))
    if display:
        print "\n".join(asp)

    return "\n".join(asp)

def to_frames(atoms):
    events = []
    for (time,frame) in sorted([atom.args() for atom in atoms if atom.name() == "timeline"], key=lambda x: x[0]):
        e = extracting.arguments.Event()
        e.minute = "{}'+{}'".format(time/100, time%100)
        e.frame  = frame
        for _,_,arg,argval in (atom.args() for atom in atoms if atom.name() == "timeline_attr" and atom.args()[0] == time and atom.args()[1] == frame):
            e.arguments[arg] = argval
        events.append(e)
    
    return events
