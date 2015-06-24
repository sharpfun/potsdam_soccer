%%
%% State Definitions.
%%

% auxiliary constructs
complement(F,neg(F))    :- fluent(F).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initial State.
holds(F,0)	:- init(F), complement(F,L).

% Law of Inertia
holds(F,T+1)	:- holds(F,T), complement(F,L), not caused(L,T+1), time(T).

% Law of Causal Effects
holds(F,T+1)    :- caused(F,T), complement(F,L).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%
% Event Effects.
%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PASS 
%    PASSER
caused(neg(ball(PlayerA)),Time+1)	:- ticker(pass(Id),Time), attribute(pass(Id),passer,PlayerA).
%    RECIPIENT
caused(    ball(PlayerB) ,Time+1)	:- ticker(pass(Id),Time), attribute(pass(Id),recipient,PlayerB).
%    TARGET
%    SOURCE
%    DIRECTION
%    BALL
%    PART_OF_BODY
%    PASS
%    DISTANCE
%    PATH
%    MOVING_BALL
%    SHOT
		% ...to handle more? We would then have to define mroe specific values,
		% like "placed" for TARGET, etc.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SCORE
%    SCORE
caused(score(S1,Team),Time+1)	:- ticker(score(Id),Time), team(Team,1), attribute(score(Id),score,S1,S2).
caused(score(S2,Team),Time+1)	:- ticker(score(Id),Time), team(Team,2), attribute(score(Id),score,S1,S2).
%    LEADER
%    TEAMS

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GOAL
%    SCORER
caused(score(S+1,Team),Time+1)      :- ticker(goal(Id),Time), team(Player,Team), holds(score(S,Team),T), attribute(goal(Id),scorer,Player).
caused(neg(score(S,Team)),Time+1)   :- ticker(goal(Id),Time), team(Player,Team), holds(score(S,Team),T), attribute(goal(Id),scorer,Player).
%    SCORER_TEAM
caused(score(S+1,Team),Time+1)      :- ticker(goal(Id),Time), holds(score(S,Team),T), attribute(goal(Id),scorer_team,Team).
caused(neg(score(S,Team)),Time+1)   :- ticker(goal(Id),Time), holds(score(S,Team),T), attribute(goal(Id),scorer_team,Team).
%    SHOT
%    RESULTING_SCORE
%    SOURCE
%    PREPARING_EVENT
%    PREVIOUS_SCORE
%    PART_OF_BODY
%    MOVING_BALL
%    TARGET
%    GOAL
%    CONCEDING_TEAM
%    BALL
%    PATH

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SUBSTITUTE
%    COACH
%    SUBSTITUTED_PLAYER
caused(neg(player(P)),Time+1)   :- ticker(substitute(Id),Time), attribute(substitute(Id),subsituted_player,P).
caused(bench(P),Time+1)			:- ticker(substitute(Id),Time), attribute(substitute(Id),subsituted_player,P).
%    SUBSTITUTE
caused(player(P),Time+1)		:- ticker(substitute(Id),Time), attribute(substitute(Id),substitute,P).
caused(neg(bench(P)),Time+1)	:- ticker(substitute(Id),Time), attribute(substitute(Id),substitute,P).
%    TEAM
%    LINEUP

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#show holds/2.
#show ticker/2.
#show attribute/3.
