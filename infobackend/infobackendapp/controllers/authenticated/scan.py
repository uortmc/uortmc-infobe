

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
from ...exceptions.base import FieldsMissingException, NinoNotFound, NinoUniquenessViolation
from ...exceptions.doctordao import UserDoctorAscNotFound
from ...exceptions.scan import ScanNotFound
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
    patientDao:PatientDAO=PatientDAO()

    @staticmethod
    def getScans(req:HttpRequest):
        if not authenticated(req):
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.noActiveSession(), LogLevel.ERROR))
        try:
            ascDoctor=ScanController.doctorDao.userToDoctor(req.user)
            scans=ScanController.dao.getScansFromDoctor(ascDoctor)
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.successGetScans(scans)))
        except UserDoctorAscNotFound as e:
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.fail(e.reason),LogLevel.ERROR))


    @staticmethod
    def addScan(req: HttpRequest):
        if not authenticated(req):
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.noActiveSession(), LogLevel.ERROR))
        try:
            nino = ScanController.__getAddPatientRequestFields(req)
            ascDoctor=ScanController.doctorDao.userToDoctor(req.user)
            patient=ScanController.patientDao.getPatientFromNino(ascDoctor,nino)
            scan=ScanController.dao.addScan(patient)
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.successAddScan(scan)))
        except (UserDoctorAscNotFound, FieldsMissingException, NinoUniquenessViolation,NinoNotFound) as e :
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.fail(e.reason),LogLevel.ERROR))

    @staticmethod
    def __getAddPatientRequestFields(req:HttpRequest)->str:
        try:
            return (req.POST['nino'])
        except MultiValueDictKeyError as e:
            raise FieldsMissingException

    @staticmethod
    def updateScanComment(req:HttpRequest):
        if not authenticated(req):
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.noActiveSession(), LogLevel.ERROR))
        try:
            token,comment=ScanController.__getUpdateScanRequestFields(req)
            doctor=ScanController.doctorDao.userToDoctor(req.user)
            scan=ScanController.dao.getScanFromDoctor(doctor,token)
            updatedScan=ScanController.dao.updateScanComment(scan,comment)
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.success()))
        except (FieldsMissingException,UserDoctorAscNotFound,ScanNotFound) as e:
            return JsonResponse(ScanController.loggingLayer(ScanController.dto.fail(e.reason), LogLevel.ERROR))


    @staticmethod
    def __getUpdateScanRequestFields(req: HttpRequest) -> ():
        try:
            return (req.POST['token'],req.POST['comment'])
        except MultiValueDictKeyError as e:
            raise FieldsMissingException







