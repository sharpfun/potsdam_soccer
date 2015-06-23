plu(NAME) :- lu(_,NAME,1).
orders(1..N) :- N = #count { plu(NAME):lu(_,NAME,1) }.

1 { ordered_plu(NAME, N): plu(NAME) } 1 :- orders(N).

:- ordered_plu(NAME, N1), ordered_plu(NAME, N2), N1 != N2.

:- ordered_plu(NAME1, N1), ordered_plu(NAME2, N2), lu(SID, NAME1, 0), lu(SID, NAME2, 1), N1>N2.

#show ordered_plu/2.