from django.shortcuts import render ,HttpResponse

def home(requsat):
    return HttpResponse("This is the data")

def home2(requsat):
    return HttpResponse("I am Sazidul")