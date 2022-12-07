from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt

tweets = [{
	'author': 'Kim A',
	'title': 'tweet 1',
	'content': 'Blah blah blah',
	'date_posted': dt.now()
	},
	{	
	'author': 'Kim B',
	'title': 'tweet 2',
	'content': " I got two versions. twooo versions.",
	'date_posted': dt.now()
	}]

def home(request):
	context = {
	'tweets': tweets
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html', {{'title': 'About'}})
