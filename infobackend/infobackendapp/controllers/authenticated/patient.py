

from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User

from ...dao.doctor import DoctorDAO
from ...dto.auth import SystemAuthDTO
import logging
from ...exceptions.doctordao import UserDoctorAscNotFound
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor
from ...etc.authenticated_util import authenticated
from ...dto.doctor import DoctorDTO as DoctorDTO

class PatientController:
    logger=logging.getLogger("Class:PatientController")
    loggingLayer=LoggingLayer(logger).log
    dao:DoctorDAO=DoctorDAO()
    dto:DoctorDTO=DoctorDTO("PatientController")

    @staticmethod
    def addPatient(req):
        return JsonResponse({'all':'ok'})
    """
    @staticmethod
    def profile(req:HttpRequest):
        if not authenticated(req):
            return JsonResponse(DoctorController.loggingLayer(DoctorController.dto.noActiveSession(),LogLevel.ERROR))
        user=req.user
        try:
            doctor:Doctor=DoctorController.dao.userToDoctor(user)
            return JsonResponse(DoctorController.loggingLayer(DoctorController.dto.successProfile(doctor)))
        except UserDoctorAscNotFound as e:
            return JsonResponse(DoctorController.loggingLayer(DoctorController.dto.failWithReason(e.reason),LogLevel.ERROR))
    """





