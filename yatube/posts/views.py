from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

# Главная страница


def index(request):
    template = 'posts/index.html'
    context = {
        "text": 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, slug):
    context = {
        "text": "Здесь будет информация о группах проекта Yatube"
    }
    return HttpResponse(f'Это {slug}')


def group_list(request):
    group_list = 'posts/group_list.html'
    return render(request, group_list)
