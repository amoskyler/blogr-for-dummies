from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
def profile(request, user_name):
	user = get_object_or_404(User, username=user_name)
	message = user_name + "'s posts"
	return HttpResponse(message)

def register(request):
	return HttpResponse("Register here")

def login(request):
	return HttpResponse("This is a login page")