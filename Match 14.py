Match Number, 14
Scouter Name, Kabir
Defenses on Field, PC, CF, M, RP, SP, DB, RW, RT #pick 4, low bar (LB) required
Spy Zone, True
Auto Reaches Defense, True
Auto Crosses Defense, PC #which defense they cross, multiple letters here mean multiple defenses crossed
Auto High Goal Shots, 1 1 0 #made made missed
Auto Low Goal Shots,  1 1 1 1 
#easy = 0, medium = 1, hard = 2, impossible/fail (can't do it) = 3; everytime they attempt generate new number
Difficulty to cross PC, 3.0, 3.0, 2.0, 3.0, 1.0
Difficulty to cross CF, 2.0, 1.0, 2.0, 2.0, 0.0
Difficulty to cross M, 0.0, 1.0, 0.0, 2.0, 1.0
Difficulty to cross RP, 3.0, 3.0, 2.0, 3.0, 1.0
Difficulty to cross SP, 3.0, 3.0, 2.0, 3.0, 1.0
Difficulty to cross DB, 3.0, 3.0, 2.0, 3.0, 1.0
Difficulty to cross RW, 3.0, 3.0, 2.0, 3.0, 1.0
Difficulty to cross RT, 3.0, 3.0, 2.0, 3.0, 1.0
Difficulty to cross LB, 3.0, 3.0, 2.0, 3.0, 1.0 #some of them (the ones they did) 
Play Defense, False
End Game, Hang, Challenge, Capture, Breach
Result Win, Lose

#NO LINE SPACES BETWEEN EACH BLOCK OF TEAM PER MATCH
#NO ENTERS ANYWHERE ELSE (additional notes must all be in one line)
TELE-OP 17 [] float difficulty to cross PC
18 [] float difficulty to cross CF, 19 [] float difficulty to cross M, 20 [] float difficulty to cross RP
21  [] float difficulty to cross SP, 22 [] float difficulty to cross DB, 23 [] float difficulty to cross RW
24 [] float difficulty to cross RT, 25 [] float difficulty to cross LB, 26 [] boolean high goal shots
27 [] boolean low goal shots, 28 [] boolean primarly did defense, 29 [] String comments,  30 [] boolean breach
31 [] boolean capture, 32 [] int win/loss/tie

#basil generates match-by-match profile for each team
#each match: all defenses on field, scouter name, start in spy zone, reach + crosses which defenses in auto, high + low goals (hit hit miss) array (one for each)
#for each defense list of numbers above, hit hit miss for high + goal goals, play defense for most of match boolean, hang/challenge/none, additional notes, breach/capture/win/lose/tie
#also include ratio of high goals shot made to high goals attempted (FRACTION), also for low goals, average of defense numbers (do nothing for null which is didn't attempt)

#put all into one dictionary in an array in a dictionary