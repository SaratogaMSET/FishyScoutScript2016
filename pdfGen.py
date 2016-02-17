from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


teams = {

"""Team Number : [] dict Game : Scouter name, name



 [ 0 []String Scouter Name, AUTO 2[] boolean Spy Zone, 
3 [] boolean auto reaches defense, 4 [] boolean auto crosses PC, 5 [] boolean auto crosses CF, 
6 [] boolean auto crosses M, 7 [] boolean auto crosses RP, 8 [] boolean auto crosses SP, 
9 [] boolean auto crosses DB, 10 [] boolean auto crosses RW, 11 [] boolean auto crosses RT, 
12 [] boolean auto crosses RT, 13 [] boolean auto crosses LB, 14 [] boolean auto high goal shots 
15 [] boolean auto low goal shots, 16 [] int auto balls used TELE-OP 17 [] float difficulty to cross PC
18 [] float difficulty to cross CF, 19 [] float difficulty to cross M, 20 [] float difficulty to cross RP
21  [] float difficulty to cross SP, 22 [] float difficulty to cross DB, 23 [] float difficulty to cross RW
24 [] float difficulty to cross RT, 25 [] float difficulty to cross LB, 26 [] boolean high goal shots
27 [] boolean low goal shots, 28 [] boolean primarly did defense, 29 [] String comments,  30 [] boolean breach
31 [] boolean capture,`4te 32 [] int win/loss/tie"""

'8': { '1',  
'100': [][],
'254': [][],
'649': [][]
}

teams ={
'Team 8':{
 'Match 14':{'Scouter': "name",'Spy Zone': true, },

'100':{'b':30,'c':40}
'254' :{'14'}
}

def addTeam(self, teamNumber):
	teams.add(teamNumber)

def updateTeamProfile(self, teamNumber, newGame):
	for x in range(0, teams) :
		teams[teamNumber][newGame[0]] 


def printPrematchForm(self, r1, r2, r3, b1, b2, b3):
	doc = SimpleDocTemplate("PreMatch Form", pagesize=letter) 

	elements = []


