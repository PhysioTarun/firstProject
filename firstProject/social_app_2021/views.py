from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('This is Home Page of Your SocialCircus! /n App Name: social_app_2021')
