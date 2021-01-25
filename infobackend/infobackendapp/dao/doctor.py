from ..exceptions.doctordao import UserDoctorAscNotFound
from ..models import Doctor
from django.contrib.auth.models import User
class DoctorDao:

    def userToDoctor(self,user:User)->Doctor:
        doc=Doctor.objects.filter(username=user.username)
        if len(doc) is not 1:
            raise UserDoctorAscNotFound
        return doc[0]





