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

match = '12'

red1 = '107'
red2 = '445'
red3 = '87'
blue1 = '990'
blue2 = '7'
blue3 = '649'
ourAlliance = 'Blue'

c = canvas.Canvas("Pre-Match Form" + ".pdf",pagesize = letter)

teams = generateDict("oneFile.txt")

overall = generateTeamOverall(teams)
rankings = generateRankings(overall)
totals = generateTotals(teams,overall)
totalsRankings = generateTotalsRankings(totals)


c.setLineWidth(.3)
width , height = letter

def topBox():
	c.setFont("Helvetica",20)
	c.drawString(width/45,height-height/30,"Match Number: " + match + " Pre-Match Form")
	c.line(0,height-height/20,width,height-height/20)
def tableLayout():
	c.line(width/4,height-height/20,width/4,0)
	c.line(width/2,height-height/20,width/2,0)
	c.line(width-width/4,height-height/20,width-width/4,0)
	c.line(0,height-height/13-9.2*(height/30),width,height-height/13-9.2*(height/30))
def ownAllianceBox():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13,"Own Alliance(" + ourAlliance + "):")
	c.line(0,height-height/13-height/90,width,height-height/13-height/90)
	c.drawString(width/80,height-height/13-height/30,"Average Match Score")
	c.drawString(width/80,height-height/13-2*(height/30),"High Goal Ratio")
	c.drawString(width/80,height-height/13-3*(height/30),"Low Goal Ratio")
	c.drawString(width/80,height-height/13-4*(height/30),"Portcullis||Cheval")
	c.drawString(width/80,height-height/13-5*(height/30),"Ramparts||Moat")
	c.drawString(width/80,height-height/13-6*(height/30),"Sallyport||Drawbridge")
	c.drawString(width/80,height-height/13-7*(height/30),"Rockwall||Roughterrain")
	c.drawString(width/60,height-height/13-8*(height/30),"Lowbar")
	c.drawString(width/60,height-height/13-9*(height/30),"Endgame")
def oppAllianceBox():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-15*(height/30),"Opposing Alliance:")
	c.line(0,height-height/13-15*(height/30)-height/90,width,height-height/13-15*(height/30)-height/90)
	c.drawString(width/80,height-height/13-16*(height/30),"Average Match Score")
	c.drawString(width/80,height-height/13-17*(height/30),"High Goal Ratio")
	c.drawString(width/80,height-height/13-18*(height/30),"Low Goal Ratio")
	c.line(0,height-height/13-18.2*(height/30),width,height-height/13-18.2*(height/30))
def oppTeamOne():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/4+width/45,height-height/13-15*(height/30), red1)
		c.drawString(width/4+width/45,height-height/13-16*(height/30),overall[red1]["Points"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-17*(height/30),overall[red1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-18*(height/30),overall[red1]["Overall Probability of Scoring Low Goals"].strip('[]'))
	else:
		c.drawString(width/4+width/45,height-height/13-15*(height/30), blue1)
		c.drawString(width/4+width/45,height-height/13-16*(height/30),overall[blue1]["Points"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-17*(height/30),overall[blue1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-18*(height/30),overall[blue1]["Overall Probability of Scoring Low Goals"].strip('[]'))
def oppTeamTwo():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/2+width/45,height-height/13-15*(height/30), red2)
		c.drawString(width/2+width/45,height-height/13-16*(height/30),overall[red2]["Points"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-17*(height/30),overall[red2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-18*(height/30),overall[red2]["Overall Probability of Scoring Low Goals"].strip('[]'))
	else:
		c.drawString(width/2+width/45,height-height/13-15*(height/30), blue2)
		c.drawString(width/2+width/45,height-height/13-16*(height/30),overall[blue2]["Points"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-17*(height/30),overall[blue2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-18*(height/30),overall[blue2]["Overall Probability of Scoring Low Goals"].strip('[]'))
def oppTeamThree():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width+width/45-width/4,height-height/13-15*(height/30), red3)
		c.drawString(width-width/4+width/45,height-height/13-16*(height/30),overall[red3]["Points"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-17*(height/30),overall[red3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-18*(height/30),overall[red3]["Overall Probability of Scoring Low Goals"].strip('[]'))
	else:
		c.drawString(width-width+width/45+width/4,height-height/13-15*(height/30), blue3)
		c.drawString(width-width/4+width/45,height-height/13-16*(height/30),overall[blue3]["Points"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-17*(height/30),overall[blue3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-18*(height/30),overall[blue3]["Overall Probability of Scoring Low Goals"].strip('[]'))
def autoBoxOwnTeamOne():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-10.75*(height/30),"Autonomous")
	c.drawString(width/4+width/45,height-height/13-10*(height/30),"DATA GOES HERES")
	c.line(0,height-height/13-12*(height/30),width,height-height/13-12*(height/30))
def autoBoxOwnTeamTwo():
	c.drawString(width/2+width/45,height-height/13-10*(height/30),"DATA GOES HERES")
def autoBoxOwnTeamThree():
	c.drawString(width-width/4+width/45,height-height/13-10*(height/30),"DATA GOES HERES")
def commentBox():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-13.25*(height/30),"Comments")
	c.line(0,height-height/13-14*(height/30),width,height-height/13-14*(height/30))
def commentBox2():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-22.25*(height/30),"Comments")
	c.line(0,height-height/13-23*(height/30),width,height-height/13-23*(height/30))
def autoBoxOpp():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-19.75*(height/30),"Autonomous")
	c.line(0,height-height/13-21*(height/30),width,height-height/13-21*(height/30))
def ownTeamOne():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/4+width/45,height-height/13, blue1)
		c.drawString(width/4+width/45,height-height/13-1*(height/30),overall[blue1]["Points"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-2*(height/30),overall[blue1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-3*(height/30),overall[blue1]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-4*(height/30),str(overall[blue1]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-5*(height/30),str(overall[blue1]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-6*(height/30),str(overall[blue1]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-7*(height/30),str(overall[blue1]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-8*(height/30),str(overall[blue1]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width/4+width/45,height-height/13, red1)
		c.drawString(width/4+width/45,height-height/13-1*(height/30),overall[red1]["Points"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-2*(height/30),overall[red1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-3*(height/30),overall[red1]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-4*(height/30),str(overall[red1]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-5*(height/30),str(overall[red1]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-6*(height/30),str(overall[red1]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-7*(height/30),str(overall[red1]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-8*(height/30),str(overall[red1]["Overall Average Difficulty of LB"]).strip('[]'))
def ownTeamTwo():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/2+width/45,height-height/13, blue2)
		c.drawString(width/2+width/45,height-height/13-1*(height/30),overall[blue2]["Points"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-2*(height/30),overall[blue2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-3*(height/30),overall[blue2]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-4*(height/30),str(overall[blue2]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-5*(height/30),str(overall[blue2]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-6*(height/30),str(overall[blue2]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-7*(height/30),str(overall[blue2]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-8*(height/30),str(overall[blue2]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width/2+width/45,height-height/13, red2)
		c.drawString(width/2+width/45,height-height/13-1*(height/30),overall[red2]["Points"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-2*(height/30),overall[red2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-3*(height/30),overall[red2]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-4*(height/30),str(overall[red2]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-5*(height/30),str(overall[red2]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-6*(height/30),str(overall[red2]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-7*(height/30),str(overall[red2]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-8*(height/30),str(overall[red2]["Overall Average Difficulty of LB"]).strip('[]'))
def ownTeamThree():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width+width/45-width/4,height-height/13, blue3)
		c.drawString(width-width/4+width/45,height-height/13-1*(height/30),overall[blue3]["Points"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-2*(height/30),overall[blue3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-3*(height/30),overall[blue3]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-4*(height/30),str(overall[blue3]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-5*(height/30),str(overall[blue3]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-6*(height/30),str(overall[blue3]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-7*(height/30),str(overall[blue3]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-8*(height/30),str(overall[blue3]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width+width/45+width/4,height-height/13, red3)
		c.drawString(width-width/4+width/45,height-height/13-1*(height/30),overall[red3]["Points"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-2*(height/30),overall[red3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-3*(height/30),overall[red3]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-4*(height/30),str(overall[red3]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-5*(height/30),str(overall[red3]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-6*(height/30),str(overall[red3]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-7*(height/30),str(overall[red3]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-8*(height/30),str(overall[red3]["Overall Average Difficulty of LB"]).strip('[]'))
def suggestionBox():
	# c.line(0,(height-(height/13-23*(height/30))),width,(height-(height/13-23*(height/30))))
	c.setFont("Helvetica",12)
	c.drawString(width/80,height-height/13-23.4*(height/30),"Opp Alliance Suggestion:")
	c.rect(26,5,100,100, stroke=1, fill=0)
	c.rect(width/4+26,5,100,100, stroke=1, fill=0)
	c.rect(width/2+26,5,100,100, stroke=1, fill=0)
	c.rect(width-width/4+26,5,100,100, stroke=1, fill=0)


suggestionBox()
commentBox()
autoBoxOwnTeamOne()
oppAllianceBox()
oppTeamOne()
oppTeamTwo()
commentBox2()
oppTeamThree()
autoBoxOpp()
autoBoxOwnTeamTwo()
autoBoxOwnTeamThree()
ownTeamOne()
ownTeamTwo()
ownTeamThree()
ownAllianceBox()
tableLayout()
topBox()
c.showPage()
c.save()