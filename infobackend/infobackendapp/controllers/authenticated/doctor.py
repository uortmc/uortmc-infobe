from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User

from ...dao.doctor import DoctorDao
from ...dto.auth import SystemAuthDTO
import logging
from ...exceptions.doctordao import UserDoctorAscNotFound
from ...logging.levels import LogLevel
from ...logging.logging import LoggingLayer
from ...models import Doctor
from ...etc.authenticated_util import authenticated

class DoctorController:
    logger=logging.getLogger("Class:DoctorController")
    loggingLayer=LoggingLayer(logger).log
    dao:DoctorDao=DoctorDao()
    @staticmethod
    def profile(req:HttpRequest):
        if not authenticated(req):
            return JsonResponse({'not':'auth'})
        user=req.user
        try:
            doctor:Doctor=DoctorController.dao.userToDoctor(user)
            DoctorController.logger.error("User "+user.username+ "And doctor "+doctor.username+" Asc")
            return JsonResponse({'all':'ok'})
        except UserDoctorAscNotFound as e:
            return JsonResponse(DoctorController.loggingLayer)







