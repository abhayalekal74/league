from django.db import models
"""
	Tasks:

	1. Show team with most points
	2. Show the result of fixtures with points scored by the participating teams

"""

class Team(models.Model):
	name = models.CharField(max_length=128)
	won = models.IntegerField(default=0)
	lost = models.IntegerField(default=0)
	points = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=256)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	points = models.IntegerField(default=0)		
	calls_per_day = models.IntegerField(default=0)		
	group_sales = models.IntegerField(default=0)		
	meetings = models.IntegerField(default=0)		
	fse = models.IntegerField(default=0)		
	five_match_plan = models.IntegerField(default=0)		

	def __str__(self):
		return self.name

class Fixture(models.Model):
	team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
	team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
	winner = models.ForeignKey(Team)

	def __str__(self):
		return self.team1.name + " vs " + self.team2.name

class PointsOfUserPerFixture(models.Model):
	fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	points = models.IntegerField(default=0)

	def __str__(self):
		return str(points)
