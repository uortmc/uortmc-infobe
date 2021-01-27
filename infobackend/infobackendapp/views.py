from django.shortcuts import render
from .controllers.auth.auth import SystemAuth
from .controllers.authenticated.doctor import DoctorController
from .controllers.authenticated.patient import PatientController


def auth_login(req):
    return SystemAuth.auth_login(req)
def auth_signup(req):
    return SystemAuth.auth_signUp(req)

def authenticated_profile(req):
    return DoctorController.profile(req)
def authenticated_getPatient(req):
    return PatientController.getPatient(req)
def authenticated_addPatient(req):
    return PatientController.addPatient(req)