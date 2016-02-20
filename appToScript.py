def openFiles(fileName):
	global file
	file = open(fileName, "r")

def appendFile(readFile):
	appendedFile = open(readFile, "r")
	readOn = True
	while readOn:
		string = appendedFile.readline()
		if string[-1:] == "\n":
			allFile.write(string)
		else:
			allFile.write(string + "\n")
			readOn = False

def oneTeamoneMatch():
	global read 
	lines = []
	for i in range(21): #lines 1-21
		string = file.readline()
		if string[-1:] == "\n":
			lines.append(string[:-1])
		else:
			lines.append(string)
			read = False

	match = {} #dictionary; order might not be guaranteed (not the same when printed)

	for i in range(0, 2):
		match[lines[i].split(",")[0]] = [int(s) for s in lines[i].split() if s.isdigit()]
	for i in range(2, 8):
		match[lines[i].split(",")[0]] = lines[i].split(", ", 1)[1]
	for i in range(7, 17):
		match[lines[i].split(",")[0]] = [int(s) for s in lines[i].split() if s.isdigit()]
	for i in range(17, 21):
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
			if len(match["Difficulty to Cross " + defense]) != 0:
				match["Average Difficulty of " + defense] = (sumDefenses/float(len(match["Difficulty to Cross " + defense])))
			else:
				match["Average Difficulty of " + defense] = "N/A"
		sumDefenses = 0
	return match

def sortByTeam(allMatches):
	team = []
	teamNumber = allMatches[0]["Team Number"]
	i = 0
	while i < len(allMatches): #make sure index doesn't go out of bounds
		if allMatches[i]["Team Number"] == teamNumber:
			team.append(allMatches[i])
			del(allMatches[i])
		i += 1
	return team

def generateOneFile():
	global allFile
	allFile = open("oneFile.txt", "a") #append to end of file
	appendFile("r1.txt")
	appendFile("r2.txt")
	appendFile("r3.txt")
	appendFile("b1.txt")
	appendFile("b2.txt")
	readOn = True
	appendedFile = open("b3.txt", "r") #don't want \n at end of this
	while readOn:
		string = appendedFile.readline()
		if string[-1:] == "\n":
			allFile.write(string)
		else:
			allFile.write(string)
			readOn = False

def generateDict(fileName):
	global read
	openFiles(fileName)
	read = True
	matches = [] #append all 6 textfiles and read
	while read: #text file names: r1.txt, r2.txt, r3.txt, b1.txt, b2.txt, b3.txt
		matches.append(oneTeamoneMatch())
	newNumber = True
	teams = {}
	i = 0
	while len(matches) > 0:
		team = sortByTeam(matches)
		num = str(team[0]["Team Number"][0])
		teams[num] = team
		#return teams
	return teams

def generateTeamOverall(teams):
	teamOverall = {} #dictionary to be returned
	for key in teams: #key is teamnumber
		highGoalsMade = 0
		highGoalsTried = 0
		lowGoalsMade = 0
		lowGoalsTried = 0
		totalWins = 0
		defensesAvg = [0, 0, 0, 0, 0, 0, 0, 0, 0] #index in defensesAvg corresponds to index in defenses
		numAverages = [0, 0, 0, 0, 0, 0, 0, 0, 0] #number of times each average shows up
		teamOverall[key] = {} #dictionary in each key of teamOverall
		defenses = ["PC", "CF", "M", "RP", "SP", "DB", "RW", "RT", "LB"] #all possible defenses 
		for i in range(len(teams[key])): #go through each match for each team
			highGoalsMade += int(teams[key][i]["Probability of Scoring High Goals"][0])
			highGoalsTried += int(teams[key][i]["Probability of Scoring High Goals"][2])
			lowGoalsMade += int(teams[key][i]["Probability of Scoring Low Goals"][0])
			lowGoalsTried += int(teams[key][i]["Probability of Scoring Low Goals"][2])
			for j in range(len(defenses)):
				if teams[key][i].get("Average Difficulty of " + defenses[j]) != None:
					defensesAvg[j] += teams[key][i]["Average Difficulty of " + defenses[j]]
					numAverages[j] += 1
			if teams[key][i]["Result"] == "Win":
				totalWins += 1
		teamOverall[key]["Overall Probability of Scoring High Goals"] = str(highGoalsMade) + "/" + str(highGoalsTried)
		teamOverall[key]["Overall Probability of Scoring Low Goals"] = str(lowGoalsMade) + "/" + str(lowGoalsTried)
		teamOverall[key]["Proportion of Wins"] = str(totalWins) + "/" + str(len(teams[key]))
		for i in range(len(defensesAvg)):
			if numAverages[i] != 0:
				teamOverall[key]["Overall Average Difficulty of " + defenses[i]] = defensesAvg[i]/numAverages[i]
			else:
				teamOverall[key]["Overall Average Difficulty of " + defenses[i]] = "N/A"
	return teamOverall

def generateRankings(teamOverall):
	rankings = {}
	defenses = ["PC", "CF", "M", "RP", "SP", "DB", "RW", "RT", "LB"]
	teamNumbers = []
	for key in teamOverall:
		teamNumbers.append(key)
	for i in range(len(defenses)):
		rankings["Average Difficulty of " + defenses[i]] = {}
		defenseValues = []
		for j in range(len(teamNumbers)):
			defenseValues.append(teamOverall[teamNumbers[j]]["Overall Average Difficulty of " + defenses[i]])
		bubbleSort(defenseValues, teamNumbers) #sorts teamNumbers based on defenseValues
		for j in range(len(teamNumbers)):
			rankings["Average Difficulty of " + defenses[i]][teamNumbers[j]] = j + 1
	rankings["Overall Probability of Scoring High Goals"] = {}
	rankings["Overall Probability of Scoring Low Goals"] = {}
	rankings["Proportion of Wins"] = {}
	highGoals = []
	lowGoals = []
	wins = []
	for i in range(len(teamNumbers)): #must have a separate loop for each proportion because order of teamNumbers will be messed up
		proportionHigh = teamOverall[teamNumbers[i]]["Overall Probability of Scoring High Goals"]
		highGoals.append(float(proportionHigh[0])/int(proportionHigh[2]))		
	bubbleSort(highGoals, teamNumbers)
	for j in range(len(teamNumbers)):
		rankings["Overall Probability of Scoring High Goals"][teamNumbers[j]] = len(teamNumbers) - j
	for i in range(len(teamNumbers)):
		proportionLow = teamOverall[teamNumbers[i]]["Overall Probability of Scoring Low Goals"]
		lowGoals.append(float(proportionLow[0])/int(proportionLow[2]))
	bubbleSort(lowGoals, teamNumbers)
	for j in range(len(teamNumbers)):
		rankings["Overall Probability of Scoring Low Goals"][teamNumbers[j]] = len(teamNumbers) - j
	for i in range(len(teamNumbers)):
		proportionWin = teamOverall[teamNumbers[i]]["Proportion of Wins"]
		wins.append(float(proportionWin[0])/int(proportionWin[2]))
	bubbleSort(wins, teamNumbers)
	for j in range(len(teamNumbers)):
		rankings["Proportion of Wins"][teamNumbers[j]] = len(teamNumbers) - j
	return rankings

def generateTotals(teams, teamOverall):
	defenseTotals = {}
	for key in teams:
		defenseTotals[key] = {}
		numOfSuccesses = [0, 0, 0, 0, 0, 0, 0, 0, 0] #number of times each average shows up
		defenses = ["PC", "CF", "M", "RP", "SP", "DB", "RW", "RT", "LB"] #all possible defenses 
		for i in range(len(teams[key])): #go through each match for each team
			for j in range(len(defenses)):
				if teams[key][i].get("Difficulty to Cross " + defenses[j]) != None:
					for k in range(len(teams[key][i]["Difficulty to Cross " + defenses[j]])):
						if teams[key][i]["Difficulty to Cross " + defenses[j]][k] < 3:
							numOfSuccesses[j] += 1
		for i in range(len(defenses)):
			defenseTotals[key]["Total Successes to Cross " + defenses[i]] = numOfSuccesses[i]
		defenseTotals[key]["Total Successes of High Goals"] = int(teamOverall[key]["Overall Probability of Scoring High Goals"][0])
		defenseTotals[key]["Total Successes of Low Goals"] = int(teamOverall[key]["Overall Probability of Scoring Low Goals"][0])
	return defenseTotals

def generateTotalsRankings(defenseTotals):
	totalsRankings = {}
	defenses = ["PC", "CF", "M", "RP", "SP", "DB", "RW", "RT", "LB"]
	teamNumbers = []
	for key in defenseTotals:
		teamNumbers.append(key)
	for i in range(len(defenses)):
		totalsRankings["Total Successes to Cross " + defenses[i]] = {}
		defenseTotalValues = []
		for j in range(len(teamNumbers)):
			defenseTotalValues.append(defenseTotals[teamNumbers[j]]["Total Successes to Cross " + defenses[i]])
		bubbleSort(defenseTotalValues, teamNumbers) #sorts teamNumbers based on defenseValues
		for j in range(len(teamNumbers)):
			totalsRankings["Total Successes to Cross " + defenses[i]][teamNumbers[j]] = len(teamNumbers) - j
	totalsRankings["Total Successes of High Goals"] = {}
	totalsRankings["Total Successes of Low Goals"] = {}
	highGoals = []
	lowGoals = []
	for i in range(len(teamNumbers)): #must have a separate loop for each proportion because order of teamNumbers will be messed up
		highGoals.append(defenseTotals[teamNumbers[i]]["Total Successes of High Goals"])		
	bubbleSort(highGoals, teamNumbers)
	for j in range(len(teamNumbers)):
		totalsRankings["Total Successes of High Goals"][teamNumbers[j]] = len(teamNumbers) - j
	for i in range(len(teamNumbers)):
		lowGoals.append(defenseTotals[teamNumbers[i]]["Total Successes of Low Goals"])
	bubbleSort(lowGoals, teamNumbers)
	for j in range(len(teamNumbers)):
		totalsRankings["Total Successes of Low Goals"][teamNumbers[j]] = len(teamNumbers) - j
	return totalsRankings

def bubbleSort(values, numbers):
	for onePass in range(len(values) - 1, 0, -1):
		for i in range(0, onePass):
			if values[i + 1] == "N/A":
				a = values[i + 1]
				b = numbers[i + 1]
				values.append(a)
				numbers.append(b)
				del(values[i + 1])
				del(numbers[i + 1])
				i -= 1
			elif values[i + 1] < values[i]:
				tempValue = values[i]
				tempNumber = numbers[i]
				values[i] = values[i + 1]
				numbers[i] = numbers[i + 1]
				values[i + 1] = tempValue
				numbers[i + 1] = tempNumber


#thing = [3, 5, 6, 2, "N/A", 5, 6, 7, "N/A"]
#otherThing = [9, 2, 3, 2, 1, 5, 6, 7, 8]
#bubbleSort(thing, otherThing)
#print thing
#print otherThing
generateOneFile() #generates a file with all the appended text files!  NOTE: must delete the file generated to run the code again
allFile.close()
teams = generateDict("oneFile.txt")
overall = generateTeamOverall(teams)
#print overall
#generateRankings(overall)
totals = generateTotals(teams, overall)
print totals
print generateTotalsRankings(totals)