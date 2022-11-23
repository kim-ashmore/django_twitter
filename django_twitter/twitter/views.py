from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'home.html')
	# return HttpResponse('<h1> Twitter Home </h1>')

def about(request):
	return HttpResponse('<h1> About Feaux Twitter </h1')
