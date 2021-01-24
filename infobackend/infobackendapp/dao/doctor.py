
from ..models import Doctor
from django.contrib.auth.models import User
class DoctorDao:

    def userToDoctor(self,user:User)->Doctor:
        return Doctor.objects.filter(username=user.username)




