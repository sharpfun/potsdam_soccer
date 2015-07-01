%
% --ASP INSTANCE FILE--
% FOR TESTING
% Later, this is done by the ticker framework dynamically.
%

#const maxScore=20.

%% Statistics, such as.
score(0..maxScore).
time(0).

player(oezil, arsenal).
player(ramsey, arsenal).
player(ramires, chelsea).
player(remy, chelsea).

bench(clayton, arsenal).
% ...

% And for better usability.
% just a few derivations of the statics
player(P) :- player(P,T).
bench(P)  :- bench(P,T).
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
%init(neg(ball(P)))  :- player(P).


%%
%% Sample Ticker Sentences and their Events.
%%
%% ticker(Event,Time)
%% attribute(Event,Frame,Value)

% Ramires completes a fine lofted pass to Remy down-field.

ticker(1,1,pass,1).
attribute(1,1,pass,passer,ramires).
attribute(1,1,pass,recipient,remy).

% Remy turns, shoots, and scores! Chelsea leads 1-0.

ticker(2,1,score,2).
attribute(2,1,score,team,chelsea).
attribute(2,1,score,score,1,0).

% Ramsey is substituted for Violand.

ticker(3,1,substitute,3).
attribute(3,1,substitute,substituted_player,ramsey).
attribute(3,1,substitute,substitute,violand).

% A fine pass from Violand!

ticker(4,1,pass,4).
attribute(4,1,pass,passer,violand).

% Now Oezil passes the ball up the left side back to Violand.

ticker(5,1,pass,5).
attribute(5,1,pass,passer,oezil).
attribute(5,1,pass,recipient,violand).	






















