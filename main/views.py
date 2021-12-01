from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):

    context={
        "name":settings.DATA["NAME"],
        "About_me":settings.DATA["About_me"]
    }
    return render(request,'main/index.html',context)

def projects(request):
    context={
        "projects":settings.DATA["projects"]
    }
    return render(request,'main/projects.html',context)

def languages(request):
    context={}
    return render(request,'main/languages.html',context)