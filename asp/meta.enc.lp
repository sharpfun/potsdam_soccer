%%
%% State Definitions.
%%
% auxiliary constructs
complement(F,neg(F))    :- fluent(F).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initial State.
holds(F,0)	:- init(F), complement(F,L).

% Law of Inertia
holds(F,T+1)	:- holds(F,T), complement(F,L), not caused(L,T+1), time(T).

% Law of Causal Effects
holds(F,T+1)    :- caused(F,T), complement(F,L).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% What happens if we have different tickers?
% - for now, it just maps all messages to the original ticker -
%
% Source is a number from 1 to len(sources)
% priority included -- the lower, the more confidence
%
ticker(Id,Frame,Time)                         :- ticker(Id,Src,Frame,Time).
attribute(Id,Frame,FrameAttribute,FrameValue) :- attribute(Id,Src,Frame,FrameAttribute,FrameValue).


