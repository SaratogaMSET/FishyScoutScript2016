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
'649':[{'match':4,'scouter':'Bassil','points':230},{'match':9,'scouter':'Koh Koh','points':120}]
}
numberOfMatches = len(teams[team])
# print str(teams[team(0['match'])])

def drawTable():
	c.rect(height/50,width/50,height-height/25,width-width/25, fill=0)
def matchNumber():
	c.drawString(height/48,width-2*(width/45),"Match")
	c.line(height/15,width-width/50,height/15,width/50)
	i=1
	while i<numberOfMatches:
		c.line(height-height/40,(i+1)*(width/16),height/50,(i+1)*(width/16))
		i+=1
matchNumber()
drawTable()
c.showPage()
c.save()