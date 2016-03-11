from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4,landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
from appToScript import *

team = '649'
teams = generateDict("oneFile.txt")

overall = generateTeamOverall(teams)

totalMatches = len(teams[team])

c = canvas.Canvas(team + " Scouting Form " + "Notes.pdf",pagesize = letter)

width , height = letter
                                                          
def drawHeading():
	c.line(0,height-height/20,width,height-height/20)
	c.setFont("Helvetica",20)
	c.drawString(width/45,height-height/30,"Notes Page")
	c.drawString(width-width/10,height-height/30, team)


def drawNotes():
	c.setFont("Helvetica",12)
	i=1
	while i<=totalMatches:
		c.drawString(width/45,height-height/30-2*(i+1)*(height/40),"Match " + str(teams[team][i-1]["Match Number"][0]) + ":")
		if(len(teams[team][i-1]["Notes"])>75):
			c.drawString(width/9,height-height/30-2*(i+1)*(height/40),str(teams[team][i-1]["Notes"][0:75]))
			c.drawString(width/9,height-height/30-2*(i+1)*(height/40),str(teams[team][i-1]["Notes"][76:len(teams[team][i-1]["Notes"])]))
		else:
			c.drawString(width/9,height-height/30-2*(i+1)*(height/40),str(teams[team][i-1]["Notes"][0:len(teams[team][i-1]["Notes"])]))
		i+=1


drawNotes()
drawHeading()
c.showPage()
c.save()