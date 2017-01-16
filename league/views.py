from django.template import loader
from models import Team, Fixture
from django.http import HttpResponse

def index(request):
	teams = Team.objects.all() 
	template = loader.get_template('index.html')
	context = {
		'teams': teams
	}
	return HttpResponse(template.render(context, request))