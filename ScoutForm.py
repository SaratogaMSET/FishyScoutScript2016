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


team = '649'
teams = generateDict("oneFile.txt")

overall = generateTeamOverall(teams)
auto = generateAutoDict(teams)
rankings = generateRankings(overall,auto)
totals = generateTotals(teams,overall)
totalsRankings = generateTotalsRankings(totals)

# picture = 'C:\Python27\dozer.jpg'
b = canvas.Canvas(team + " Scouting Form " + "Page 1.pdf",pagesize = letter)
# c = canvas.Canvas(team + " Scouting Form " + "Page 2.pdf",pagesize = landscape(letter))
# c2 = canvas.Canvas(team + " Scouting Form " + "Page 3.pdf",pagesize = landscape(letter))
# a = canvas.Canvas(team + " New Scouting Form " + "Page 2.pdf",pagesize = letter)
# a2 = canvas.Canvas(team + " New Scouting Form " + "Page 3.pdf",pagesize = letter)
# c.setLineWidth(.3)
width , height = letter
"""Team Number : [] dict Game : Scouter name, name"""


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
	b.drawString(width/45,height-height/25,"Scouting Form")
	b.drawString(width-width/4,height-height/25, "Team " + team )
	b.setFont("Helvetica",16)
	b.drawString(width/2.25,height/2,"Data!")
	# b.drawString(width/45,(height-height/2)-13*(height/35),"Key:")
	b.setFont("Helvetica",12)
	# b.drawString(width/45,(height/2)-14*(height/35),"All defensive rankings are between 0-3. 0 means nearly flawless, 1 means decent,")
	# b.drawString(width/45,(height/2)-15*(height/35),"2 means struggled, 3 means impossible or nearly impossible, and N/A means not attempted.")
	b.drawString(width/2.25,(height-height/2)-(height/35),str(totals[team]["Total Alliance Points"]))
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
	b.drawString(width/2.25,(height-height/2)-13*(height/35),str(auto[team]["Probability of Scoring Auto High Goals"]))
	b.drawString(width/2.25,(height-height/2)-14*(height/35),str(auto[team]["Probability of Scoring Auto Low Goals"]))
	b.drawString(width/2.25,(height-height/2)-15*(height/35),str(auto[team]["Ratio of Crossing a Defense in Auto"]))

def showRankings():
	global rankings
	b.setFont("Helvetica",16)
	b.drawString(width/45,height-height/2,"Percent Rankings")
	b.drawString(width/1.6,height/2,"Completion Rankings")
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
	b.drawString(width/45,(height-height/2)-13*(height/35),"Auto High Goal Percentage:")
	b.drawString(width/3,(height-height/2)-13*(height/35),str(rankings["Probability of Scoring Auto High Goals"][team]))
	b.drawString(width/45,(height-height/2)-14*(height/35),"Auto Low Goal Percentage:")
	b.drawString(width/3,(height-height/2)-14*(height/35),str(rankings["Probability of Scoring Auto Low Goals"][team]))
	b.drawString(width/45,(height-height/2)-15*(height/35),"Ratio of Crossing Defenses in Auto:")
	b.drawString(width/3,(height-height/2)-15*(height/35),str(rankings["Ratio of Crossing a Defense in Auto"][team]))
	b.drawString(width/1.6,(height-height/2)-height/35,"Match Point Average")
	b.drawString(width/1.1,(height/2)-height/35,str(rankings["Average Alliance Match Points"][team]))
	b.drawString(width/1.6,(height-height/2)-2*(height/35),"High Goal Total:")
	b.drawString(width/1.1,(height-height/2)-2*(height/35),str(totalsRankings["Total Successes of High Goals"][team]))
	b.drawString(width/1.6,(height-height/2)-3*(height/35),"Portcullis Total:")
	b.drawString(width/1.1,(height-height/2)-3*(height/35),str(totalsRankings["Total Successes to Cross PC"][team]))
	b.drawString(width/1.6,(height-height/2)-4*(height/35),"Cheval de Frise Total:")
	b.drawString(width/1.1,(height-height/2)-4*(height/35),str(totalsRankings["Total Successes to Cross CF"][team]))
	b.drawString(width/1.6,(height-height/2)-5*(height/35),"Moat Total:" )
	b.drawString(width/1.1,(height-height/2)-5*(height/35),str(totalsRankings["Total Successes to Cross M"][team]))
	b.drawString(width/1.6,(height-height/2)-6*(height/35),"Ramparts Total:")
	b.drawString(width/1.1,(height-height/2)-6*(height/35),str(totalsRankings["Total Successes to Cross RP"][team]))
	b.drawString(width/1.6,(height-height/2)-7*(height/35),"Drawbridge Total:")
	b.drawString(width/1.1,(height-height/2)-7*(height/35),str(totalsRankings["Total Successes to Cross SP"][team]))
	b.drawString(width/1.6,(height-height/2)-8*(height/35),"Sally Port Total:")
	b.drawString(width/1.1,(height-height/2)-8*(height/35),str(totalsRankings["Total Successes to Cross DB"][team]))
 	b.drawString(width/1.6,(height-height/2)-9*(height/35),"Rock Wall Total:")
 	b.drawString(width/1.1,(height-height/2)-9*(height/35),str(totalsRankings["Total Successes to Cross RW"][team]))
	b.drawString(width/1.6,(height-height/2)-10*(height/35),"Rough Terrain Total:")
	b.drawString(width/1.1,(height-height/2)-10*(height/35),str(totalsRankings["Total Successes to Cross RT"][team]))
	b.drawString(width/1.6,(height-height/2)-11*(height/35),"Low Bar Total:")
	b.drawString(width/1.1,(height-height/2)-11*(height/35),str(totalsRankings["Total Successes to Cross LB"][team]))
	b.drawString(width/1.6,(height-height/2)-12*(height/35),"Low Goal Total:")
	b.drawString(width/1.1,(height-height/2)-12*(height/35),str(totalsRankings["Total Successes of Low Goals"][team]))
	# b.drawString(width/1.6,(height-height/2)-13*(height/35),"Auto High Goal Total:")
	# b.drawString(width/1.1,(height-height/2)-13*(height/35),str(totalsRankings["Total Successes of Low Goals"][team]))
	# b.drawString(width/1.6,(height-height/2)-14*(height/35),"Auto Low Goal Total:")
	# b.drawString(width/1.1,(height-height/2)-14*(height/35),str(totalsRankings["Total Successes of Low Goals"][team]))
	# b.drawString(width/1.6,(height-height/2)-15*(height/35),"Total Crosses in Auto:")
	# b.drawString(width/1.1,(height-height/2)-15*(height/35),str(totalsRankings["Total Successes of Low Goals"][team]))
	# do this

bigData()
topBox()
showRankings()
prettyPicture()
b.showPage()
b.save()
print str(totals[team]["Total Alliance Points"])