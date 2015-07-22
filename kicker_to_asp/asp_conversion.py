#!/usr/bin/env python

from meta_scrape import meta_scrape
import string

def to_asp(events, write=True, display=True):
	team_one, team_two, player_data, bench_data = meta_scrape()

	asp = []
    ## META SECTION ##
    # Match Statistics Initialization.
	asp.extend((    '#const maxScore=20.',
                    'score(0..maxScore).',
                    'time(0,0).'
                    ))

    # Teams --> FROM METADATA
	asp.extend((    'team(%s,1).' % team_one,
                    'team(%s,2).' % team_two
                    ))

    # Players & Their Teams: Team One --> FROM METADATA
	for p,t in player_data:
		asp.append( 'player(%s,%s).' % (p,t) )

	for b,t in bench_data:
		asp.append( 'bench(%s,%s).' % (b,t) )

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

    ## DYNAMIC ACTION!!!
	for i in events:
		a = i.ticker
		# TODO: add second argument to represent second time unit.
		b = i.minute
		c = i.text.split()
		d = i.arguments
		e = int(i.event_id)
		f = i.frame.lower()
		asp.append( 'ticker(%s,%s,%s,%s).' % (e,b,f,a) )

        for j in i.arguments:
            asp.append( 'attribute(%s,%s,%s,%s,%s).' % (e,b,f,j.lower(),i.arguments[j].replace(' ','_').lower()) )

	if write == True:
		f = open('game_instance.lp','w+')
	for item in asp:
		f.write(item + '\n')
	f.close()

	if display == True:
		for i in asp:
			print i
    
	return asp

