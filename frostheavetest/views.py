from django.shortcuts import get_object_or_404, render
import requests
from django.http import HttpResponse
import json

from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.hmtl')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "you're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def player(request):
    r = requests.get('https://www.haloapi.com/stats/h5/servicerecords/arena?players=darkwolf king54')
    player = r.json()
    return render(request, 'data/player.html', {
        'Gamertag': player['Gamertag'],
        'TotalKills': player['TotalKills'],
        'Ocp-Apim-Subscription-Key': '92a2365131bb451e9cf5fc960ba1df22'
    })
