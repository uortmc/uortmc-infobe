

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
from ...exceptions.doctordao import UserDoctorAscNotFound
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor
from ...etc.authenticated_util import authenticated
from ...dto.doctor import DoctorDTO as DoctorDTO

class PatientController:
    logger=logging.getLogger("Class:PatientController")
    loggingLayer=LoggingLayer(logger).log
    dao:PatientDAO=PatientDAO()
    dto:PatientDTO=PatientDTO("PatientController")
    doctorDao:DoctorDAO=DoctorDAO()
    @staticmethod
    def getPatient(req:HttpRequest):
        #Is Logged in?
        if not authenticated(req):
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.noActiveSession(), LogLevel.ERROR))
        #Is a doctor or an another user?
        try:
            doctor=PatientController.doctorDao.userToDoctor(req.user)
            patients=PatientController.dao.getPatients(doctor)
            PatientController.logger.error(patients)
            return JsonResponse(PatientController.dto.successAddPatients(patients))
        except UserDoctorAscNotFound as e:
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.fail(e.reason),LogLevel.ERROR))

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





