from django.shortcuts import render
from django.http import HttpResponse

dict_of_posts = {
    1:'index.html'
}

def post(request, id):
    try:
        return render(request, f"myapp/{dict_of_posts[id]}")
    except:
        return HttpResponse("<h1>Error</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")