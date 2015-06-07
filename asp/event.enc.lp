%%
%% Definitions of actions that can occur
%% during a game
%%
%% event(Event,Effect).


%> pass(PlayerA,PlayerB)
event(pass(PlayerA,PlayerB),ball(PlayerB)).
event(pass(PlayerA,PlayerB),neg(ball(PlayerA))).

%> goal(Player)
event(goal(Player),).

%> score(Score,Team)

