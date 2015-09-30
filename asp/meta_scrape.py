#!/usr/bin/env python

def meta_scrape(filepath = False):
	## Meta-Data Representing Knowledge before the Match
	## To be scraped dynamically from source, e.g.:
	## http://www.flashscore.com/match/WnVNPAX3/#lineups;1
	## Following is hard-coded for now.
	team_one = "arsenal"
	team_two = "hull_city"
	player_data = [("bellerin_h","arsenal"),("cazorla_s","arsenal"),("coquelin_f","arsenal"),("giroud_o","arsenal"),("koscielny_l","arsenal"),("mertesacker_p","arsenal"),("monreal_n","arsenal"),("ospina_d","arsenal"),("ozil_m","arsenal"),("ramsey_a","arsenal"),("sanchez_a","arsenal"),('aluko_s','hull_city'),('brady_r','hull_city'),('chester_j','hull_city'),('dawson_m','hull_sity'),('elmohamady_a','hull_city'),('harper_s','hull_city'),('huddlestone_t','hull_city'),('livermore_j','hull_city'),('mcshane_p','hull_city'),('ndoye_d','hull_city'),('quinn_s','hull_city')]
	bench_data = [('flamini_m','arsenal'),('gibbs_k','arsenal'),('gabriel','arsenal'),('rosicky_t','arsenal'),('szczesny_w','arsenal'),('walcott_t','arsenal'),('wilshere_j','arsenal'),('bruce_a','hull_city'),('hernandez_a','hull_city'),('jelavic_n','hull_city'),('mcgregor_a','hull_city'),('meyler_d','hull_city'),('robertson_a','hull_city'),('rosenior_l','hull_city')]

	return team_one, team_two, player_data, bench_data

