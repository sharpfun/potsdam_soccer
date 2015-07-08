#const maxScore=20.
score(0..maxScore).
time(0).
team(arsenal, 1).
team(hull city, 2).
player(A,Red).
player(B,Red).
player(C,Red).
player(D,Red).
player(E,Red).
player(F,Red).
player(G,Red).
player(H,Red).
player(I,Red).
player(J,Red).
player(K,Red).
bench(L,Red).
bench(M,Red).
bench(N,Red).
bench(O,Red).
bench(P,Red).
bench(Q,Red).
bench(R,Red).
bench(S,Red).
bench(T,Red).
player(AA,Blue).
player(BB,Blue).
player(CC,Blue).
player(DD,Blue).
player(EE,Blue).
player(FF,Blue).
player(GG,Blue).
player(HH,Blue).
player(II,Blue).
player(JJ,Blue).
player(KK,Blue).
bench(LL,Blue).
bench(MM,Blue).
bench(NN,Blue).
bench(OO,Blue).
bench(PP,Blue).
bench(QQ,Blue).
bench(RR,Blue).
bench(SS,Blue).
bench(TT,Blue).
player(P) :- player(P,T).
team(T)   :- player(P,T).
bench(P)  :- bench(P,T).
fluent(score(S,T)) :- score(S), team(T).
fluent(ball(P))    :- player(P).
fluent(player(P))  :- player(P).
fluent(player(P))  :- bench(P).
fluent(bench(P))   :- player(P).
fluent(bench(P))   :- bench(P).
init(score(0,T))    :- team(T).
init(player(P))     :- player(P).
init(bench(P))      :- bench(P).
init(neg(ball(P)))  :- player(P).
ticker(252,0,,p4).
ticker(251,90'+5',,p4).
ticker(250,90'+4',,p4).
ticker(249,90'+4',,p4).
ticker(248,90.4,,p4).
ticker(247,90.4,,p4).
ticker(246,90'+3',pass,p4).
attribute(246,90'+3',pass,passer,david meyler).
ticker(245,90.3,,p4).
ticker(244,90.3,,p4).
ticker(243,90'+2',pass,p4).
attribute(243,90'+2',pass,passer,santiago cazorla).
ticker(242,90.2,,p4).
ticker(241,90.2,,p4).
ticker(240,90'+2',,p4).
ticker(239,90'+2',pass,p4).
attribute(239,90'+2',pass,passer,héctor bellerín).
ticker(238,90.2,,p4).
ticker(237,90.2,,p4).
ticker(236,90'+1',,p4).
ticker(235,90',pass,p4).
attribute(235,90',pass,passer,mesut Özil).
ticker(234,90.1,,p4).
ticker(233,90.1,,p4).
ticker(232,90,,p4).
ticker(231,90,,p4).
ticker(230,89',foul,p4).
attribute(230,89',foul,offender,francis coquelin).
ticker(229,89',,p4).
ticker(228,88',,p4).
ticker(227,88',,p4).
ticker(226,88',pass,p4).
attribute(226,88',pass,passer,tom huddlestone).
ticker(225,89,foul,p4).
attribute(225,89,foul,offender,francis coquelin).
ticker(224,89,,p4).
ticker(223,88,,p4).
ticker(222,88,,p4).
ticker(221,88,,p4).
ticker(220,88,,p4).
ticker(219,86',substitute,p4).
attribute(219,86',substitute,substituted_player,olivier giroud.).
attribute(219,86',substitute,substitute,theo walcott).
ticker(218,85',,p4).
ticker(217,86,,p4).
ticker(216,86,substitute,p4).
attribute(216,86,substitute,substituted_player,olivier giroud).
attribute(216,86,substitute,substitute,theo walcott).
ticker(215,85,,p4).
ticker(214,85,,p4).
ticker(213,85,,p4).
ticker(212,85,,p4).
ticker(211,85,,p4).
ticker(210,85,,p4).
ticker(209,84',,p4).
ticker(208,84',pass,p4).
attribute(208,84',pass,passer,olivier giroud).
ticker(207,84,,p4).
ticker(206,84,,p4).
ticker(205,83',,p4).
ticker(204,83',pass,p4).
attribute(204,83',pass,passer,alexis sánchez).
ticker(203,83,,p4).
ticker(202,83,,p4).
ticker(201,81',substitute,p4).
attribute(201,81',substitute,substituted_player,stephen quinn.).
attribute(201,81',substitute,substitute,nikica jelavic).
ticker(200,81',,p4).
ticker(199,75',pass,p4).
attribute(199,75',pass,passer,jack wilshere).
ticker(198,81,,p4).
ticker(197,81,substitute,p4).
attribute(197,81,substitute,substituted_player,stephen quinn).
attribute(197,81,substitute,substitute,nikica jelavic).
ticker(196,81,,p4).
ticker(195,81,,p4).
ticker(194,75,,p4).
ticker(193,75,,p4).
ticker(192,72',,p4).
ticker(191,72',pass,p4).
attribute(191,72',pass,passer,mesut Özil).
ticker(190,72,,p4).
ticker(189,72,,p4).
ticker(188,72,,p4).
ticker(187,72,,p4).
ticker(186,71',,p4).
ticker(185,71',,p4).
ticker(184,71,,p4).
ticker(183,71,,p4).
ticker(182,71,,p4).
ticker(181,71,,p4).
ticker(180,70',foul,p4).
attribute(180,70',foul,offender,michael dawson).
ticker(179,70',,p4).
ticker(178,68',substitute,p4).
attribute(178,68',substitute,substituted_player,aaron ramsey.).
attribute(178,68',substitute,substitute,jack wilshere).
ticker(177,65',substitute,p4).
attribute(177,65',substitute,substituted_player,sone aluko.).
attribute(177,65',substitute,substitute,andrew robertson).
ticker(176,64',,p4).
ticker(175,70,foul,p4).
attribute(175,70,foul,offender,michael dawson).
ticker(174,70,,p4).
ticker(173,68,,p4).
ticker(172,68,substitute,p4).
attribute(172,68,substitute,substituted_player,aaron ramsey).
attribute(172,68,substitute,substitute,jack wilshere).
ticker(171,65,,p4).
ticker(170,65,substitute,p4).
attribute(170,65,substitute,substituted_player,sone aluko).
attribute(170,65,substitute,substitute,andrew robertson).
ticker(169,64,,p4).
ticker(168,64,,p4).
ticker(167,62',,p4).
ticker(166,61',pass,p4).
attribute(166,61',pass,passer,olivier giroud).
ticker(165,62,,p4).
ticker(164,62,,p4).
ticker(163,61,,p4).
ticker(162,61,,p4).
ticker(161,60',pass,p4).
attribute(161,60',pass,passer,héctor bellerín).
ticker(160,60,,p4).
ticker(159,60,,p4).
ticker(158,58',foul,p4).
attribute(158,58',foul,offender,francis coquelin).
ticker(157,58',,p4).
ticker(156,56',,p4).
ticker(155,56',pass,p4).
attribute(155,56',pass,passer,ahmed elmohamady).
ticker(154,58,foul,p4).
attribute(154,58,foul,offender,francis coquelin).
ticker(153,58,,p4).
ticker(152,56,,p4).
ticker(151,56,,p4).
ticker(150,56,pass,p4).
attribute(150,56,pass,passer,ahmed elmohamady).
ticker(149,56,,p4).
ticker(148,56,,p4).
ticker(147,54',,p4).
ticker(146,49',,p4).
ticker(145,49',foul,p4).
attribute(145,49',foul,offender,sone aluko).
ticker(144,49',,p4).
ticker(143,49',foul,p4).
attribute(143,49',foul,offender,per mertesacker).
ticker(142,48',foul,p4).
attribute(142,48',foul,offender,david meyler).
ticker(141,48',,p4).
ticker(140,46',,p4).
ticker(139,46',pass,p4).
attribute(139,46',pass,passer,santiago cazorla).
ticker(138,54,,p4).
ticker(137,54,,p4).
ticker(136,49,,p4).
ticker(135,49,foul,p4).
attribute(135,49,foul,offender,sone aluko).
ticker(134,49,,p4).
ticker(133,49,foul,p4).
attribute(133,49,foul,offender,per mertesacker).
ticker(132,48,foul,p4).
attribute(132,48,foul,offender,david meyler).
ticker(131,48,,p4).
ticker(130,46,,p4).
ticker(129,46,,p4).
ticker(128,46,pass,p4).
attribute(128,46,pass,passer,david meyler).
ticker(127,46,,p4).
ticker(126,45',substitute,p4).
attribute(126,45',substitute,substituted_player,jake livermore.).
attribute(126,45',substitute,substitute,david meyler).
ticker(125,45'+3',,p4).
ticker(124,45'+1',,p4).
ticker(123,45,,p4).
ticker(122,45,substitute,p4).
attribute(122,45,substitute,substituted_player,jake livermore).
attribute(122,45,substitute,substitute,david meyler).
ticker(121,45.3,,p4).
ticker(120,45.1,,p4).
ticker(119,45.1,,p4).
ticker(118,45.1,pass,p4).
attribute(118,45.1,pass,passer,aaron ramsey).
ticker(117,45,,p4).
ticker(116,45,,p4).
ticker(115,44',,p4).
ticker(114,44',pass,p4).
attribute(114,44',pass,passer,santiago cazorla).
ticker(113,44,,p4).
ticker(112,44,,p4).
ticker(111,43',foul,p4).
attribute(111,43',foul,offender,dame n'doye).
ticker(110,43',,p4).
ticker(109,39',,p4).
ticker(108,39',foul,p4).
attribute(108,39',foul,offender,laurent koscielny).
ticker(107,39',,p4).
ticker(106,37',,p4).
ticker(105,37',,p4).
ticker(104,37',pass,p4).
attribute(104,37',pass,passer,alexis sánchez).
ticker(103,43,foul,p4).
attribute(103,43,foul,offender,dame n'doye).
ticker(102,43,,p4).
ticker(101,39,,p4).
ticker(100,39,,p4).
ticker(99,39,foul,p4).
attribute(99,39,foul,offender,laurent koscielny).
ticker(98,39,,p4).
ticker(97,37,,p4).
ticker(96,37,,p4).
ticker(95,37,,p4).
ticker(94,37,,p4).
ticker(93,35',,p4).
ticker(92,35',foul,p4).
attribute(92,35',foul,offender,olivier giroud).
ticker(91,33',,p4).
ticker(90,31',foul,p4).
attribute(90,31',foul,offender,mesut Özil).
ticker(89,31',,p4).
ticker(88,31',,p4).
ticker(87,35,,p4).
ticker(86,35,foul,p4).
attribute(86,35,foul,offender,olivier giroud).
ticker(85,33,,p4).
ticker(84,33,,p4).
ticker(83,33,pass,p4).
attribute(83,33,pass,passer,santiago cazorla).
ticker(82,31,foul,p4).
attribute(82,31,foul,offender,mesut Özil).
ticker(81,31,,p4).
ticker(80,31,,p4).
ticker(79,31,,p4).
ticker(78,31,,p4).
ticker(77,30',foul,p4).
attribute(77,30',foul,offender,dame n'doye).
ticker(76,30',,p4).
ticker(75,29',foul,p4).
attribute(75,29',foul,offender,santiago cazorla).
ticker(74,29',,p4).
ticker(73,28',,p4).
ticker(72,27',foul,p4).
attribute(72,27',foul,offender,jake livermore).
ticker(71,27',,p4).
ticker(70,26',,p4).
ticker(69,26',,p4).
ticker(68,30,foul,p4).
attribute(68,30,foul,offender,dame n'doye).
ticker(67,30,,p4).
ticker(66,29,foul,p4).
attribute(66,29,foul,offender,santiago cazorla).
ticker(65,29,,p4).
ticker(64,28,,p4).
ticker(63,28,,p4).
ticker(62,27,foul,p4).
attribute(62,27,foul,offender,jake livermore).
ticker(61,27,,p4).
ticker(60,26,,p4).
ticker(59,26,,p4).
ticker(58,26,,p4).
ticker(57,26,,p4).
ticker(56,26,,p4).
ticker(55,26,,p4).
ticker(54,26,,p4).
ticker(53,26,,p4).
ticker(52,23',foul,p4).
attribute(52,23',foul,offender,jake livermore).
ticker(51,23',,p4).
ticker(50,23',,p4).
ticker(49,23,foul,p4).
attribute(49,23,foul,offender,jake livermore).
ticker(48,23,,p4).
ticker(47,23,,p4).
ticker(46,23,,p4).
ticker(45,21',pass,p4).
attribute(45,21',pass,passer,robbie brady).
ticker(44,21,,p4).
ticker(43,21,,p4).
ticker(42,20',pass,p4).
attribute(42,20',pass,passer,jake livermore).
ticker(41,20,,p4).
ticker(40,20,,p4).
ticker(39,19',,p4).
ticker(38,19',foul,p4).
attribute(38,19',foul,offender,francis coquelin).
ticker(37,17',foul,p4).
attribute(37,17',foul,offender,per mertesacker).
ticker(36,17',,p4).
ticker(35,14',,p4).
ticker(34,14',,p4).
ticker(33,19,,p4).
ticker(32,19,foul,p4).
attribute(32,19,foul,offender,francis coquelin).
ticker(31,17,foul,p4).
attribute(31,17,foul,offender,per mertesacker).
ticker(30,17,,p4).
ticker(29,14,,p4).
ticker(28,14,,p4).
ticker(27,14,,p4).
ticker(26,14,,p4).
ticker(25,13',pass,p4).
attribute(25,13',pass,passer,alexis sánchez).
ticker(24,13,,p4).
ticker(23,13,,p4).
ticker(22,11',pass,p4).
attribute(22,11',pass,passer,mesut Özil).
ticker(21,11,,p4).
ticker(20,11,,p4).
ticker(19,9',,p4).
ticker(18,9',foul,p4).
attribute(18,9',foul,offender,jake livermore).
ticker(17,8',,p4).
ticker(16,8',,p4).
ticker(15,8',pass,p4).
attribute(15,8',pass,passer,aaron ramsey).
ticker(14,9,,p4).
ticker(13,9,foul,p4).
attribute(13,9,foul,offender,jake livermore).
ticker(12,8,,p4).
ticker(11,8,,p4).
ticker(10,8,,p4).
ticker(9,8,,p4).
ticker(8,7',foul,p4).
attribute(8,7',foul,offender,olivier giroud).
ticker(7,7',,p4).
ticker(6,3',,p4).
ticker(5,3',,p4).
ticker(4,3',,p4).
ticker(3,7,foul,p4).
attribute(3,7,foul,offender,olivier giroud).
ticker(2,7,,p4).
ticker(1,3,,p4).
ticker(0,3,,p4).
