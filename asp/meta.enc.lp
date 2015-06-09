%%
%% Mostly about state definitions
%%

%> depends on [time]

literal(L)|literal(neg(L)) :- fluent(L)

%
% definition of the initial state
%

holds(F,0) :- init(F).


%
% holds definition
%

% inertia
%holds(F,T+1) :- holds(F,T), %...

% what happens when an event occur:
holds(Effect,Time+1) :- ticker(Time,Event), event(Event,Effect). 

#show holds/2.
