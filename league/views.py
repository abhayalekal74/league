from django.template import loader
from models import Team, Fixture
from django.http import HttpResponse

def index(request):
	teams = Team.objects.all() 
	fixtures = Fixture.objects.all()
		# template = loader.get_template('index.html')
		# context = {
		# 	'teams': teams
		# }
		# return HttpResponse(template.render(context, request))
	common_init = """ 
					<html>
						<head>
							<style>
								table {
								    border-collapse: collapse;
								    width: 100%;
								}

								th, td {
								    text-align: left;
								    padding: 8px;
								}

								tr:nth-child(even){background-color: #f2f2f2}
							</style>
						</head>
						<body>
					"""
	
	rankings_table = """ 
		
			<h2>Team Standings</h2>
			<div style="overflow-x:auto;">
			<table border="1px">
				<tr>
					<th>
						Team
					</th>
					<th>
						Wins
					</th>
					<th>
						Loses
					</th>
					<th>
						Points
					</th>
				</tr>
				"""
	for team in teams:
		row = """
					<tr>
						<td> """ + team.name + """</td>
						<td>""" + str(team.won) + """</td>
						<td>""" + str(team.lost) + """</td>
						<td>""" + str(team.points) + """</td>
					</tr>
				"""
		rankings_table = rankings_table + row;		
	rankings_table = rankings_table + """ 
											</table>
										</div>												
										"""	

	fixtures_table = """			
				
			<h2>Fixtures</h2>
			<div style="overflow-x:auto;">
			<table border="1px">
				<tr>
					<th>
						Team 1
					</th>
					<th>
						Team 2
					</th>
					<th>
						Team 1 Points
					</th>
					<th>
						Team 2 Points
					</th>
					<th>
						Winner
					</th>
				</tr>
			"""
	for fixture in fixtures:
		winner = "NA"
		if fixture.team1_points > fixture.team2_points:
			winner = fixture.team1.name
		elif fixture.team2_points > fixture.team1_points:	
			winner = fixture.team2.name
		row = """
					<tr>
						<td> """ + fixture.team1.name + """</td>
						<td> """ + fixture.team2.name + """</td>
						<td> """ + str(fixture.team1_points) + """</td>
						<td> """ + str(fixture.team2_points) + """</td>
						<td> """ + winner + """</td>
					</tr>
				"""	
		fixtures_table = fixtures_table + row		
	fixtures_table = fixtures_table + """ 
											</table>
										</div>												
										"""
	common_end = """ 
						</body>
						</html>
					"""								
	return HttpResponse(common_init + rankings_table + fixtures_table + common_end)
