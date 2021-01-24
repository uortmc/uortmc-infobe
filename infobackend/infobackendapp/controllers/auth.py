from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from ..dto.auth import SystemAuthDTO
import logging

from ..exceptions.auth import SystemAuthException
from ..logging.levels import LogLevel
from ..logging.logging import LoggingLayer
from ..models import Doctor


class SystemAuth:
    logger=logging.getLogger("SystemAuth")
    loggingLayer=LoggingLayer(logger).log
    @staticmethod
    def index(req:HttpRequest):
        return HttpResponse("Index")
    @staticmethod
    def auth_login(req:HttpRequest):
        try:
            username,password=SystemAuth.getLoginCredentials(req)
            user = authenticate(req, username=username, password=password)
            if (not req.user.is_authenticated):
                if (user is not None):
                    login(user=user, request=req)
                    return JsonResponse(SystemAuth.loggingLayer(SystemAuthDTO.loginSuccess()))
                else:
                    return JsonResponse(SystemAuth.loggingLayer(SystemAuthDTO.loginFailed("Invalid Credentials"),LogLevel.ERROR))
            else:
                return JsonResponse(SystemAuth.loggingLayer(SystemAuthDTO.loginSuccess()))
        except SystemAuthException as e:
            return JsonResponse(SystemAuth.loggingLayer(SystemAuthDTO.loginFailedWithException(e),LogLevel.ERROR))

    @staticmethod
    def getLoginCredentials(req: HttpRequest) -> ():
        try:
            return (req.POST['username'], req.POST['password'])
        except MultiValueDictKeyError:
            raise SystemAuthException("Bad request: Request without the necessary fields has being raised.")


    @staticmethod
    def auth_signUp(req:HttpRequest):
        try:
            credentials=SystemAuth.getSignUpCredentials(req)
            user=User.objects.create_user(*credentials[0:2])
            user.first_name=credentials[3]
            user.last_name=credentials[4]
            user.save()
            Doctor.fromUser(user).save()
            return JsonResponse(SystemAuth.loggingLayer(SystemAuthDTO.signupSuccess()))
        except SystemAuthException as e:
            SystemAuth.logger.error(e)
            return JsonResponse(SystemAuth.loggingLayer(SystemAuthDTO.signUpFailedWithException(e),LogLevel.ERROR))
        except IntegrityError as e:
            SystemAuth.logger.error(e)
            return JsonResponse(SystemAuth.loggingLayer(SystemAuthDTO.signUpFailed("User Already Exists"),LogLevel.ERROR))



    @staticmethod
    def getSignUpCredentials(req: HttpRequest) -> ():
        try:
            return (req.POST['username'],req.POST['email'], req.POST['password'],req.POST['first_name'],req.POST['last_name'])
        except MultiValueDictKeyError:
            raise SystemAuthException("Bad request: Login Request without the necessary fields has being raised.")





