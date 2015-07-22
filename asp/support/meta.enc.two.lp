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
% What happens if we have different tickers?
% - for now, it just maps all messages to the original ticker -
%
% Source is a number from 1 to len(sources)
% priority included -- the lower, the more confidence
%
ticker(Id,Frame,Time)                         :- ticker(Id,Src,Frame,Time).
attribute(Id,Frame,FrameAttribute,FrameValue) :- attribute(Id,Src,Frame,FrameAttribute,FrameValue).

%%%
%%% Event Effects.
%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% PASS 
%%%    PASSER
%%caused(neg(ball(PlayerA)),Time+1)	:- ticker(Id,pass,Time), attribute(Id,pass,passer,PlayerA).
%%%    RECIPIENT
%%caused(    ball(PlayerB) ,Time+1)	:- ticker(Id,pass,Time), attribute(Id,pass,recipient,PlayerB).
%%%    TARGET
%%%    SOURCE
%%%    DIRECTION
%%%    BALL
%%%    PART_OF_BODY
%%%    PASS
%%%    DISTANCE
%%%    PATH
%%%    MOVING_BALL
%%%    SHOT
%%		% ...to handle more? We would then have to define mroe specific values,
%%		% like "placed" for TARGET, etc.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% SCORE
%%%    SCORE
%%caused(score(S1,Team),Time+1)	:- ticker(Id,score,Time), team(Team,1), attribute(Id,score,score,S1,S2).
%%caused(score(S2,Team),Time+1)	:- ticker(Id,score,Time), team(Team,2), attribute(Id,score,score,S1,S2).
%%%    LEADER
%%%    TEAMS

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% GOAL
%%%    SCORER
%%caused(score(S+1,Team),Time+1)      :- ticker(Id,goal,Time), team(Player,Team), holds(score(S,Team),T), attribute(Id,goal,scorer,Player).
%%caused(neg(score(S,Team)),Time+1)   :- ticker(Id,goal,Time), team(Player,Team), holds(score(S,Team),T), attribute(Id,goal,scorer,Player).
%%%    SCORER_TEAM
%%caused(score(S+1,Team),Time+1)      :- ticker(Id,goal,Time), holds(score(S,Team),T), attribute(Id,goal,scorer_team,Team).
%%caused(neg(score(S,Team)),Time+1)   :- ticker(Id,goal,Time), holds(score(S,Team),T), attribute(Id,goal,scorer_team,Team).
%%%    SHOT
%%%    RESULTING_SCORE
%%%    SOURCE
%%%    PREPARING_EVENT
%%%    PREVIOUS_SCORE
%%%    PART_OF_BODY
%%%    MOVING_BALL
%%%    TARGET
%%%    GOAL
%%%    CONCEDING_TEAM
%%%    BALL
%%%    PATH

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% SUBSTITUTE
%%%    COACH
%%%    SUBSTITUTED_PLAYER
%%caused(neg(player(P)),Time+1)   :- ticker(Id,substitute,Time), attribute(Id,substitute,subsituted_player,P).
%%caused(bench(P),Time+1)			    :- ticker(Id,substitute,Time), attribute(Id,substitute,subsituted_player,P).
%%%    SUBSTITUTE
%%caused(player(P),Time+1)		    :- ticker(Id,substitute,Time), attribute(Id,substitute,substitute,P).
%%caused(neg(bench(P)),Time+1)	  :- ticker(Id,substitute,Time), attribute(Id,substitute,substitute,P).
%%%    TEAM
%%%    LINEUP

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%#show holds/2.
%%#show ticker/3.
%%#show attribute/4.
