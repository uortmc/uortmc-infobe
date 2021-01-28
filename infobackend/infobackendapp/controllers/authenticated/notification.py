

from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User

from ...dao.doctor import DoctorDAO
from ...dao.notification import NotificationDAO
from ...dao.patient import PatientDAO
from ...dto.auth import SystemAuthDTO
import logging

from ...dto.notification import NotificationDTO
from ...dto.patient import PatientDTO
from ...exceptions.base import FieldsMissingException
from ...exceptions.doctordao import UserDoctorAscNotFound
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor, Patient, Notification
from ...etc.authenticated_util import authenticated
from ...dto.doctor import DoctorDTO as DoctorDTO

class NotificationsController:
    logger=logging.getLogger("Class:NotificationsController")
    loggingLayer=LoggingLayer(logger).log
    dao:NotificationDAO=NotificationDAO()
    dto:NotificationDTO=NotificationDTO("NotificationsController")
    doctorDao:DoctorDAO=DoctorDAO()
    @staticmethod
    def getNotifications(req:HttpRequest):
        if not authenticated(req):
            return JsonResponse(NotificationsController.loggingLayer(NotificationsController.dto.noActiveSession(), LogLevel.ERROR))
        try:
            doctor=NotificationsController.doctorDao.userToDoctor(req.user)
            notifications=NotificationsController.dao.getNotifications(doctor)
            return JsonResponse(NotificationsController.loggingLayer(NotificationsController.dto.successGetNotifications(notifications)))
        except UserDoctorAscNotFound as e:
            return JsonResponse(NotificationsController.loggingLayer(NotificationsController.dto.fail(e.reason),LogLevel.ERROR))

    @staticmethod
    def addNotification(req: HttpRequest):
        if not authenticated(req):
            return JsonResponse(NotificationsController.loggingLayer(NotificationsController.dto.noActiveSession(), LogLevel.ERROR))
        try:
            doctor=NotificationsController.doctorDao.userToDoctor(req.user)
            message=NotificationsController.__getAddNotificationRequestFields(req)
            notification=NotificationsController.__constructNotification(message,doctor)
            return JsonResponse(NotificationsController.loggingLayer(NotificationsController.dto.successAddNotification(notification)))
        except (UserDoctorAscNotFound , FieldsMissingException) as e:
            return JsonResponse(NotificationsController.loggingLayer(NotificationsController.dto.fail(e.reason),LogLevel.ERROR))

    @staticmethod
    def __getAddNotificationRequestFields(req: HttpRequest) -> ():
        try:
            return (req.POST['message'])
        except MultiValueDictKeyError:
            raise FieldsMissingException
    @staticmethod
    def __constructNotification(message:str,doctor:Doctor)->Notification:
        new=Notification(message=message,ascDoctor=doctor)
        new.save()
        return new





