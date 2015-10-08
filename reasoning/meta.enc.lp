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
% Source is an identifier
% Each of the tickers has the same certainty
%
numberOfTickers(X) :- X = #count {Src : ticker(_,Src,_,_)}.

%
timeline(Id,Frame,Time) :-  ticker(Id,_,Frame,Time),
                            Frame != none, % thats not nice...
                            numberOfTickers(N),
                            N/2 <= {ticker(Id,Src,Frame,Time)}.

% move attributes of the events we have in the timeline
timeline_attr(Id,Frame,FAttr,FVal) :- timeline(Id,Frame,Time),
                             attribute(Id,_,Frame,FAttr,FVal).
