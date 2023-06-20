from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,
                "frontapp/index.html",
                {})
    
def main(request):
    return render(request,
                "frontapp/main.html",
                {})
    
def map(request):
    return render(request,
                "frontapp/map.html",
                {})

def detailView(request):
    return render(request,
                "frontapp/detailView.html",
                {})
    
def favorite(request):
    return render(request,
                "frontapp/favorite.html",
                {})

def direction(request):
    return render(request,
                "frontapp/direction.html",
                {})