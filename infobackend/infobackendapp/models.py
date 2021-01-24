from django.db.models import *
from django.contrib.auth.models import User
from django.utils.timezone import now

class Doctor(Model):
    username=CharField('Username',max_length=50)
    first_name=CharField('First name', max_length=30)
    last_name = CharField('Last name', max_length=30)
    title = CharField('Title', max_length=30,default="Doctors Title not set")
    enrolled_date = DateTimeField('Enrolled date', default=now)
    last_seen = DateTimeField('Last seen', default=now)
    online_status=BooleanField('Online status', default=True)
    tasks=IntegerField('Tasks',default=0)

    def __str__(self):
        return "Doctor "+self.first_name+" "+self.last_name

    @staticmethod
    def fromUser(user:User): # -> Doctor (for some reason this annon doesnt work)
        id=None
        try:
            id=Doctor.objects.latest('id').id+1
        except ObjectDoesNotExist:
            id=0
        return Doctor(id=id,username=user.username,first_name=user.first_name,last_name=user.last_name)


class Patient(Model):
    first_name=CharField('First name', max_length=30)
    last_name = CharField('Last name', max_length=30)
    enrolled_date = DateTimeField('Enrolled date', default=now)
    comments=TextField('Comments',max_length=200)
    ascDoctor=ForeignKey(Doctor,on_delete=CASCADE)

    def __str__(self):
        return "Patient "+self.first_name+" "+self.last_name

class Scan(Model):
    token=TextField('Scan TE Token',max_length=300)
    ascPatient=ForeignKey(Patient,on_delete=CASCADE)

    def __str__(self):
        return "Scan "+self.token



