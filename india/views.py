from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def virat(request):
    return HttpResponse('<h1>Virat scored 50<sup>th</sup> century in ODI</h1>')

def shreyash(request):
    return HttpResponse('<h1>Shreyash scored century in WC semi final</h1>')