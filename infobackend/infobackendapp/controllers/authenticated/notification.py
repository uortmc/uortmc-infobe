

from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User

from ...dao.doctor import DoctorDAO
from ...dao.patient import PatientDAO
from ...dto.auth import SystemAuthDTO
import logging

from ...dto.patient import PatientDTO
from ...exceptions.base import FieldsMissingException
from ...exceptions.doctordao import UserDoctorAscNotFound
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor, Patient
from ...etc.authenticated_util import authenticated
from ...dto.doctor import DoctorDTO as DoctorDTO

class NotificationsController:
    logger=logging.getLogger("Class:NotificationsController")
    loggingLayer=LoggingLayer(logger).log
    dao:PatientDAO=PatientDAO()
    dto:PatientDTO=PatientDTO("NotificationsController")
    doctorDao:DoctorDAO=DoctorDAO()
    @staticmethod
    def getNotifications(req:HttpRequest):
        return JsonResponse({'all':'ok'})

    @staticmethod
    def addNotification(req: HttpRequest):
        return JsonResponse({'all': 'ok'})





