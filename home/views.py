from django.shortcuts import render ,HttpResponse

def home(requsat):
    return HttpResponse("This is the data")

def home2(requsat):
    return HttpResponse("I am Sazidul")

def about(requsat):
    return HttpResponse("This is my about page in portfolio project(/)")
def projects(requsat):
    return HttpResponse("This is my projects page in portfolio project(/)")
def contact(requsat):
    return HttpResponse("This is my contact page in portfolio project(/)")
def signup(requsat):
    return HttpResponse("This is my singup page in portfolio project(/)")