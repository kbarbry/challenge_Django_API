from django.shortcuts import render
from django.http import HttpResponse

def mainPage(response):
	return HttpResponse("<h1>Welcome to our site</h1>")