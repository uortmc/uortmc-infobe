from django.shortcuts import render
from .controllers.auth import SystemAuth



def auth_login(req):
    return SystemAuth.auth_login(req)