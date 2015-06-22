%%
%% State Definitions.
%%

% [Time] Dependant.

literal(L)		:- fluent(L).
literal(neg(L)) :- fluent(L).

contrary(F,neg(F))	:- fluent(F).
contrary(neg(F),F)	:- fluent(F).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Initial State.
%

holds(F,0)	:- init(F).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Holds Property.
%

% Law of Inertia

holds(F,T+1)	:- holds(F,T), contrary(F,FF), not holds(FF,T+1), time(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Event Effects.
%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PASS 
		% James mentioned last time that this is the way Torsten preferred, from 
		% one of his talks -> makes things more flexible (e.g. when one of them 
		% is unknown).
		% A pass event in kicktionary is defined by:

%    PASSER

holds(neg(ball(PlayerA)),Time+1)	:- ticker(pass(Id),Time), attribute(passer,PlayerA,Id).

%    RECIPIENT

holds(    ball(PlayerB) ,Time+1)	:- ticker(pass(Id),Time), attribute(recipient,PlayerB,Id).

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

holds(score(S1,Team),Time+1)	:- ticker(score(Id),Time), team(Team,1), attribute(score,S1,S2,Id).
holds(score(S2,Team),Time+1)	:- ticker(score(Id),Time), team(Team,2), attribute(score,S1,S2,Id).

%    LEADER
%    TEAMS

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SUBSTITUTE
%    COACH
%    SUBSTITUTED_PLAYER

holds(neg(player(P)),Time+1)	:- ticker(substitute(Id),Time), attribute(subsituted_player,P,Id).
holds(bench(P),Time+1)			:- ticker(substitute(Id),Time), attribute(subsituted_player,P,Id).

%    SUBSTITUTE

holds(player(P),Time+1)		:- ticker(substitute(Id),Time), attribute(substitute,P,Id).
holds(neg(bench(P)),Time+1)	:- ticker(substitute(Id),Time), attribute(substitute,P,Id).

%    TEAM
%    LINEUP

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#show holds/2.
