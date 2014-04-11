from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("posts go here")

def new_user(request):
	return HttpResponse("Create a new user here")

def login(request):
	return HttpResponse("This is a login page")