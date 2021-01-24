
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError

from ..dto.auth import SystemAuthDTO
import logging

from ..exceptions.auth import SystemAuthException


class SystemAuth:
    logger=logging.getLogger("SystemAuth")
    @staticmethod
    def index(req:HttpRequest):
        return HttpResponse("Index")
    @staticmethod
    def auth_login(req:HttpRequest):
        try:
            username,password=SystemAuth.getCredentials(req)
            user = authenticate(req, username=username, password=password)
            if (not req.user.is_authenticated):
                if (user is not None):
                    login(user=user, request=req)
                    return JsonResponse(SystemAuthDTO.loginSuccess())
                else:
                    return JsonResponse(SystemAuthDTO.loginFailed("Invalid Credentials"))
            else:
                return JsonResponse(SystemAuthDTO.loginSuccess())
        except SystemAuthException as e:
            SystemAuth.logger.error(e)
            return JsonResponse(SystemAuthDTO.loginFailedWithException(e))



    @staticmethod
    def getCredentials(req:HttpRequest)->():
        try:
            return (req.POST['username'], req.POST['password'])
        except MultiValueDictKeyError:
            raise SystemAuthException("Bad request: Request without the necessary fields has being raised.")


