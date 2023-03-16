from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_first(request):
    return HttpResponse('This is the first view function of app2')


def app2_second(request):
    return HttpResponse('second view function of app2')
