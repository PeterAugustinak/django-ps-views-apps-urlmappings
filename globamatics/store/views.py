from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello there, under construction it is ...")


def detail(request):
    return HttpResponse("This is detail view.")


def electronics(request):
    return HttpResponse("Electronics view.")
