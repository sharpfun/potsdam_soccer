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

% what happens when an event occur:
holds(Effect,Time+1) :- ticker(Event,Time), event(Event,Effect). 

#show holds/2.
