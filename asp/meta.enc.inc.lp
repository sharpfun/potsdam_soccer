%%
%% State Definitions.
%%
#program base.
% auxiliary constructs
complement(F,neg(F))    :- fluent(F).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initial State.
holds(F,0)	:- init(F), complement(F,L).

#program inc(t).

% Law of Inertia
holds(F,t+1)	:- holds(F,t), complement(F,L), not caused(L,t+1).

% Law of Causal Effects
holds(F,t+1)    :- caused(F,t), complement(F,L).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% What happens if we have different tickers?
% - for now, it just maps all messages to the original ticker -

ticker(Id,Frame,t)                              :- ticker(Id,Src,Frame,t).
attribute(Id,Frame,FrameAttribute,FrameValue,t) :- attribute(Id,Src,Frame,FrameAttribute,FrameValue,t).


%
% Event Effects.
%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PASS 
%    PASSER
caused(neg(ball(PlayerA)),t+1)	:- ticker(Id,pass,t), attribute(Id,pass,passer,PlayerA,t).
%    RECIPIENT
caused(    ball(PlayerB) ,t+1)	:- ticker(Id,pass,t), attribute(Id,pass,recipient,PlayerB,t).
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
caused(score(S1,Team),t+1)	:- ticker(Id,score,t), team(Team,1), attribute(Id,score,score,S1,S2,t).
caused(score(S2,Team),t+1)	:- ticker(Id,score,t), team(Team,2), attribute(Id,score,score,S1,S2,t).
%    LEADER
%    TEAMS

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GOAL
%    SCORER
caused(score(S+1,Team),t+1)      :- ticker(Id,goal,t), team(Player,Team), holds(score(S,Team),t), attribute(Id,goal,scorer,Player,t).
caused(neg(score(S,Team)),t+1)   :- ticker(Id,goal,t), team(Player,Team), holds(score(S,Team),t), attribute(Id,goal,scorer,Player,t).
%    SCORER_TEAM
caused(score(S+1,Team),t+1)      :- ticker(Id,goal,t), holds(score(S,Team),t), attribute(Id,goal,scorer_team,Team,t).
caused(neg(score(S,Team)),t+1)   :- ticker(Id,goal,t), holds(score(S,Team),t), attribute(Id,goal,scorer_team,Team,t).
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
caused(neg(player(P)),t+1)   :- ticker(Id,substitute,t), attribute(Id,substitute,subsituted_player,P,t).
caused(bench(P),t+1)			    :- ticker(Id,substitute,t), attribute(Id,substitute,subsituted_player,P,t).
%    SUBSTITUTE
caused(player(P),t+1)		    :- ticker(Id,substitute,t), attribute(Id,substitute,substitute,P,t).
caused(neg(bench(P)),t+1)	  :- ticker(Id,substitute,t), attribute(Id,substitute,substitute,P,t).
%    TEAM
%    LINEUP

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%#show holds/2.
%#show ticker/3.
%#show attribute/4.
