from django.db.models import *

from django.utils.timezone import now

class Doctor(Model):
    name=CharField('Name', max_length=30)
    surname = CharField('Surname', max_length=30)
    title = CharField('Title', max_length=30)
    enrolled_date = DateTimeField('Enrolled date', default=now)
    last_seen = DateTimeField('Last seen', default=now)
    online_status=BooleanField('Online status', default=True)
    tasks=IntegerField('Tasks',default=0)

class Patient(Model):
    name=CharField('Name', max_length=30)
    surname = CharField('Surname', max_length=30)
    enrolled_date = DateTimeField('Enrolled date', default=now)
    comments=TextField('Comments',max_length=200)
    ascDoctor=ForeignKey(Doctor,on_delete=CASCADE)

class Scan(Model):
    token=TextField('Scan TE Token',max_length=300)
    ascPatient=ForeignKey(Patient,on_delete=CASCADE)



