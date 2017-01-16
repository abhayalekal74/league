from django.template import loader
from models import Team, Fixture
from django.http import HttpResponse

week2_start_time = 1484542800000
millis_per_week = 604800000

def index(request):
	teams = Team.objects.all().order_by('-won') 
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

	
	common_end = """ 
						</body>
						</html>
					"""								
	return HttpResponse(common_init + rankings_table + common_end)

def update_db(fixture, w, update_winner):
	import os
	from pyexcel_xlsx import get_data
	cur_path = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(cur_path, "data/" + str(w) + ".xlsx")
	data = get_data(file_path)['Sheet1']
	for row_num in range(1,len(data)):
		row = data[row_num]
		if row[0] == fixture.team1.name:
			calls_per_day = row[2] 
			group_sales = row[3] * 5
			meetings = row[4] * 5
			fse = row[5] * 17
			five_match_plans = row[6] * 5
			fixture.team1_points = calls_per_day + group_sales + meetings + fse + five_match_plans
		elif row[0] == fixture.team2.name:
			calls_per_day = row[2] 
			group_sales = row[3] * 5
			meetings = row[4] * 5
			fse = row[5] * 17
			five_match_plans = row[6] * 5
			fixture.team2_points = calls_per_day + group_sales + meetings + fse + five_match_plans
	if update_winner:
		winning_team = None
		losing_team = None
		if fixture.team1_points > fixture.team2_points:
			fixture.winner = fixture.team1.name
			winning_team = Team.objects.get(name=fixture.team1.name)
			losing_team = Team.objects.get(name=fixture.team2.name)
		elif fixture.team2_points > fixture.team1_points:
			fixture.winner = fixture.team2.name				
			winning_team = Team.objects.get(name=fixture.team2.name)
			losing_team = Team.objects.get(name=fixture.team1.name)
		else:
			fixture.winner = 'Tie'
		if winning_team is not None:
			winning_team.points = winning_team.points + 2
			winning_team.won = winning_team.won + 1
			winning_team.save()	
		if losing_team is not None:
			losing_team.lost = losing_team.lost + 1
			losing_team.save()	
	print fixture.winner			
	fixture.save()		

def read_from_sheet(fixtures, w):
	w = int(w)
	from pytz import timezone
	from datetime import datetime
	tz = timezone('US/Eastern')
	current_time =  int(datetime.now(tz).strftime("%s")) * 1000
	current_week = ((current_time - week2_start_time) // millis_per_week) + 2
	if w < current_week:
		print "check1"
		for fixture in fixtures:
			print fixture.winner
			if fixture.winner == 'NA':
				update_db(fixture, w, True)		
	elif w > current_week:
		return False
	else:
		for fixture in fixtures:
			update_db(fixture, w, False)
	return True				
		

def fixtures(request, w):
	fixtures = Fixture.objects.filter(week=w)
	hasData = read_from_sheet(fixtures, w)
	if not hasData:
		return HttpResponse("This week's data is not provided")
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
	fixtures_table = """ 
		
			<h2>Week """ + str(w) + """ Fixtures</h2>
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
						Winner
					</th>
				</tr>
				"""
	for fixture in fixtures:
		winner = "NA"

		row = """
					<tr>
						<td>""" + fixture.team1.name +" ("+ str(fixture.team1_points) + ")" + """</td>
						<td>""" + fixture.team2.name +" ("+ str(fixture.team2_points) + ")" +  """</td>
						<td>""" + fixture.winner + """</td>
					</tr>
				"""
		fixtures_table = fixtures_table + row;		
	fixtures_table = fixtures_table + """ 
											</table>
										</div>												
										"""			

	common_end = """ 
						</body>
					</html>
				"""			
	return HttpResponse(common_init + fixtures_table + common_end)			