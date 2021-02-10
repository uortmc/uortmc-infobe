

from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User

from ...dao.doctor import DoctorDAO
from ...dao.patient import PatientDAO
from ...dao.scan import ScanDAO
from ...dto.auth import SystemAuthDTO
import logging

from ...dto.patient import PatientDTO
from ...dto.scan import ScanDTO
from ...exceptions.base import FieldsMissingException
from ...exceptions.doctordao import UserDoctorAscNotFound
from ...exceptions.patient import NinoUniquenessViolation, NinoNotFound
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor, Patient
from ...etc.authenticated_util import authenticated
from ...dto.doctor import DoctorDTO as DoctorDTO

class ScanController:
    logger=logging.getLogger("Class:ScanController")
    loggingLayer=LoggingLayer(logger).log
    dao:ScanDAO=ScanDAO()
    dto:ScanDTO=ScanDTO("ScanController")
    doctorDao:DoctorDAO=DoctorDAO()

    @staticmethod
    def getScans(req:HttpRequest):
        return JsonResponse({'all':'ok'})


    @staticmethod
    def addScan(req: HttpRequest):
        return JsonResponse({'all':'ok'})



