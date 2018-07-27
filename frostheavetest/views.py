from django.shortcuts import get_object_or_404, render
import requests
from django.http import HttpResponse
import json

from .forms import PlayerForm


#from .models import Question
# Create your views here.

#admin test questions
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.hmtl')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return render(request, 'polls/index.html', context)
#
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk = question_id)
#    return render(request, 'polls/detail.html', {'question': question})
#
#def results(request, question_id):
#    response = "you're looking at the results of questions %s."
#    return HttpResponse(response % question_id)
#
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)


#data request

def player(request):
    search_result = {}
    if 'player' in request.GET:
        form = PlayerForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = PlayerForm()
    return render(request, 'data/player.html', {'form': form, 'search_result': search_result})
