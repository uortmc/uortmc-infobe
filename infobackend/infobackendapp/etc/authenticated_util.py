from django.http import HttpRequest


def authenticated(req:HttpRequest):
    return req.user.is_authenticated
