from django.shortcuts import render

dict_of_posts = {
    1:''
}

def post(request, id):
    return render(request, f"myapp/{dict_of_posts[id]}")
