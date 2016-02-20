from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4,landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
from appToScript import *
from PIL import Image
import glob, os

team = '87'
teams = generateDict("oneFile.txt")

overall = generateTeamOverall(teams)
rankings = generateRankings(overall)
# picture = 'C:\Python27\dozer.jpg'
b = canvas.Canvas(team + " Scouting Form " + "Page 1.pdf",pagesize = letter)
c = canvas.Canvas(team + " Scouting Form " + "Page 2.pdf",pagesize = landscape(letter))
c2 = canvas.Canvas(team + " Scouting Form " + "Page 3.pdf",pagesize = landscape(letter))
c.setLineWidth(.3)
width , height = letter
"""Team Number : [] dict Game : Scouter name, name"""

# teams ={
# '649':[{'match':4,'scouter':'Bassil','totalPoints':230},{'match':9,'scouter':'Koh Koh','totalPoints':120},{'match':19,'scouter':'Neelus','totalPoints':420},{'match':30,'scouter':'Kabir','totalPoints':80}],
# '846':[{'match':3,'scouter':'Bassil','totalPoints':230},{'match':9,'scouter':'Koh Koh','totalPoints':120},{'match':19,'scouter':'Neelus','totalPoints':420},{'match':30,'scouter':'Kabir','totalPoints':80}]
# }

numberOfMatches = len(teams[team])
# print str(teams[team(0['match'])])
print str(rankings["Proportion of Wins"][team])
def prettyPicture():


	im = Image.open("C:\Python27\dozer.jpg")

	b.drawImage("C:\Python27\dozer.jpg",3*(width/45),height-height/2.2,width=width-6*(width/45),height=height/2.7)
def topBox():
	b.line(0,height-height/20,width,height-height/20)
	b.line(0,height/20,width,height/20)
# def picture():
# 	p = open(picture,'w')
# 	c.drawImage(p, 20, 20)

def bigData():
	# win ratio, total hgih shot ratio, low shto ratio, defense avg score lower is better, 
	b.setFont("Helvetica",20)
	b.drawString(width/45,height-height/25,"Team " + team + " Scouting Form")
	b.setFont("Helvetica",16)
	b.drawString(width/2.25,height/2,"Data!")
	b.drawString(width/45,(height-height/2)-13*(height/35),"Key:")
	b.setFont("Helvetica",12)
	b.drawString(width/45,(height-height/2)-14*(height/35),"All defensive rankings are between 0-3. 0 means nearly flawless, 1 means decent, 2 means struggled, 3 means impossible or nearly impossible, and N/A means not attempted.")
	b.drawString(width/2.25,(height-height/2)-(height/35),overall[team]['Proportion of Wins'])
	b.drawString(width/2.25,(height-height/2)-2*(height/35),overall[team]['Overall Probability of Scoring High Goals'])
	b.drawString(width/2.25,(height-height/2)-3*(height/35),str(overall[team]['Overall Average Difficulty of PC']))
	b.drawString(width/2.25,(height-height/2)-4*(height/35),str(overall[team]['Overall Average Difficulty of CF']))
	b.drawString(width/2.25,(height-height/2)-5*(height/35),str(overall[team]['Overall Average Difficulty of M']))
	b.drawString(width/2.25,(height-height/2)-6*(height/35),str(overall[team]['Overall Average Difficulty of RP']))
	b.drawString(width/2.25,(height-height/2)-7*(height/35),str(overall[team]['Overall Average Difficulty of SP']))
	b.drawString(width/2.25,(height-height/2)-8*(height/35),str(overall[team]['Overall Average Difficulty of DB']))
	b.drawString(width/2.25,(height-height/2)-9*(height/35),str(overall[team]['Overall Average Difficulty of RW']))
	b.drawString(width/2.25,(height-height/2)-10*(height/35),str(overall[team]['Overall Average Difficulty of RT']))
	b.drawString(width/2.25,(height-height/2)-11*(height/35),str(overall[team]['Overall Average Difficulty of LB']))
	b.drawString(width/2.25,(height-height/2)-12*(height/35),str(overall[team]['Overall Probability of Scoring Low Goals']))
def matchNumber():
	c.drawString(height/48,width-2*(width/45), 'Match')
	c.line(height/15,width-width/50,height/15,width/50)
	i=1
	while i<=numberOfMatches:
		c.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
		c.drawString(height/48,width-(i+1)*(width/22),str(teams[team][i-1]["Match Number"][0]))
		i+=1
	c.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
def drawTable():
	c.rect(height/50,width/50,height-height/25,width-width/25, fill=0)
def scouterName():
	c.drawString(height/14.5,width-2*(width/45),"Scouter")
	c.line(height/7.5,width-width/50,height/7.5,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/14.5,width-(i+1)*(width/22),str(teams[team][i-1]["Scouter Name"]))
		i+=1
def totalPoints():
	c.drawString(height/7.35,width-2*(width/45),"Total Points")
	c.line(height/4.5,width-width/50,height/4.5,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/7.35,width-(i+1)*(width/22),str(teams[team][i-1]["Total Points"][0]))
		i+=1
# def oppPoints():
# 	c.drawString(height/4.45,width-2*(width/45),"Opp Points")
# 	c.line(height/3.3,width-width/50,height/3.3,width/50)
# 	i=1
# 	while i<=numberOfMatches:
# 		c.drawString(height/4.45,width-(i+1)*(width/22),"320")
# 		i+=1		
# def myPoints():
# 	c.drawString(height/3.28,width-2*(width/45),"Own Points")
def defensesOnField():
	c.line(height/2.6,width-width/50,height/2.6,width/50)
	c.drawString(height/4.45,width-2*(width/45),"Defenses on Field")
	i=1
	while i<=numberOfMatches:
 		c.drawString(height/4.45,width-(i+1)*(width/22),str(teams[team][i-1]["Defenses on Field"]))
 		i+=1		
# 	i=1
# 	while i<=numberOfMatches:
# 		c.drawString(height/3.28,width-(i+1)*(width/22),"140")
# 		i+=1		
def endGame():
	c.drawString(height/2.58,width-2*(width/45),"End Game")
	c.line(height/2,width-width/50,height/2,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/2.58,width-(i+1)*(width/22),str(teams[team][i-1]["End Game"]))
		i+=1	
# def allianceTotalCapture():
# 	c.drawString(height/2.235,width-2*(width/45),"Breach")
# 	c.line(height/2,width-width/50,height/2,width/50)
# 	i=1
# 	while i<=numberOfMatches:
# 		c.drawString(height/2.235,width-(i+1)*(width/22),"4")
# 		i+=1				
def showRankings():
	global rankings
	b.setFont("Helvetica",16)
	b.drawString(width/45,height-height/2,"Rankings")
	b.drawString(width/1.6,height/2,"More Rankings")
	b.setFont("Helvetica",12)
	b.drawString(width/45,(height/2)-height/35,"Wins")
	b.drawString(width/3,height/2-(height/35),str(rankings["Proportion of Wins"][team]))
	b.drawString(width/45,(height-height/2)-2*(height/35),"High Goal Percentage:")
	b.drawString(width/3,(height-height/2)-2*(height/35),str(rankings["Overall Probability of Scoring High Goals"][team]))
	b.drawString(width/45,(height-height/2)-3*(height/35),"Portcullis Percentage:")
	b.drawString(width/3,(height-height/2)-3*(height/35),str(rankings["Average Difficulty of PC"][team]))
	b.drawString(width/45,(height-height/2)-4*(height/35),"Cheval de Frise Percentage:")
	b.drawString(width/3,(height-height/2)-4*(height/35),str(rankings["Average Difficulty of CF"][team]))
	b.drawString(width/45,(height-height/2)-5*(height/35),"Moat Percentage")
	b.drawString(width/3,(height-height/2)-5*(height/35),str(rankings["Average Difficulty of M"][team]))
	b.drawString(width/45,(height-height/2)-6*(height/35),"Ramparts Percentage:")
	b.drawString(width/3,(height-height/2)-6*(height/35),str(rankings["Average Difficulty of RP"][team]))
	b.drawString(width/45,(height-height/2)-7*(height/35),"Drawbridge Percentage:" )
	b.drawString(width/3,(height-height/2)-7*(height/35),str(rankings["Average Difficulty of SP"][team]))
	b.drawString(width/45,(height-height/2)-8*(height/35),"Sally Port Percentage:")
	b.drawString(width/3,(height-height/2)-8*(height/35),str(rankings["Average Difficulty of DB"][team]))
	b.drawString(width/45,(height-height/2)-9*(height/35),"Rock Wall Percentage:")
	b.drawString(width/3,(height-height/2)-9*(height/35),str(rankings["Average Difficulty of RW"][team]))
	b.drawString(width/45,(height-height/2)-10*(height/35),"Rough Terrain Percentage:")
	b.drawString(width/3,(height-height/2)-10*(height/35),str(rankings["Average Difficulty of RT"][team]))
	b.drawString(width/45,(height-height/2)-11*(height/35),"Low Bar Percentage:")
	b.drawString(width/3,(height-height/2)-11*(height/35),str(rankings["Average Difficulty of LB"][team]))
	b.drawString(width/45,(height-height/2)-12*(height/35),"Low Goal Percentage:")
	b.drawString(width/3,(height-height/2)-12*(height/35),str(rankings["Overall Probability of Scoring Low Goals"][team]))
	b.drawString(width/1.6,(height-height/2)-(height/35),"Overall")
	b.drawString(width/1.1,(height-height/2)-height/35,"2")
	b.drawString(width/1.6,(height-height/2)-2*(height/35),"High Goal Total:")
	b.drawString(width/1.1,(height-height/2)-2*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-3*(height/35),"Portcullis Total:")
	b.drawString(width/1.1,(height-height/2)-3*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-4*(height/35),"Cheval de Frise Total:")
	b.drawString(width/1.1,(height-height/2)-4*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-5*(height/35),"Moat Total:" )
	b.drawString(width/1.1,(height-height/2)-5*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-6*(height/35),"Ramparts Total:")
	b.drawString(width/1.1,(height-height/2)-6*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-7*(height/35),"Drawbridge Total:")
	b.drawString(width/1.1,(height-height/2)-7*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-8*(height/35),"Sally Port Total:")
	b.drawString(width/1.1,(height-height/2)-8*(height/35),"16")
 	b.drawString(width/1.6,(height-height/2)-9*(height/35),"Rock Wall Total:")
 	b.drawString(width/1.1,(height-height/2)-9*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-10*(height/35),"Rough Terrain Total:")
	b.drawString(width/1.1,(height-height/2)-10*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-11*(height/35),"Low Bar Total:")
	b.drawString(width/1.1,(height-height/2)-11*(height/35),"16")
	b.drawString(width/1.6,(height-height/2)-12*(height/35),"Low Goal Total:")
	b.drawString(width/1.1,(height-height/2)-12*(height/35),"16")
def lowBar():
	c.drawString(height/1.99,width-2*(width/45),"Low Bar")
	c.line(height/1.77,width-width/50,height/1.77,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.99,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross LB"]).strip('[]'))		
		i+=1				
def port():
	c.drawString(height/1.766,width-2*(width/45),"Port")
	c.line(height/1.62,width-width/50,height/1.62,width/50)
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross PC") == None:
			c.drawString(height/1.768,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.768,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross PC"]).strip('[]'))
		i+=1	
def cheval():
	c.drawString(height/1.618,width-2*(width/45),"Cheval")
	c.line(height/1.48,width-width/50,height/1.48,width/50)
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross CF") == None:
			c.drawString(height/1.618,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.618,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross CF"]).strip('[]'))
		i+=1	
def moat():
	c.drawString(height/1.47,width-2*(width/45),"Moat")
	c.line(height/1.37,width-width/50,height/1.37,width/50)
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross M") == None:
			c.drawString(height/1.47,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.47,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross M"]).strip('[]'))
		i+=1	
def ramparts():
	c.drawString(height/1.365,width-2*(width/45),"Ramp")
	c.line(height/1.28,width-width/50,height/1.28,width/50)
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross RP") == None:
			c.drawString(height/1.365,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.365,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross RP"]).strip('[]'))
		i+=1	
def draw():
	c.drawString(height/1.277,width-2*(width/45),"Bridge")
	c.line(height/1.2,width-width/50,height/1.2,width/50)
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross DB") == None:
			c.drawString(height/1.277,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.277,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross DB"]).strip('[]'))
		i+=1	
def sally():
	c.drawString(height/1.195,width-2*(width/45),"Sally")
	c.line(height/1.135,width-width/50,height/1.135,width/50)
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross SP") == None:
			c.drawString(height/1.195,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.195,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross SP"]).strip('[]'))
		i+=1	
def rock():
	c.drawString(height/1.133,width-2*(width/45),"Rock")
	c.line(height/1.075,width-width/50,height/1.08,width/50)
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross RW") == None:
			c.drawString(height/1.133,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.133,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross RW"]).strip('[]'))
		i+=1	
def rough():
	c.drawString(height/1.074,width-2*(width/45),"Rough")
	i=1
	while i<=numberOfMatches:
		if teams[team][i-1].get("Difficulty to Cross RT") == None:
			c.drawString(height/1.074,width-(i+1)*(width/22),"N/A")
		else:
			c.drawString(height/1.074,width-(i+1)*(width/22),str(teams[team][i-1]["Difficulty to Cross RT"]).strip('[]'))
		i+=1	
def drawTable2():
	c2.rect(height/50,width/50,height-height/25,width-width/25, fill=0)
def spyZone():
	c2.drawString(height/48,width-2*(width/45),"Spy")
	c2.line(height/16,width-width/50,height/16,width/50)
	i=1
	while i<=numberOfMatches:
		c2.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
		c2.drawString(height/48,width-(i+1)*(width/22),str(teams[team][i-1]["Spy Zone"]))
		i+=1
		c2.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
def autoHighShots():
	c2.drawString(height/15.5,width-2*(width/45),"Auto High")
	c2.line(height/7.5,width-width/50,height/7.5,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/15.5,width-(i+1)*(width/22),str(teams[team][i-1]["Auto High Goal Shots"]).strip('[]'))
		i+=1
def autoLowShots():
	c2.drawString(height/7.15,width-2*(width/45),"Auto Low")
	c2.line(height/4.8,width-width/50,height/4.8,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/7.15,width-(i+1)*(width/22),str(teams[team][i-1]["Auto Low Goal Shots"]).strip('[]'))
		i+=1
def autoCross():
	c2.drawString(height/4.65,width-2*(width/45),"Auto Defense")
	c2.line(height/3.2,width-width/50,height/3.2,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/4.65,width-(i+1)*(width/22),str(teams[team][i-1]["Auto Crosses Defense"]))
		i+=1
def teleopHighShots():
	c2.drawString(height/3.15,width-2*(width/45),"Teleop High")
	c2.line(height/2.4,width-width/50,height/2.4,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/3.15,width-(i+1)*(width/22),str(teams[team][i-1]["Teleop High Goal Shots"]))
		i+=1
def teleopLowShots():
	c2.drawString(height/2.36,width-2*(width/45),"Teleop Low")
	c2.line(height/1.95,width-width/50,height/1.95,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/2.36,width-(i+1)*(width/22),str(teams[team][i-1]["Teleop Low Goal Shots"]))
		i+=1
def defense():
	c2.drawString(height/1.93,width-2*(width/45),"Defense")
	c2.line(height/1.73,width-width/50,height/1.73,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/1.93,width-(i+1)*(width/22),str(teams[team][i-1]["Play Defense"]))
		i+=1
# def hang():
# 	c2.drawString(height/1.71,width-2*(width/45),"Hang")
# 	c2.line(height/1.58,width-width/50,height/1.58,width/50)
# 	i=1
# 	while i<=numberOfMatches:
# 		c2.drawString(height/1.71,width-(i+1)*(width/22),"False")
# 		i+=1
def notes():
	c2.drawString(height/1.725,width-2*(width/45),"Notes")
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/1.725,width-(i+1)*(width/22),str(teams[team][i-1]["Notes"]))
		i+=1

bigData()
notes()
# hang()
topBox()
defense()
teleopLowShots()
teleopHighShots()
autoCross()
autoLowShots()
drawTable2()
spyZone()
autoHighShots()
lowBar()
port()
cheval()
moat()
ramparts()
draw()
sally()
rock()
rough()
#allianceTotalCapture()
#allianceCapture()
# myPoints()
# oppPoints()
endGame()
showRankings()
prettyPicture()
# picture()
totalPoints()
scouterName()
matchNumber()
drawTable()
defensesOnField()
b.showPage()
b.save()
c.showPage()
c.save()
c2.showPage()
c2.save()