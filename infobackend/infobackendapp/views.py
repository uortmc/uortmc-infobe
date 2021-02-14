from django.shortcuts import render
from .controllers.auth.auth import SystemAuth
from .controllers.authenticated.doctor import DoctorController
from .controllers.authenticated.notification import NotificationsController
from .controllers.authenticated.patient import PatientController
from .controllers.authenticated.scan import ScanController


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
def authenticated_setPatientComment(req):
    return PatientController.setPatientsComment(req)
def authenticated_getNotifications(req):
    return NotificationsController.getNotifications(req)
def authenticated_addNotification(req):
    return NotificationsController.addNotification(req)
def authenticated_getScans(req):
    return ScanController.getScans(req)
def authenticated_addScan(req):
    return ScanController.addScan(req)
def scanComplete(req):
    return NotificationsController.scanCompleteNotification(req)