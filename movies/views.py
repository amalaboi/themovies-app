# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'movies':['gladiator','top gun','casino','john wick','yeh vada ha', 'ghazab', 'street fighter']
    }
    # context = {}
    return render(request,'movies/index.html', context)
    # return HttpResponse('My Favourite Movies')

# template naming structure ... appname/templates/appname/templatename.html e.g movies/templates/movies/index.html

def about(request):
    return render(request,'movies/about.html',{})

