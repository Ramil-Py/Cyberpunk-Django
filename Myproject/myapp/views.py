from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render(request, f"myapp/index.html")

def about(request):
    return HttpResponse("<h1>About</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")