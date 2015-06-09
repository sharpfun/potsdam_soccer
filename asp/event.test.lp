%
% just for testing
% later this is done by the ticker framework dynamically
%

#const maxScore=20.
score(0..maxScore).
time(0..10).

%% statics like 
player(oezil, arsenal).
player(ramsey, arsenal).
player(ramires, chelsea).
player(remy, chelsea).
% ...

% and for better usability
player(P) :- player(P,T).
team(T)   :- player(P,T).

%%
%% fluent definitions
%% what is a state described in the [soccer] world
%%
fluent(score(S,T)) :- score(S), team(T).
fluent(ball(P))    :- player(P).

%%
%% init(Property).
%%
init(score(0,T))  :- team(T).
init(neg(ball(P))) :- player(P).


%%
%% Here come sample sentences (their asp representation)
%%

%% ticker(Time,Event)

% A pass from ramires to remy
ticker(1, pass(ramires,remy)).

% the score is 0 to 3
ticker(2, score(0,arsenal)).
ticker(2, score(3,chelsea)).
