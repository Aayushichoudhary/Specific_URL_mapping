from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def williamson(request):
    return HttpResponse('<h1>Williamson scored 50 in WC semi final</h1>')

def ravindra(request):
    return HttpResponse('<h1><center>Wonderful youngster of New Zealand</center></h1>')
