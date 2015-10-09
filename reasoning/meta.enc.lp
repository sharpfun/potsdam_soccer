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
counter(Time,Frame,N) :- ticker(_,_,Frame,Time),
                         Frame != none, 
                         N = #count { Src : ticker(_,Src,Frame,Time) }.
{ maxCounter(Time,Frame,N) : counter(Time,Frame,N) } = 1 :- counter(Time,_,_).
:- maxCounter(Time,Frame,N), counter(Time,Frame2,M), M > N.

%
timeline(Time,Frame) :-  ticker(_,_,Frame,Time), maxCounter(Time,Frame,N).
                            

% move attributes of the events we have in the timeline
timeline_attr(Time,Frame,FAttr,FVal) :- timeline(Time,Frame), 
                                        ticker(Id,Src,Frame,Time), 
                                        attribute(Id,_,Frame,FAttr,FVal).
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
                             
