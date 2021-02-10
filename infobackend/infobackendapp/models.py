from django.db.models import *
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid
class Doctor(Model):
    username=CharField('Username',max_length=50,unique=True)
    first_name=CharField('First name', max_length=30)
    last_name = CharField('Last name', max_length=30)
    title = CharField('Title', max_length=30,default="Not Set")
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

class Notification(Model):
    message=CharField('Message',max_length=100)
    ascDoctor=ForeignKey(Doctor,on_delete=CASCADE)
    created=DateTimeField('Creation Date',default=now)

    def __str__(self):
        return "| Doctor :  "+str(self.ascDoctor)+"  | Message :  "+str(self.message)

class Patient(Model):
    first_name=CharField('First name', max_length=30)
    last_name = CharField('Last name', max_length=30)
    nino=CharField('National Insurance Number',max_length=9,unique=True)
    enrolled_date = DateTimeField('Enrolled date', default=now)
    comments=TextField('Comments',max_length=200,default="Not Set")
    ascDoctor=ForeignKey(Doctor,on_delete=CASCADE)

    def __str__(self):
        return "Patient "+self.first_name+" "+self.last_name


class Scan(Model):


    ALGORITHMS = [
        ('NS', 'NOT SET'),
        ('SVC', 'Simple Support Vector Machine')
    ]
    STATUS = [
        ('SUBMITTED', 'Submitted'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]
    ascPatient=ForeignKey(Patient,on_delete=CASCADE)
    token = UUIDField('Scan Token',unique=True, default=uuid.uuid4, editable=False)
    status=CharField('Scan Status',max_length=10,choices=STATUS,default=STATUS[0][0])
    algorithm=CharField('Algorithm Used',max_length=10,choices=ALGORITHMS,default=ALGORITHMS[0][0])
    comment = TextField('Doctors Comments',default="Not Set", max_length=300)

    def __str__(self):
        return "Scan "+str(self.token)



