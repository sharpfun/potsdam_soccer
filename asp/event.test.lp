%
% FOR TESTING
% Later, this is done by the ticker framework dynamically.
%

#const maxScore=20.

%% Statistics, such as.
score(0..maxScore).
time(0..10).

player(oezil, arsenal).
player(ramsey, arsenal).
player(ramires, chelsea).
player(remy, chelsea).

bench(clayton, arsenal).
% ...

% And for better usability.
% just a few derivations of the statics
player(P) :- player(P,T).
team(T)   :- player(P,T).
team(arsenal, 1).
team(chelsea, 2).

%%
%% Fluents Definitions.
%% (what is a state described in the [soccer] world)
%%
fluent(score(S,T)) :- score(S), team(T).
fluent(ball(P))    :- player(P).
fluent(player(P))  :- player(P).
fluent(player(P))  :- bench(P).
fluent(bench(P))   :- player(P).
fluent(bench(P))   :- bench(P).

%%
%% init(Property).
%%
init(score(0,T))  	:- team(T).
init(player(P))   	:- player(P).
init(bench(P))    	:- bench(P).
%init(neg(ball(P))) :- player(P).








%%
%% Here come sample sentences (their asp representation)
%%

%% ticker(Time,Event)

% Ramires completes a fine lofted pass to Remy down field.

ticker(pass(1),1). 
passer(1,ramires).
recipient(1,remy).

% holds(neg(ball(ramires)),Time+1) :- ticker(pass(1),1), passer(1,ramires).
% holds(ball(remy),Time+1) :- ticker(pass(1),Time), recipient(1,remy).

%holds(neg(ball(PlayerA)),Time+1)    :- ticker(pass(Id),Time), passer(Id,PlayerA).
%holds(    ball(PlayerB) ,Time+1)    :- ticker(pass(Id),Time), recipient(Id,PlayerB).



% Remy turns, shoots, and scores! Chelsea leads 1-0.

ticker(shoot(2), 2).
shooter(2,Remy).

% holds(score(1,chelsea),Time+1) :- ticker(score(2),Time), team(chelsea,1), score(2,1,0).
% holds(score(0,arsenal),Time+1) :- ticker(score(2),Time), team(chelsea,2), score(2,1,0).

%holds(score(S1,Team),Time+1) :- ticker(score(Id),Time), team(Team,1), score(Id,S1,S2).
%holds(score(S2,Team),Time+1) :- ticker(score(Id),Time), team(Team,2), score(Id,S1,S2).



% Ramsey is substituted for Violand.

ticker(substitute(3),3).
substituted_player(3,ramsey).
substitute(3,violand).

%holds(neg(player(P)),Time+1)  :- ticker(substitute(Id),Time), subsituted_player(Id,P).
%holds(bench(P),Time+1)        :- ticker(substitute(Id),Time), subsituted_player(Id,P).
%holds(player(P),Time+1)       :- ticker(substitute(Id),Time), substitute(Id,P).
%holds(neg(bench(P)),Time+1)   :- ticker(substitute(Id),Time), substitute(Id,P).



% A fine pass from Violand!

ticker(pass(4), 4).
passer(4,violand)

% Now Oezil passes the ball up the left side back to Violand.

ticker(pass(5), 5).
passer(5,oezil)
recipient(5,violand)	

