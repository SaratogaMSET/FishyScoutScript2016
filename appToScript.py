file = open('Match 14 R2.txt', 'r')
def oneTeamoneMatch():
	lines = []
	for i in range(20): #lines 1-20
		string = file.readline()
		if string[-1:] == "\n":
			lines.append(string[:-1])
		else:
			lines.append(string)
	match = { #dictionary; order might not be guaranteed (not the same when printed)

	}
	for i in range(0, 2):
		match[lines[i].split(",")[0]] = [int(s) for s in lines[i].split() if s.isdigit()]
	for i in range(2, 6):
		match[lines[i].split(",")[0]] = lines[i].split(", ", 1)[1]
	for i in range(6, 17):
		match[lines[i].split(",")[0]] = [int(s) for s in lines[i].split() if s.isdigit()]
	for i in range(16, 20):
		match[lines[i].split(",")[0]] = lines[i].split(", ", 1)[1]

	highGoalScores = 0
	for i in match["Auto High Goal Shots"]:
		if i == 1: highGoalScores += 1
	for i in match["Teleop High Goal Shots"]:
		if i == 1: highGoalScores += 1

	lowGoalScores = 0
	for i in match["Auto Low Goal Shots"]:
		if i == 1: lowGoalScores += 1
	for i in match["Teleop Low Goal Shots"]:
		if i == 1: lowGoalScores += 1

	match["Probability of Scoring High Goals"] = str(highGoalScores) + "/" + str(len(match["Auto High Goal Shots"]) + len(match["Teleop High Goal Shots"]))
	match["Probability of Scoring Low Goals"] = str(lowGoalScores) + "/" + str(len(match["Auto Low Goal Shots"]) + len(match["Teleop Low Goal Shots"]))

	defenses = ["PC", "CF", "M", "RP", "SP", "DB", "RW", "RT", "LB"]
	sumDefenses = 0
	for defense in defenses:
		if match.get("Difficulty to Cross " + defense) != None:
			for num in match["Difficulty to Cross " + defense]:
				sumDefenses += num
			match["Average Difficulty of " + defense] = (sumDefenses/float(len(match["Difficulty to Cross " + defense])))
		sumDefenses = 0

	return match

matches = []
matches.append(oneTeamoneMatch())
print matches
