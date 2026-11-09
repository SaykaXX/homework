from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "myapp/index.html", {"title": "Home"})

def user_detail(request, id):
    return HttpResponse(f"User: {id}")
