from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_first(request):
    return HttpResponse('THis is first view function of app1')


def app1_second(request):
    return HttpResponse('Second view function of app1')
