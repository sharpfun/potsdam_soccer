%%
%% Definitions of actions that can occur
%% during a game
%%
%% event(Event,Effect).

%> depends on [score, team, player]

%> pass(PlayerA,PlayerB)
event(pass(PlayerA,PlayerB),ball(PlayerB))      :- player(PlayerA), player(PlayerB).
event(pass(PlayerA,PlayerB),neg(ball(PlayerA))) :- player(PlayerA), player(PlayerB).

%> goal(Player)
event(goal(Player,CScore),score(CScore+1,Team))    :- player(Player,Team), score(CScore).
event(goal(Player,CScore),neg(score(CScore,Team))) :- player(Player,Team), score(CScore).

%> score(Score,Team)
event(score(Score,Team),score(Score,Team))        :- team(Team), score(Score).
event(score(Score,Team),neg(score(Score-1),Team)) :- team(Team), score(Score).
