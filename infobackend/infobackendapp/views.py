from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.contrib.auth import authenticate, login
def index(req:HttpRequest):
    return HttpResponse("Index")
# Create your views here.

def login(req:HttpRequest):
    username=req.POST['username']
    password=req.POST['password']
    user=authenticate(req,username=username,password=password)
    if(user is not None):
        login(req,user)
        return HttpResponse("Hello "+username)
    else:
        return HttpResponse("Invalid Credentials")