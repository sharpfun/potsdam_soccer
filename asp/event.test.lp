%
% just for testing
% later this is done by the ticker framework dynamically
%

#const maxScore=20.

%% statics like 
score(0..maxScore).
time(0..10).
%
player(oezil, arsenal).
player(ramsey, arsenal).
player(ramires, chelsea).
player(remy, chelsea).

bench(clayton, arsenal).
% ...

% and for better usability
% just a few derivations of the statics
player(P) :- player(P,T).
team(T)   :- player(P,T).
team(arsenal, 1).
team(chelsea, 2).

%%
%% fluent definitions
%% what is a state described in the [soccer] world
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
init(score(0,T))  :- team(T).
init(player(P))   :- player(P).
init(bench(P))    :- bench(P).
%init(neg(ball(P))) :- player(P).


%%
%% Here come sample sentences (their asp representation)
%%

%% ticker(Time,Event)

% A pass from ramires to remy
ticker(pass(1), 1). passer(1,ramires). recipient(1,remy).

