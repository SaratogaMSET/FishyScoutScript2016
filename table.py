from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4,landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize

c = canvas.Canvas("table",pagesize = landscape(letter))
c.setLineWidth(.3)
width, height = letter
team = "649"

"""Team Number : [] dict Game : Scouter name, name"""


teams ={
'649':[{'match':4,'scouter':'Bassil','totalPoints':230},{'match':9,'scouter':'Koh Koh','totalPoints':120},{'match':19,'scouter':'Neelus','totalPoints':420},{'match':30,'scouter':'Kabir','totalPoints':80}]
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
	c.drawString(height/3,width-2*(width/45),"Own Points")
myPoints()
oppPoints()
totalPoints()
scouterName()
matchNumber()
drawTable()
c.showPage()
c.save()