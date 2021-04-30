from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("welcome to the meeting Planner!")


def date(request):
    return HttpResponse(" This page served at" + str(datetime.now()))


def about(request):
    return HttpResponse(" I'm a Software Engineer! who knows django! ")