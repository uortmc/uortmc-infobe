from django.db import IntegrityError

from ..exceptions.doctordao import UserDoctorAscNotFound, UserAlreadyExists
from ..models import Doctor
from django.contrib.auth.models import User
class DoctorDAO:

    def userToDoctor(self,user:User)->Doctor:
        doc=Doctor.objects.filter(username=user.username)
        if len(doc) is not 1:
            raise UserDoctorAscNotFound
        return doc[0]

    def constructDoctor(self,username:str,email:str,password:str,first_name:str,lastname:str)->Doctor:
        try:
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = lastname
            user.save()
            doctor=Doctor.fromUser(user)
            doctor.save()
            return doctor
        except IntegrityError as e:
            raise UserAlreadyExists





