%
% --ASP INSTANCE FILE--
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
init(neg(ball(P)))  :- player(P).


%%
%% Sample Ticker Sentences and their Events.
%%
%% ticker(Event,Time)
%% attribute(Event,Frame,Value)

% Ramires completes a fine lofted pass to Remy down-field.

ticker(pass(1),1). 
attribute(pass(1),passer,ramires).
attribute(pass(1),recipient,remy).

% Remy turns, shoots, and scores! Chelsea leads 1-0.

ticker(score(2),2).
attribute(score(2),team,chelsea).
attribute(score(2),score,1,0).

% Ramsey is substituted for Violand.

ticker(substitute(3),3).
attribute(substitute(3),substituted_player,ramsey).
attribute(substitute(3),substitute,violand).

% A fine pass from Violand!

ticker(pass(4),4).
attribute(pass(4),passer,violand).

% Now Oezil passes the ball up the left side back to Violand.

ticker(pass(5),5).
attribute(pass(5),passer,oezil).
attribute(pass(5),recipient,violand).	






















