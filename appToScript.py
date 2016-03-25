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
	print matches
	newNumber = True
	teams = {}
	i = 0
	while len(matches) > 0:
		team = sortByTeam(matches)
		num = str(team[0]["Team Number"][0])
		teams[num] = team
		#return teams
	return teams

def getMatchesArray(teams, teamNumber):
	matches = []
	for i in range(len(teams[teamNumber])):
		matches.append(teams[teamNumber][i]["Match Number"][0])
	return matches

def generateTeamOverall(teams):
	teamOverall = {} #dictionary to be returned
	for key in teams: 
		highGoalsMade = 0
		highGoalsTried = 0
		lowGoalsMade = 0
		lowGoalsTried = 0
		totalWins = 0
		totalPoints = 0
		defensesAvg = [0, 0, 0, 0, 0, 0, 0, 0, 0] #index in defensesAvg corresponds to index in defenses
		numAverages = [0, 0, 0, 0, 0, 0, 0, 0, 0] #number of times each average shows up
		teamOverall[key] = {} #dictionary in each key of teamOverall
		defenses = ["PC", "CF", "M", "RP", "SP", "DB", "RW", "RT", "LB"] #all possible defenses 
		for i in range(len(teams[key])): #go through each match for each team
			#highGoalsMade += int(teams[key][i]["Probability of Scoring High Goals"][0])
			#highGoalsTried += int(teams[key][i]["Probability of Scoring High Goals"][2])
			#lowGoalsMade += int(teams[key][i]["Probability of Scoring Low Goals"][0])
			#lowGoalsTried += int(teams[key][i]["Probability of Scoring Low Goals"][2])
			highGoalsMade += int(teams[key][i]["Probability of Scoring High Goals"].split("/", 1)[0])
			highGoalsTried += int(teams[key][i]["Probability of Scoring High Goals"].split("/", 1)[1])
			lowGoalsMade += int(teams[key][i]["Probability of Scoring Low Goals"].split("/", 1)[0])
			lowGoalsTried += int(teams[key][i]["Probability of Scoring Low Goals"].split("/", 1)[1])
			for j in range(len(defenses)):
				if teams[key][i].get("Average Difficulty of " + defenses[j]) != None:
					if teams[key][i]["Average Difficulty of " + defenses[j]] != "N/A":
							defensesAvg[j] += teams[key][i]["Average Difficulty of " + defenses[j]]
							numAverages[j] += 1
			if teams[key][i]["Result"] == "Win":
				totalWins += 1
			elif teams[key][i]["Result"] == "Tie":
				totalWins += 0.5
			totalPoints += teams[key][i]["Total Points"][0]
		teamOverall[key]["Overall Probability of Scoring High Goals"] = str(highGoalsMade) + "/" + str(highGoalsTried)
		teamOverall[key]["Overall Probability of Scoring Low Goals"] = str(lowGoalsMade) + "/" + str(lowGoalsTried)
		teamOverall[key]["Proportion of Wins"] = str(totalWins) + "/" + str(len(teams[key]))
		teamOverall[key]["Overall Average Alliance Points"] = float(totalPoints)/len(teams[key])
		for i in range(len(defensesAvg)):
			if numAverages[i] != 0:
				teamOverall[key]["Overall Average Difficulty of " + defenses[i]] = round(defensesAvg[i]/numAverages[i], 2)
				#teamOverall[key]["Overall Average Difficulty of " + defenses[i]] = round(teamOverall[key]["Overall Average Difficulty of " + defenses[i]],-2)
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
	rankings["Average Alliance Match Points"] = {}
	points = []
	highGoals = []
	lowGoals = []
	wins = []
	points = []
	for i in range(len(teamNumbers)): #must have a separate loop for each proportion because order of teamNumbers will be messed up
		proportionHigh = teamOverall[teamNumbers[i]]["Overall Probability of Scoring High Goals"]
		if int(proportionHigh.split("/", 1)[1]) != 0: 
			highGoals.append(float(proportionHigh.split("/", 1)[0])/int(proportionHigh.split("/", 1)[1]))
		else:
			highGoals.append("N/A")		
	bubbleSort(highGoals, teamNumbers)
	for j in range(len(teamNumbers)):
		rankings["Overall Probability of Scoring High Goals"][teamNumbers[j]] = len(teamNumbers) - j
	for i in range(len(teamNumbers)):
		proportionLow = teamOverall[teamNumbers[i]]["Overall Probability of Scoring Low Goals"]
		if int(proportionLow.split("/", 1)[1]) != 0:
			lowGoals.append(float(proportionLow.split("/", 1)[0])/int(proportionLow.split("/", 1)[1]))
		else:
			lowGoals.append("N/A")
	bubbleSort(lowGoals, teamNumbers)
	for j in range(len(teamNumbers)):
		rankings["Overall Probability of Scoring Low Goals"][teamNumbers[j]] = len(teamNumbers) - j
	for i in range(len(teamNumbers)):
		proportionWin = teamOverall[teamNumbers[i]]["Proportion of Wins"]
		wins.append(float(proportionWin.split("/", 1)[0])/int(proportionWin.split("/", 1)[1]))
	bubbleSort(wins, teamNumbers)
	for j in range(len(teamNumbers)):
		rankings["Proportion of Wins"][teamNumbers[j]] = len(teamNumbers) - j
	for i in range(len(teamNumbers)):
		points.append(teamOverall[teamNumbers[i]]["Overall Average Alliance Points"])
	bubbleSort(points, teamNumbers)
	for j in range(len(teamNumbers)):
		rankings["Average Alliance Match Points"][teamNumbers[j]] = len(teamNumbers) - j
	return rankings

def generateTotals(teams, teamOverall):
	defenseTotals = {}
	for key in teams:
		defenseTotals[key] = {}
		totalPoints = 0
		numOfSuccesses = [0, 0, 0, 0, 0, 0, 0, 0, 0] #number of times each average shows up
		defenses = ["PC", "CF", "M", "RP", "SP", "DB", "RW", "RT", "LB"] #all possible defenses 
		for i in range(len(teams[key])): #go through each match for each team
			for j in range(len(defenses)):
				if teams[key][i].get("Difficulty to Cross " + defenses[j]) != None:
					for k in range(len(teams[key][i]["Difficulty to Cross " + defenses[j]])):
						if teams[key][i]["Difficulty to Cross " + defenses[j]][k] < 3:
							numOfSuccesses[j] += 1
			totalPoints += teams[key][i]["Total Points"][0]
		for i in range(len(defenses)):
			defenseTotals[key]["Total Successes to Cross " + defenses[i]] = numOfSuccesses[i]
		defenseTotals[key]["Total Successes of High Goals"] = int(teamOverall[key]["Overall Probability of Scoring High Goals"].split("/", 1)[0])
		defenseTotals[key]["Total Successes of Low Goals"] = int(teamOverall[key]["Overall Probability of Scoring Low Goals"].split("/", 1)[0])
		defenseTotals[key]["Total Alliance Points"] = totalPoints
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
	totalsRankings["Total Alliance Points"] = {}
	highGoals = []
	lowGoals = []
	points = []
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
	for i in range(len(teamNumbers)):
		points.append(defenseTotals[teamNumbers[i]]["Total Alliance Points"])
	bubbleSort(points, teamNumbers)
	for j in range(len(teamNumbers)):
		totalsRankings["Total Alliance Points"][teamNumbers[j]] = len(teamNumbers) - j
	return totalsRankings

def bubbleSort(values, numbers): #smallest to biggest
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
#returns the average of all 3 teams for each defense and ranks them from highest to lowest(worst -> best)

def compareDefenseCategory(team1, team2, team3, defense1, defense2, overall):
	defenseCategory = {}
	sumOfAverages1 = 0
	sumOfAverages2 = 0
	repeat = "Overall Average Difficulty of "
	numbers1 = [overall[team1][repeat + defense1], overall[team2][repeat + defense1], overall[team3][repeat + defense1]]
	numbers2 = [overall[team1][repeat + defense2], overall[team2][repeat + defense2], overall[team3][repeat + defense2]]
	numOfTimes1 = 0
	numOfTimes2 = 0
	noAttempt1 = []
	noAttempt2 = []
	teamNumbers = [team1, team2, team3]
	for i in range(len(numbers1)):
		if numbers1[i] != "N/A":
			sumOfAverages1 += numbers1[i]
			numOfTimes1 += 1
		elif numbers1[i] == "N/A":
			noAttempt1.append(teamNumbers[i])
		if numbers2[i] != "N/A":
			sumOfAverages2 += numbers2[i]
			numOfTimes2 += 1
		elif numbers2[i] == "N/A":
				noAttempt2.append(teamNumbers[i])
	if numOfTimes1 != 0:
		defenseCategory["Alliance Average of " + defense1] = str(sumOfAverages1/numOfTimes1)
	elif numOfTimes1 == 0:
		defenseCategory["Alliance Average of " + defense1] = "N/A"
	if numOfTimes2 != 0:
		defenseCategory["Alliance Average of " + defense2] = str(sumOfAverages2/numOfTimes2)
	elif numOfTimes2 == 0:
		defenseCategory["Alliance Average of " + defense2] = "N/A"
	if len(noAttempt1) != 0:
		defenseCategory["Alliance Average of " + defense1] += "; Team(s) " + str(noAttempt1) + " did not attempt."
	if len(noAttempt2) != 0:
		defenseCategory["Alliance Average of " + defense2] += "; Team(s) " + str(noAttempt2) + " did not attempt."
	defenseCategory['Did not attempt ' + defense1] = str(noAttempt1)
	defenseCategory['Did not attempt ' + defense2] = str(noAttempt2)
	return defenseCategory

#thing = [3, 5, 6, 2, "N/A", 5, 6, 7, "N/A"]
#otherThing = [9, 2, 3, 2, 1, 5, 6, 7, 8]
#bubbleSort(thing, otherThing)
#print thing
#print otherThing
generateOneFile() #generates a file with all the appended text files!  NOTE: must delete the file generated to run the code again
allFile.close()
teams = generateDict("oneFile.txt")
print teams
print getMatchesArray(teams, "649")
overall = generateTeamOverall(teams)

#print overall
print generateRankings(overall)
totals = generateTotals(teams, overall)
print totals
totalRankings = generateTotalsRankings(totals)
#keys = []
#for key in overall:
#	keys.append(key)
#print keys[0]
#print overall[keys[0]]
#print keys[1]
#print overall[keys[1]]
#print keys[2]
#print overall[keys[2]]
#teamNumbers = [keys[0], keys[1], keys[2]]
#defensesThree = compareDefenses3(overall[keys[0]], overall[keys[1]], overall[keys[2]], teamNumbers) 
# category = compareDefenseCategory("7", "990", "107", "PC", "LB", overall)