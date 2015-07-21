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

% map informations from the one ticker to the main ticker which has the 
% highest priority (= 1)
% ticker(Id1,Frame1,Time) :- ticker(Id1,Src1,Frame1,T1), 
%                            Src1 := #min{ Src : ticker(_,Src,_,_) }.
timeline(Id,1,Frame,Time) :- ticker(Id,1,Frame,Time).

% if we find some new frame in some other ticker that is plus or minus 1 second,
% we insert the informations into the main ticker 
timeline(Id,Src,Frame,Time) :-  ticker(Id,Src,Frame,Time), Src > 1, 
                                timeline(Id,S1,F1,Time-100), Frame != F1,
                                timeline(Id,S2,F2,Time+100), Frame != F2.

% move attributes of the events we have in the timeline
attr(Id,Src,Frame,FAttr,FVal) :- timeline(Id,Src,Frame,Time),
                                 attribute(Id,Src,Frame,FAttr,FVal).

% extend attributes of an event that already occured,
% but missed some attributes - so we merge them 
attr(Id,Src,Frame,FAttr,FVal) :- timeline(Id,Src,Frame,Time),
                                 ticker(Id2,Src2,Frame,Time),
                                 attribute(Id2,Src2,Frame,FAttr,FVal). 


