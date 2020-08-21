from urllib import urlopen
from bs4 import BeautifulSoup as soup

myurl = "https://www.ligamx.net/cancha/tablas/tablaGeneralClasificacion/sp/8934b8c89a62e0"

#opening up page
uClient = urlopen(myurl)
page_html = uClient.read()
uClient.close()

#html parsing
pageSoup = soup(page_html, "html.parser")

#grabs each team

teamInfo = pageSoup.findAll("tr")

teams = teamInfo[2:]

ligaMx = []

for team in teams:
	teamDict = {}
	teamdata = team.findAll("td")
	
	#get name
	name = teamdata[1].find("a", class_= "tpts loadershow col-xs-9 hidden-xs")
	teamDict = {"Team Name": name.string.strip()}
	
	#get games played
	gamesPlayed = teamdata[2].a.string
	teamDict["Games Played"] = gamesPlayed

	#get games won
	gamesWon = teamdata[3].a
	if gamesWon == None:
		teamDict["Games Won"] = teamdata[3].string
	else:
		teamDict["Games Won"] = gamesWon.string
	
	gamesTied = teamdata[4].a
	if gamesTied == None:
		teamDict["Games Tied"] = teamdata[4].string
	else:
		teamDict["Games Tied"] = gamesTied.string

	gamesLost = teamdata[5].a
	if gamesLost == None:
		teamDict["Games Lost"] = teamdata[5].string
	else:
		teamDict["Games Lost"] = gamesLost.string

	goalsFavor = teamdata[6].a
	if goalsFavor == None:
		teamDict["Goals Scored"] = teamdata[6].string
	else:
		teamDict["Goals Scored"] = goalsFavor.string

	goalsAgainst = teamdata[7].a
	if goalsAgainst == None:
		teamDict["Goals Against"] = teamdata[7].string
	else:
		teamDict["Goals Against"] = goalsAgainst.string

	goalDifference = teamdata[8].a
	if goalDifference == None:
		teamDict["Goal Difference"] = teamdata[8].string
	else:
		teamDict["Goal Difference"] = goalDifference.string

	points = teamdata[9].a
	if points == None:
		teamDict["Points"] = teamdata[9].string
	else:
		teamDict["Points"] = points.string
	ligaMx.append(teamDict)
	




myurl = "https://soyreferee.com/futbol/futbol-internacional/apodos-asi-se-les-llama-a-los-clubes-mx-y-en-argentina-espana-e-inglaterra/"


#opening up page
uClient = urlopen(myurl)
page_html = uClient.read()
uClient.close()

#html parsing
pageSoup = soup(page_html, "html.parser")


listOfNicks = pageSoup.find("div", class_="entry-content")

teamNicks = listOfNicks.findAll("li")

teamNicks = teamNicks[1:25]


def extractNickNames(s,l):
	n = s.find(",")
	if n == -1:
		l.append(s)
		return(l)
	else:
		nick = s[:n]
		l.append(nick)
		return(extractNickNames(s[n + 1:],l))
		



for team in teamNicks:
	team = team.text
	num = team.find(":")
	teamName = team[:num]
	nickNames = extractNickNames(team[num+2:],[])
	for teamDict in ligaMx:
		if teamDict["Team Name"] == teamName:
			teamDict["Nick Names"] = nickNames
		elif teamName == "Tigres" and teamDict["Team Name"] == "UANL":
			teamDict["Nick Names"] = nickNames
		elif teamName == "Pumas" and teamDict["Team Name"] == "PUMAS":
			teamDict["Nick Names"] = nickNames
		elif teamName == "Puebla" and teamDict["Team Name"] == "Puebla F.C.":
			teamDict["Nick Names"] = nickNames
		elif teamName == "Santos" and teamDict["Team Name"] == "Santos Laguna":
			teamDict["Nick Names"] = nickNames












#userTeam = input("Sobre que equipo quiere saber mas?\n")

def team_info(team):
	print("Informacion sobre {}".format(team["Team Name"]))
	print("Selecione del Menu para mas Informacion")
	uInput = input(" 1 - Juegos Ganados \n 2 - Juegos Perdidos \n 3 - Juegos Empatados \n 4 - Goles a favor y en contra \n 5 - Puntos \n 6 - Posicion \n 7 - Toda Informacion\n 8 - Salir \n")
	if uInput == 1:
		print("{} tiene {} juegos ganados.".format(team["Team Name"], team["Games Won"]))
		team_info(team)
	elif uInput == 2:
		print("{} tiene {} juegos perdidos.".format(team["Team Name"], team["Games Lost"]))
		team_info(team)		
	elif uInput == 3:
		print("{} tiene {} juegos empatados.".format(team["Team Name"], team["Games Tied"]))
		team_info(team)
	elif uInput == 4:
		print("{} tiene {} goles a favor y {} en contra con una diferencia de {}.".format(team["Team Name"], team["Goals Scored"], team["Goals Against"], team["Goal Difference"]))
		team_info(team)

	elif uInput == 5:
		print("{} tiene {} puntos.".format(team["Team Name"], team["Points"]))
		team_info(team)
	elif uInput == 6:
		print("{} esta en pocision {} de la tabla".format(team["Team Name"], team["Position"]))
	elif uInput == 7:
		print("{} tiene {} juegos ganados.".format(team["Team Name"], team["Games Won"]))
		print("{} tiene {} juegos perdidos.".format(team["Team Name"], team["Games Lost"]))
		print("{} tiene {} juegos empatados.".format(team["Team Name"], team["Games Tied"]))
		print("{} tiene {} goles a favor y {} en contra con una diferencia de {}.".format(team["Team Name"], team["Goals Scored"], team["Goals Against"], team["Goal Difference"]))
		print("{} tiene {} puntos.".format(team["Team Name"], team["Points"]))
		team_info(team)
	elif uInput == 8:
		print("Gracias")
	else:
		print("\nNo entiendo\n")
		team_info(team)


for team in ligaMx:
	print("{}".format(team["Team Name"]))



#for team in ligaMx:
	#team["Position"] = ligaMx.index(team) + 1
	#if team["Team Name"] == userTeam or "Nick Names" in team.keys() and userTeam in team["Nick Names"]:
		#team_info(team)






