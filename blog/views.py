from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("posts go here")

def login(request):
	return HttpResponse("This is a login page")