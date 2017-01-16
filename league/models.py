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

class Fixture(models.Model):
	team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
	team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
	team1_points = models.IntegerField(default=0)		
	team2_points = models.IntegerField(default=0)		
	week = models.IntegerField(default=0)		
	winner = models.CharField(max_length=128, default='NA')

	def __str__(self):
		return self.team1.name + " vs " + self.team2.name