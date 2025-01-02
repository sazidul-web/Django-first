from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("This is the data")

def home2(request):
    return HttpResponse("I am Sazidul")

def about(request):
    # return HttpResponse("This is my about page in portfolio project(/)")
    return render(request, 'home.html')

def projects(request):
    return HttpResponse("This is my projects page in portfolio project(/)")

def contact(request):
    return HttpResponse("This is my contact page in portfolio project(/)")

def signup(request):
    return HttpResponse("This is my signup page in portfolio project(/)")
