# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
import datetime
from polls.models import Question,Choice

def index(request):
    date = datetime.datetime.now()
    return render(request, 'polls/index.html', {'date': date})

def home(request):
    date = datetime.datetime.now()
    return render(request, 'polls/home.html', {'date': date})





 