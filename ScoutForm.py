from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4,landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
team = "649"

b = canvas.Canvas(team + " Scouting Form " + "Page 1",pagesize = letter)
c = canvas.Canvas(team + " Scouting Form " + "Page 2",pagesize = landscape(letter))
c2 = canvas.Canvas(team + " Scouting Form " + "Page 3",pagesize = landscape(letter))
c.setLineWidth(.3)
width , height = letter

"""Team Number : [] dict Game : Scouter name, name"""


teams ={
'649':[{'match':4,'scouter':'Bassil','totalPoints':230},{'match':9,'scouter':'Koh Koh','totalPoints':120},{'match':19,'scouter':'Neelus','totalPoints':420},{'match':30,'scouter':'Kabir','totalPoints':80}],
'846':[{'match':3,'scouter':'Bassil','totalPoints':230},{'match':9,'scouter':'Koh Koh','totalPoints':120},{'match':19,'scouter':'Neelus','totalPoints':420},{'match':30,'scouter':'Kabir','totalPoints':80}]
}

numberOfMatches = len(teams[team])
# print str(teams[team(0['match'])])

def drawTable():
	c.rect(height/50,width/50,height-height/25,width-width/25, fill=0)
def matchNumber():
	c.drawString(height/48,width-2*(width/45),"Match")
	c.line(height/15,width-width/50,height/15,width/50)
	i=1
	while i<=numberOfMatches:
		c.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
		c.drawString(height/48,width-(i+1)*(width/22),"test")
		i+=1
	c.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
def scouterName():
	c.drawString(height/14.5,width-2*(width/45),"Scouter")
	c.line(height/7.5,width-width/50,height/7.5,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/14.5,width-(i+1)*(width/22),"Koh Koh")
		i+=1
def totalPoints():
	c.drawString(height/7.35,width-2*(width/45),"Total Points")
	c.line(height/4.5,width-width/50,height/4.5,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/7.35,width-(i+1)*(width/22),"420")
		i+=1
def oppPoints():
	c.drawString(height/4.45,width-2*(width/45),"Opp Points")
	c.line(height/3.3,width-width/50,height/3.3,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/4.45,width-(i+1)*(width/22),"320")
		i+=1		
def myPoints():
	c.drawString(height/3.28,width-2*(width/45),"Own Points")
	c.line(height/2.6,width-width/50,height/2.6,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/3.28,width-(i+1)*(width/22),"140")
		i+=1		
def allianceCapture():
	c.drawString(height/2.58,width-2*(width/45),"Capture")
	c.line(height/2.25,width-width/50,height/2.25,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/2.58,width-(i+1)*(width/22),"False")
		i+=1	
def allianceTotalCapture():
	c.drawString(height/2.235,width-2*(width/45),"Breach")
	c.line(height/2,width-width/50,height/2,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/2.235,width-(i+1)*(width/22),"4")
		i+=1				
def lowBar():
	c.drawString(height/1.99,width-2*(width/45),"Low Bar")
	c.line(height/1.77,width-width/50,height/1.77,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.99,width-(i+1)*(width/22),"13212")
		i+=1				
def port():
	c.drawString(height/1.766,width-2*(width/45),"Port")
	c.line(height/1.62,width-width/50,height/1.62,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.768,width-(i+1)*(width/22),"13212")
		i+=1	
def cheval():
	c.drawString(height/1.618,width-2*(width/45),"Cheval")
	c.line(height/1.48,width-width/50,height/1.48,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.618,width-(i+1)*(width/22),"13212")
		i+=1	
def moat():
	c.drawString(height/1.47,width-2*(width/45),"Moat")
	c.line(height/1.37,width-width/50,height/1.37,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.47,width-(i+1)*(width/22),"13212")
		i+=1	
def ramparts():
	c.drawString(height/1.365,width-2*(width/45),"Ramp")
	c.line(height/1.28,width-width/50,height/1.28,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.365,width-(i+1)*(width/22),"13212")
		i+=1	
def draw():
	c.drawString(height/1.277,width-2*(width/45),"Bridge")
	c.line(height/1.2,width-width/50,height/1.2,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.277,width-(i+1)*(width/22),"13212")
		i+=1	
def sally():
	c.drawString(height/1.195,width-2*(width/45),"Sally")
	c.line(height/1.135,width-width/50,height/1.135,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.195,width-(i+1)*(width/22),"13212")
		i+=1	
def rock():
	c.drawString(height/1.133,width-2*(width/45),"Rock")
	c.line(height/1.075,width-width/50,height/1.08,width/50)
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.133,width-(i+1)*(width/22),"13212")
		i+=1	
def rough():
	c.drawString(height/1.076,width-2*(width/45),"Rough")
	i=1
	while i<=numberOfMatches:
		c.drawString(height/1.076,width-(i+1)*(width/22),"13212")
		i+=1	
def drawTable2():
	c2.rect(height/50,width/50,height-height/25,width-width/25, fill=0)
def spyZone():
	c2.drawString(height/48,width-2*(width/45),"Spy")
	c2.line(height/16,width-width/50,height/16,width/50)
	i=1
	while i<=numberOfMatches:
		c2.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
		c2.drawString(height/48,width-(i+1)*(width/22),"False")
		i+=1
		c2.line(height-height/50,width-i*(width/20),height/50,width-i*(width/20))
def autoHighShots():
	c2.drawString(height/15.5,width-2*(width/45),"Auto High")
	c2.line(height/7.5,width-width/50,height/7.5,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/15.5,width-(i+1)*(width/22),"0111")
		i+=1
def autoLowShots():
	c2.drawString(height/7.15,width-2*(width/45),"Auto Low")
	c2.line(height/4.8,width-width/50,height/4.8,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/7.15,width-(i+1)*(width/22),"0111")
		i+=1
def autoCross():
	c2.drawString(height/4.65,width-2*(width/45),"Auto Defense")
	c2.line(height/3.2,width-width/50,height/3.2,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/4.65,width-(i+1)*(width/22),"DB,LB,SP")
		i+=1
def teleopHighShots():
	c2.drawString(height/3.15,width-2*(width/45),"Teleop High")
	c2.line(height/2.4,width-width/50,height/2.4,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/3.15,width-(i+1)*(width/22),"0111001101")
		i+=1
def teleopLowShots():
	c2.drawString(height/2.36,width-2*(width/45),"Teleop Low")
	c2.line(height/1.95,width-width/50,height/1.95,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/2.36,width-(i+1)*(width/22),"0111001001")
		i+=1
def defense():
	c2.drawString(height/1.93,width-2*(width/45),"Defense")
	c2.line(height/1.73,width-width/50,height/1.73,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/1.93,width-(i+1)*(width/22),"False")
		i+=1
def hang():
	c2.drawString(height/1.71,width-2*(width/45),"Hang")
	c2.line(height/1.58,width-width/50,height/1.58,width/50)
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/1.71,width-(i+1)*(width/22),"False")
		i+=1
def notes():
	c2.drawString(height/1.57,width-2*(width/45),"Notes")
	i=1
	while i<=numberOfMatches:
		c2.drawString(height/1.57,width-(i+1)*(width/22),"Got caught on drawbridge. Fed balls to team")
		i+=1

notes()
hang()
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
allianceTotalCapture()
allianceCapture()
myPoints()
oppPoints()
totalPoints()
scouterName()
matchNumber()
drawTable()
b.showPage()
b.save()
c.showPage()
c.save()
c2.showPage()
c2.save()