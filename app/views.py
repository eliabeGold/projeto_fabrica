
from cgitb import html
from django.shortcuts import render 
from django.http import HttpResponse
import datetime
# Create your views here.


def home(request):
    now = datetime.datetime.now()
    return render(request, 'app/home.html')
    
