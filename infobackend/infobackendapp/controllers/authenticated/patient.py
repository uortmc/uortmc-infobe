

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
from ...exceptions.patient import NinoUniquenessViolation
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor, Patient
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
        if not authenticated(req):
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.noActiveSession(), LogLevel.ERROR))
        try:
            doctor=PatientController.doctorDao.userToDoctor(req.user)
            patients=PatientController.dao.getPatients(doctor)
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.successGetPatients(patients)))
        except UserDoctorAscNotFound as e:
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.fail(e.reason),LogLevel.ERROR))

    @staticmethod
    def addPatient(req: HttpRequest):
        if not authenticated(req):
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.noActiveSession(), LogLevel.ERROR))
        try:
            doctor=PatientController.doctorDao.userToDoctor(req.user)
            first_name,last_name,nino=PatientController.__getAddPatientRequestFields(req)
            patient=PatientController.__constructPatient(first_name,last_name,nino,doctor)
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.successAddPatient(patient)))
        except (UserDoctorAscNotFound , FieldsMissingException,NinoUniquenessViolation) as e:
            return JsonResponse(PatientController.loggingLayer(PatientController.dto.fail(e.reason),LogLevel.ERROR))


    @staticmethod
    def __getAddPatientRequestFields(req: HttpRequest) -> ():
        try:
            return (req.POST['first_name'], req.POST['last_name'],req.POST['nino'])
        except MultiValueDictKeyError:
            raise FieldsMissingException
    @staticmethod
    def __constructPatient(first_name:str,last_name:str,nino:str,doctor:Doctor)->Patient:
        try:
            new=Patient(first_name=first_name,last_name=last_name,nino=nino,ascDoctor=doctor)
            new.save()
            return new
        except IntegrityError as e:
            raise NinoUniquenessViolation






