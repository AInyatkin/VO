from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<a href=\"http://127.0.0.1:8000/answer\">Привет джанго!</a>")

def index2(request):
    return HttpResponse("И тебе привет!")
