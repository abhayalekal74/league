from django.shortcuts import render
from models import Team, Fixture
from django.http import HttpResponse

def index(request):
	teams = Team.objects.all() 
	context = dict()
	context['teams'] = teams
	return render(request, 'index.html', context)