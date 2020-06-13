from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# from .models import users
# from .models import useractive
# from django.contrib.auth.models import User


def index(request):
	return render(request,'index.html',{})

def qualification(request):
	return render(request,'qualification.html',{})

def skills(request):
	return render(request,'skills.html',{})

def experience(request):
	return render(request,'experience.html',{})

def projects(request):
	return render(request,'projects.html',{})

def achivements(request):
	return render(request,'achivements.html',{})

def certificate(request):
	return render(request,'certificate.html',{})

def contact(request):
	return render(request,'contact.html',{})
    
