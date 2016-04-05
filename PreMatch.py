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

match = '11'

red1 = '649'
red2 = '1678'
red3 = '971'
blue1 = '846'
blue2 = "254"
blue3 = '368'
ourAlliance = 'Red'


c = canvas.Canvas("Pre-Match Form " + match + ".pdf", pagesize = letter)

teams = generateDict("oneFile.txt")

overall = generateTeamOverall(teams)
auto = generateAutoDict(teams)
rankings = generateRankings(overall, auto)
totals = generateTotals(teams,overall)

# rankings = generateRankings(overall,auto)
totalsRankings = generateTotalsRankings(totals)

width , height = letter

def topBox():
	c.setFont("Helvetica",20)
	c.drawString(width/45,height-height/30,"Pre-Match Form")
	c.drawString(width-width/10,height-height/30, match)
	c.line(0,height-height/20,width,height-height/20)
def tableLayout():
	c.line(width/4,height-height/20,width/4,0)
	c.line(width/2,height-height/20,width/2,0)
	c.line(width-width/4,height-height/20,width-width/4,0)
	# c.line(0,height-height/13-7.2*(height/30),width,height-height/13-7.2*(height/30))
def ownAllianceBox():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13,"Own Alliance(" + ourAlliance + "):")
	c.line(0,height-height/13-height/90,width,height-height/13-height/90)
	c.drawString(width/80,height-height/13-height/30,"Average Match Score")
	c.drawString(width/80,height-height/13-1.75*(height/30),"High Goal Ratio")
	c.drawString(width/80,height-height/13-2.5*(height/30),"Low Goal Ratio")
	c.drawString(width/80,height-height/13-3.25*(height/30),"PC||CF")
	c.drawString(width/80,height-height/13-4*(height/30),"RP||M")
	c.drawString(width/80,height-height/13-4.75*(height/30),"SP||DB")
	c.drawString(width/80,height-height/13-5.5*(height/30),"RW||RT")
	c.drawString(width/80,height-height/13-6.25*(height/30),"LB")
	c.drawString(width/80,height-height/13-7*(height/30),"Endgame")
def oppAllianceBox():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-10.75*(height/30),"Opposing Alliance:")
	c.line(0,height-height/13-10.75*(height/30)-height/90,width,height-height/13-10.75*(height/30)-height/90)
	c.drawString(width/80,height-height/13-12*(height/30),"Average Match Score")
	c.drawString(width/80,height-height/13-12.75*(height/30),"High Goal Ratio")
	c.drawString(width/80,height-height/13-13.5*(height/30),"Low Goal Ratio")
	c.drawString(width/80,height-height/13-14.25*(height/30),"PC||CF")
	c.drawString(width/80,height-height/13-15*(height/30),"RP||M")
	c.drawString(width/80,height-height/13-15.75*(height/30),"SP||DB")
	c.drawString(width/80,height-height/13-16.5*(height/30),"RW||RT")
	c.drawString(width/80,height-height/13-17.25*(height/30),"LB")
	# c.drawString(width/80,height-height/13-20.25*(height/30),"Endgame")
	# c.line(0,height-height/13-16*(height/30),width,height-height/13-16*(height/30))
def oppTeamOne():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/4+width/45,height-height/13-10.75*(height/30), red1)
		c.drawString(width/4+width/45,height-height/13-12*(height/30),str(totals[red1]["Total Alliance Points"]))
		c.drawString(width/4+width/45,height-height/13-12.75*(height/30),overall[red1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-13.5*(height/30),overall[red1]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-14.25*(height/30),str(overall[red1]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-15*(height/30),str(overall[red1]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-15.75*(height/30),str(overall[red1]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-16.5*(height/30),str(overall[red1]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-17.25*(height/30),str(overall[red1]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width/4+width/45,height-height/13-10.75*(height/30), blue1)
		c.drawString(width/4+width/45,height-height/13-12*(height/30),str(totals[blue1]["Total Alliance Points"]))
		c.drawString(width/4+width/45,height-height/13-12.75*(height/30),overall[blue1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-13.5*(height/30),overall[blue1]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-14.25*(height/30),str(overall[blue1]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-15*(height/30),str(overall[blue1]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-15.75*(height/30),str(overall[blue1]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-16.5*(height/30),str(overall[blue1]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-17.25*(height/30),str(overall[blue1]["Overall Average Difficulty of LB"]).strip('[]'))
def oppTeamTwo():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/2+width/45,height-height/13-10.75*(height/30), red2)
		c.drawString(width/2+width/45,height-height/13-12*(height/30),str(totals[red2]["Total Alliance Points"]))
		c.drawString(width/2+width/45,height-height/13-12.75*(height/30),overall[red2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-13.5*(height/30),overall[red2]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-14.25*(height/30),str(overall[red2]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-15*(height/30),str(overall[red2]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-15.75*(height/30),str(overall[red2]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-16.5*(height/30),str(overall[red2]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-17.25*(height/30),str(overall[red2]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width/2+width/45,height-height/13-10.75*(height/30), blue2)
		c.drawString(width/2+width/45,height-height/13-12*(height/30),str(totals[blue2]["Total Alliance Points"]))
		c.drawString(width/2+width/45,height-height/13-12.75*(height/30),overall[blue2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-13.5*(height/30),overall[blue2]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-14.25*(height/30),str(overall[blue2]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-15*(height/30),str(overall[blue2]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-15.75*(height/30),str(overall[blue2]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-16.5*(height/30),str(overall[blue2]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-17.25*(height/30),str(overall[blue2]["Overall Average Difficulty of LB"]).strip('[]'))
def oppTeamThree():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width+width/45-width/4,height-height/13-10.75*(height/30), red3)
		c.drawString(width-width/4+width/45,height-height/13-12*(height/30),str(totals[red3]["Total Alliance Points"]))
		c.drawString(width-width/4+width/45,height-height/13-12.75*(height/30),overall[red3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-13.5*(height/30),overall[red3]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/4+width/45-width/4,height-height/13-14.25*(height/30),str(overall[red2]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/4+width/45-width/4,height-height/13-15*(height/30),str(overall[red3]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/4+width/45-width/4,height-height/13-15.75*(height/30),str(overall[red3]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/4+width/45-width/4,height-height/13-16.5*(height/30),str(overall[red3]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/4+width/45-width/4,height-height/13-17.25*(height/30),str(overall[red3]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width+width/45-width/4,height-height/13-10.75*(height/30), blue3)
		c.drawString(width-width/4+width/45,height-height/13-12*(height/30),str(totals[blue3]["Total Alliance Points"]))
		c.drawString(width-width/4+width/45,height-height/13-12.75*(height/30),overall[blue3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-13.5*(height/30),overall[blue3]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-14.25*(height/30),str(overall[blue3]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-15*(height/30),str(overall[blue3]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-15.75*(height/30),str(overall[blue3]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-16.5*(height/30),str(overall[blue3]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-17.25*(height/30),str(overall[blue3]["Overall Average Difficulty of LB"]).strip('[]'))
def autoBoxOwnTeamOne():
	c.setFont("Helvetica",14)
	# c.drawString(width/80,height-height/13-8.75*(height/30),"Autonomous")
	# b.drawString(width/2.25,(height-height/2)-13*(height/35),str(auto[team]["Probability of Scoring Auto High Goals"]))
	# b.drawString(width/2.25,(height-height/2)-14*(height/35),str(auto[team]["Probability of Scoring Auto Low Goals"]))
	# b.drawString(width/2.25,(height-height/2)-15*(height/35),str(auto[team]["Ratio of Crossing a Defense in Auto"]))

	c.drawString(width/80,(height-height/13)-7.75*(height/30),"Auto High Goals")
	c.drawString(width/80,(height-height/13)-8.5*(height/30),"Auto Low Goals")
	c.drawString(width/80,(height-height/13)-9.25*(height/30),"Auto Cross")
	if(ourAlliance == 'Blue'):
		c.drawString(width/45+width/4,height-height/13-7.75*(height/30),str(auto[blue1]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-7.75*(height/30),str(auto[blue2]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-7.75*(height/30),str(auto[blue3]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-8.5*(height/30),str(auto[blue1]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-8.5*(height/30),str(auto[blue2]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-8.5*(height/30),str(auto[blue3]["Probability of Scoring Low Goals"]).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-9.25*(height/30),str(auto[blue1]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-9.25*(height/30),str(auto[blue2]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-9.25*(height/30),str(auto[blue3]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
	else:
		c.drawString(width/45+width/4,height-height/13-7.75*(height/30),str(auto[red1]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-7.75*(height/30),str(auto[red2]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-7.75*(height/30),str(auto[red3]['Probability of Scoring Auto High Goals']).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-8.5*(height/30),str(auto[red1]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-8.5*(height/30),str(auto[red2]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-8.5*(height/30),str(auto[red3]['Probability of Scoring Auto Low Goals']).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-9.25*(height/30),str(auto[red1]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-9.25*(height/30),str(auto[red2]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-9.25*(height/30),str(auto[red3]["Ratio of Crossing a Defense in Auto"]).strip('[]'))

	c.line(0,height-height/13-10*(height/30),width,height-height/13-10*(height/30))
	# c.drawString(width/4+width/45,height-height/13-10*(height/30),"DATA GOES HERES")
	
# def autoBoxOwnTeamTwo():
# 	# c.drawString(width/2+width/45,height-height/13-10*(height/30),"DATA GOES HERES")
# def autoBoxOwnTeamThree():
	# c.drawString(width-width/4+width/45,height-height/13-10*(height/30),"DATA GOES HERES")
def commentBox():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-11.5*(height/30),"Comments")
	c.line(0,height-height/13-12.5*(height/30),width,height-height/13-12.5*(height/30))
def commentBox2():
	c.setFont("Helvetica",14)
	c.drawString(width/80,height-height/13-21.5*(height/30),"Comments")
	c.line(0,height-height/13-23*(height/30),width,height-height/13-23*(height/30))
def autoBoxOpp():
	c.setFont("Helvetica",14)
	c.drawString(width/80,(height-height/13)-18*(height/30),"Auto High Goals")
	c.drawString(width/80,(height-height/13)-18.75*(height/30),"Auto Low Goals")
	c.drawString(width/80,(height-height/13)-19.5*(height/30),"Auto Cross")
	if(ourAlliance == 'Red'):
		c.drawString(width/45+width/4,height-height/13-18*(height/30),str(auto[blue1]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-18*(height/30),str(auto[blue2]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-18*(height/30),str(auto[blue3]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-18.75*(height/30),str(auto[blue1]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-18.75*(height/30),str(auto[blue2]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-18.75*(height/30),str(auto[blue3]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-19.5*(height/30),str(auto[blue1]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-19.5*(height/30),str(auto[blue2]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-19.5*(height/30),str(auto[blue3]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
	else:
		c.drawString(width/45+width/4,height-height/13-18*(height/30),str(auto[red1]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-18*(height/30),str(auto[red2]["Probability of Scoring Auto High Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-18*(height/30),str(auto[red3]['Probability of Scoring Auto High Goals']).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-18.75*(height/30),str(auto[red1]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-18.75*(height/30),str(auto[red2]["Probability of Scoring Auto Low Goals"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-18.75*(height/30),str(auto[red3]['Probability of Scoring Auto Low Goals']).strip('[]'))
		c.drawString(width/45+width/4,height-height/13-19.5*(height/30),str(auto[red1]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width/45+width/2,height-height/13-19.5*(height/30),str(auto[red2]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
		c.drawString(width+width/45-width/4,height-height/13-19.5*(height/30),str(auto[red3]["Ratio of Crossing a Defense in Auto"]).strip('[]'))
	# c.drawString(width/80,height-height/13-19.75*(height/30),"Autonomous")
	c.line(0,height-height/13-19.75*(height/30),width,height-height/13-19.75*(height/30))
def ownTeamOne():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/4+width/45,height-height/13, blue1)
		c.drawString(width/4+width/45,height-height/13-1*(height/30),str(totals[blue1]["Total Alliance Points"]))
		c.drawString(width/4+width/45,height-height/13-1.75*(height/30),overall[blue1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-2.5*(height/30),overall[blue1]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-3.25*(height/30),str(overall[blue1]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-4*(height/30),str(overall[blue1]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-4.75*(height/30),str(overall[blue1]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-5.5*(height/30),str(overall[blue1]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-6.25*(height/30),str(overall[blue1]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width/4+width/45,height-height/13, red1)
		c.drawString(width/4+width/45,height-height/13-1*(height/30),str(totals[red1]["Total Alliance Points"]))
		c.drawString(width/4+width/45,height-height/13-1.75*(height/30),overall[red1]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-2.5*(height/30),overall[red1]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/4+width/45,height-height/13-3.25*(height/30),str(overall[red1]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-4*(height/30),str(overall[red1]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-4.75*(height/30),str(overall[red1]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-5.5*(height/30),str(overall[red1]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[red1]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/4+width/45,height-height/13-6.25*(height/30),str(overall[red1]["Overall Average Difficulty of LB"]).strip('[]'))
def ownTeamTwo():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width/2+width/45,height-height/13, blue2)
		c.drawString(width/2+width/45,height-height/13-1*(height/30),str(totals[blue2]["Total Alliance Points"]))
		c.drawString(width/2+width/45,height-height/13-1.75*(height/30),overall[blue2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-2.5*(height/30),overall[blue2]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-3.25*(height/30),str(overall[blue2]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-4*(height/30),str(overall[blue2]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-4.75*(height/30),str(overall[blue2]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-5.5*(height/30),str(overall[blue2]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue2]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-6.25*(height/30),str(overall[blue2]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width/2+width/45,height-height/13, red2)
		c.drawString(width/2+width/45,height-height/13-1*(height/30),str(totals[red2]["Total Alliance Points"]))
		c.drawString(width/2+width/45,height-height/13-1.75*(height/30),overall[red2]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-2.5*(height/30),overall[red2]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width/2+width/45,height-height/13-3.25*(height/30),str(overall[red2]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-4*(height/30),str(overall[red2]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-4.75*(height/30),str(overall[red2]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-5.5*(height/30),str(overall[red2]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[red2]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width/2+width/45,height-height/13-6.25*(height/30),str(overall[red2]["Overall Average Difficulty of LB"]).strip('[]'))
def ownTeamThree():
	c.setFont("Helvetica",14)
	if(ourAlliance == 'Blue'):
		c.drawString(width+width/45-width/4,height-height/13, blue3)
		c.drawString(width-width/4+width/45,height-height/13-1*(height/30),str(totals[blue3]["Total Alliance Points"]))
		c.drawString(width-width/4+width/45,height-height/13-1.75*(height/30),overall[blue3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-2.5*(height/30),overall[blue3]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-3.25*(height/30),str(overall[blue3]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-4*(height/30),str(overall[blue3]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-4.75*(height/30),str(overall[blue3]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-5.5*(height/30),str(overall[blue3]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[blue3]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-6.25*(height/30),str(overall[blue3]["Overall Average Difficulty of LB"]).strip('[]'))
	else:
		c.drawString(width+width/45-width/4,height-height/13, red3)
		c.drawString(width-width/4+width/45,height-height/13-1*(height/30),str(totals[red3]["Total Alliance Points"]))
		c.drawString(width-width/4+width/45,height-height/13-1.75*(height/30),overall[red3]["Overall Probability of Scoring High Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-2.5*(height/30),overall[red3]["Overall Probability of Scoring Low Goals"].strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-3.25*(height/30),str(overall[red3]["Overall Average Difficulty of PC"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of CF"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-4*(height/30),str(overall[red3]["Overall Average Difficulty of RP"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of M"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-4.75*(height/30),str(overall[red3]["Overall Average Difficulty of SP"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of DB"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-5.5*(height/30),str(overall[red3]["Overall Average Difficulty of RW"]).strip('[]') + " || " + str(overall[red3]["Overall Average Difficulty of RT"]).strip('[]'))
		c.drawString(width-width/4+width/45,height-height/13-6.25*(height/30),str(overall[red3]["Overall Average Difficulty of LB"]).strip('[]'))
def suggestionBox():
	# c.line(0,(height-(height/13-23*(height/30))),width,(height-(height/13-23*(height/30))))
	c.setFont("Helvetica",12)
	c.drawString(width/80,height-height/13-23.4*(height/30),"Opp Alliance Suggestion:")
	c.rect(26,5,100,100, stroke=1, fill=0)
	c.rect(width/4+26,5,100,100, stroke=1, fill=0)
	c.rect(width/2+26,5,100,100, stroke=1, fill=0)
	c.rect(width-width/4+26,5,100,100, stroke=1, fill=0)
def writeBoxes():
	c.setFont("Helvetica",11)
	if(ourAlliance=='Blue'):
		defenseA = compareDefenseCategory(red1, red2, red3, "PC", "CF", overall)
	else:
		defenseA = compareDefenseCategory(blue1, blue2, blue3, 'PC', "CF", overall)
	if(ourAlliance=='Blue'):
		defenseB = compareDefenseCategory(red1, red2, red3, 'M', 'RP', overall)
	else:
		defenseB = compareDefenseCategory(blue1, blue2, blue3, 'M', 'RP', overall)
	if(ourAlliance=='Blue'):
		defenseC = compareDefenseCategory(red1, red2, red3, 'DB', 'SP', overall)
	else:
		defenseC = compareDefenseCategory(blue1, blue2, blue3, 'DB', 'SP', overall)
	if(ourAlliance=='Blue'):
		defenseD = compareDefenseCategory(red1, red2, red3, 'RW', 'RT', overall)
	else:
		defenseD = compareDefenseCategory(blue1, blue2, blue3, 'RW', 'RT', overall)
	print str(defenseA)
	if(defenseA['Alliance Average of CF'] != 'N/A' and defenseA['Alliance Average of PC'] != 'N/A'):
		if(defenseA['Alliance Average of CF'] > defenseA['Alliance Average of PC']):
			suggestedA = 'CF'
		elif(defenseA['Alliance Average of CF'] < defenseA['Alliance Average of PC']):
			suggestedA = 'PC'
		else:
			suggestedA = 'Tie'
	else:
		suggestedA = 'Not enough data.'
	c.drawString(28,90,'Suggested:')
	c.drawString(28,75,suggestedA)
	if(defenseA['Did not attempt PC']):
		c.drawString(28,60,'PC no attempt:')
		c.drawString(28,45,defenseA['Did not attempt PC'].strip('[]'))
	if(defenseA['Did not attempt CF']):
		c.drawString(28,30,'CF no attempt:')
		c.drawString(28,15,defenseA['Did not attempt CF'].strip('[]'))
	if(defenseB['Alliance Average of M'] != 'N/A' and defenseB['Alliance Average of RP'] != 'N/A'):
		if(defenseB['Alliance Average of M'] > defenseB['Alliance Average of RP']):
			suggestedB = 'M'
		elif(defenseB['Alliance Average of M'] < defenseB['Alliance Average of RP']):
			suggestedB = 'RP'
		else:
			suggestedB = 'Tie'
	else:
		suggestedB = 'Not enough data.'

	c.drawString(width/4+28,90,'Suggested:')
	c.drawString(width/4+28,75,suggestedB)
	if(defenseB['Did not attempt M']):
		c.drawString(width/4+28,60,'M no attempt:')
		c.drawString(width/4+28,45,defenseB['Did not attempt M'].strip('[]'))
	if(defenseB['Did not attempt RP']):
		c.drawString(width/4+28,30,'RP no attempt:')
		c.drawString(width/4+28,15,defenseB['Did not attempt RP'].strip('[]'))
	if(defenseC['Alliance Average of DB'] != 'N/A' and defenseC['Alliance Average of SP'] != 'N/A'):
		if(defenseC['Alliance Average of DB'] > defenseC['Alliance Average of SP']):
			suggestedC = 'DB'
		elif(defenseC['Alliance Average of DB'] < defenseC['Alliance Average of SP']):
			suggestedC = 'SP'
		else:
			suggestedC = 'Tie'
	else:
		suggestedC = 'Not enough data.'

	c.drawString(width/2+28,90,'Suggested:')
	c.drawString(width/2+28,75,suggestedC)
	if(defenseC['Did not attempt DB']):
		c.drawString(width/2+28,60,'DB no attempt:')
		c.drawString(width/2+28,45,defenseC['Did not attempt DB'].strip('[]'))
	if(defenseC['Did not attempt SP']):
		c.drawString(width/2+28,30,'SP no attempt:')
		c.drawString(width/2+28,15,defenseC['Did not attempt SP'].strip('[]'))
	if(defenseD['Alliance Average of RW'] != 'N/A' and defenseD['Alliance Average of RT'] != 'N/A'):
		if(defenseD['Alliance Average of RW'] > defenseD['Alliance Average of RT']):
			suggestedD = 'RW'
		elif(defenseD['Alliance Average of RW'] < defenseD['Alliance Average of RT']):
			suggestedD = 'RT'
		else:
			suggestedD = 'Tie'
	else:
		suggestedD = 'Not enough data.'

	c.drawString(width-width/4+28,90,'Suggested:')
	c.drawString(width-width/4+28,75,suggestedD)
	if(defenseD['Did not attempt RW']):
		c.drawString(width-width/4+28,60,'RW no attempt:')
		c.drawString(width-width/4+28,45,defenseD['Did not attempt RW'].strip('[]'))
	if(defenseD['Did not attempt RT']):
		c.drawString(width-width/4+28,30,'RT no attempt:')
		c.drawString(width-width/4+28,15,defenseD['Did not attempt RT'].strip('[]'))
	# if(defenseD['Alliance Average of RW'] != 'N/A' and defenseD['Alliance Average of RT'] != 'N/A'):
	# 	if(defenseD['Alliance Average of RW'] > defenseD['Alliance Average of RT']):
	# 		suggestedD = 'RW'
	# 	elif(defenseD['Alliance Average of RW'] < defenseD['Alliance Average of RT']):
	# 		suggestedD = 'RT'
	# 	else:
	# 		suggestedD = 'Tie'
	# else:
	# 	suggestedD = 'Not enough data.'

	# c.drawString(width-width/4+28,90,'Suggested:')
	# c.drawString(width-width/4+28,75,suggestedD)
	# if(defenseD['Did not attempt RW']):
	# 	c.drawString(width-width/4+28,60,'RW no attempt:')
	# 	c.drawString(width-width/4+28,45,defenseD['Did not attempt RW'].strip('[]'))
	# if(defenseD['Did not attempt RT']):
	# 	c.drawString(width-width/4+28,30,'RT no attempt:')
	# 	c.drawString(width-width/4+28,15,defenseD['Did not attempt RT'].strip('[]'))
writeBoxes()
suggestionBox()
# commentBox()
autoBoxOwnTeamOne()
oppAllianceBox()
oppTeamOne()
oppTeamTwo()
commentBox2()
oppTeamThree()
autoBoxOpp()
# autoBoxOwnTeamTwo()
# autoBoxOwnTeamThree()
ownTeamOne()
ownTeamTwo()
ownTeamThree()
ownAllianceBox()
tableLayout()
topBox()
c.showPage()
c.save()