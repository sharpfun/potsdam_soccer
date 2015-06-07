%
% just for testing
% later this is done by the ticker framework dynamically
%

%% statics like 
player(oezil, arsenal).
player(ramsey, arsenal).
player(ramires, chelsea).
player(remy, chelsea).
% ...

% and for better usability
player(P) :- player(P,T).
team(T)   :- player(P,T).

%% init(Property).

init(score(0,T)) :- team(T).
init(


%%
%% Here come sample sentences (their asp representation)
%%

%% ticker(Time,Event)

% the score is 0 to 3
ticker(1, 
