from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Siiiiiii hpppppp")

def home2(request):
	return HttpResponse("Y de nuevo :)") 

def post(request,id_post):
	return HttpResponse("Este es el post numero %s" % id_post)