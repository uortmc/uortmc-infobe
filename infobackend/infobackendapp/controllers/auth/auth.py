from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User

from ...dao.doctor import DoctorDAO
from ...dto.auth import SystemAuthDTO
import logging

from ...exceptions.base import FieldsMissingException
from ...exceptions.doctordao import UserAlreadyExists
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor
from ...etc.authenticated_util import authenticated

class SystemAuth:
    logger=logging.getLogger("Class:SystemAuth")
    loggingLayer=LoggingLayer(logger).log
    dto=SystemAuthDTO("SystemAuth")
    doctorDao=DoctorDAO()
    @staticmethod
    def auth_login(req:HttpRequest):
        try:
            username,password=SystemAuth.__getLoginCredentials(req)
            user = authenticate(req, username=username, password=password)
            if not authenticated(req):
                if (user is not None):
                    login(user=user, request=req)
                    return JsonResponse(SystemAuth.loggingLayer(SystemAuth.dto.loginSuccess()))
                else:
                    return JsonResponse(SystemAuth.loggingLayer(SystemAuth.dto.invalidCredentials(),LogLevel.ERROR))
            else:
                return JsonResponse(SystemAuth.loggingLayer(SystemAuth.dto.loginSuccess()))
        except FieldsMissingException as e:
            return JsonResponse(SystemAuth.loggingLayer(SystemAuth.dto.fail(e.reason),LogLevel.ERROR))

    @staticmethod
    def __getLoginCredentials(req: HttpRequest) -> ():
        try:
            return (req.POST['username'], req.POST['password'])
        except MultiValueDictKeyError:
            raise FieldsMissingException


    @staticmethod
    def auth_signUp(req:HttpRequest):
        try:
            credentials=SystemAuth.__getSignUpCredentials(req)
            doctor=SystemAuth.doctorDao.constructDoctor(*credentials)
            return JsonResponse(SystemAuth.loggingLayer(SystemAuth.dto.signUpSuccess(doctor)))
        except (FieldsMissingException,UserAlreadyExists )as e:
            return JsonResponse(SystemAuth.loggingLayer(SystemAuth.dto.fail(e.reason),LogLevel.ERROR))



    @staticmethod
    def __getSignUpCredentials(req: HttpRequest) -> ():
        try:
            return (req.POST['username'],req.POST['email'], req.POST['password'],req.POST['first_name'],req.POST['last_name'])
        except MultiValueDictKeyError:
            raise FieldsMissingException





