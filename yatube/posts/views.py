from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

def group_posts(request, slug):
    return HttpResponse(f'Это {slug}')