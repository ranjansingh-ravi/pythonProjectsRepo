from django.shortcuts import render #already populated
from django.http import HttpResponse  #importing to send http response

# Create your views here.

# function that accepts requests and returns static String
def index(request) :
    return HttpResponse("This is a view inside my_app")
