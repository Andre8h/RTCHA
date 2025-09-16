from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeage(request):
    return HttpResponse("Welcome")

