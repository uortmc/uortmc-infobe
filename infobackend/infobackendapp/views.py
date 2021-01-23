from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def index(req:HttpRequest):
    return HttpResponse("Index")
# Create your views here.

def login(req:HttpRequest):
    username=req.POST['username']
    password=req.POST['password']
    return HttpResponse("Hello "+username)