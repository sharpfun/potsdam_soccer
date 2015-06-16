%%
%% Mostly about state definitions
%%

%> depends on [time]

literal(L)      :- fluent(L).
literal(neg(L)) :- fluent(L).

contrary(F,neg(F)) :- fluent(F).
contrary(neg(F),F) :- fluent(F).

%
% definition of the initial state
%
holds(F,0) :- init(F).


%
% holds definition
%

% inertia
holds(F,T+1) :- holds(F,T), contrary(F,FF), not holds(FF,T+1), time(T).

% effects of an event

%> PASS
% james mentioned last time, that this is the way torsten prefered in one of his
% talks -> makes things more flexible, e.g. one of them is unknown
% A pass event in kicktionary is defined by:
%    PASSER
holds(neg(ball(PlayerA)),Time+1)    :- ticker(pass(Id),Time), passer(Id,PlayerA).
%    RECIPIENT
holds(    ball(PlayerB) ,Time+1)    :- ticker(pass(Id),Time), recipient(Id,PlayerB).
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
% ... handle more? we then have to define mroe specific values like placed for target etc.

%> SCORE
%    SCORE
holds(score(S1,Team),Time+1)    :- ticker(score(Id),Time), team(Team,1), score(Id,S1,S2).
holds(score(S2,Team),Time+1)    :- ticker(score(Id),Time), team(Team,2), score(Id,S1,S2).
%    LEADER
%    TEAMS

%> SUBSTITUTE
%    COACH
%    SUBSTITUTED_PLAYER
holds(neg(player(P)),Time+1)  :- ticker(substitute(Id),Time), subsituted_player(Id,P).
holds(bench(P),Time+1)        :- ticker(substitute(Id),Time), subsituted_player(Id,P).
%    SUBSTITUTE
holds(player(P),Time+1)       :- ticker(substitute(Id),Time), substitute(Id,P).
holds(neg(bench(P)),Time+1)   :- ticker(substitute(Id),Time), substitute(Id,P).
%    TEAM
%    LINEUP

#show holds/2.
