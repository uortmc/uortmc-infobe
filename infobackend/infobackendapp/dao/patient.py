from django.db import IntegrityError

from ..exceptions.base import NinoNotFound, NinoUniquenessViolation
from ..models import Patient, Doctor


class PatientDAO:
    def getPatients(self,doctor:Doctor):
        return Patient.objects.filter(ascDoctor__username__exact=doctor.username)

    def constructPatient(self,first_name: str, last_name: str, nino: str, doctor: Doctor) -> Patient:
        try:
            new = Patient(first_name=first_name, last_name=last_name, nino=nino, ascDoctor=doctor)
            new.save()
            return new
        except IntegrityError as e:
            raise NinoUniquenessViolation

    def getPatientFromNino(self,doctor:Doctor,nino:str)->Patient:
        retval=self.getPatients(doctor).filter(nino=nino)
        if(len(retval)==0):
            raise NinoNotFound
        return retval[0] #Get the first, nino is unique, so every nino should have only 1 entry

    def setPatientCommentFromNino(self,doctor:Doctor,nino:str,comment:str)->Patient:
        instance=self.getPatientFromNino(doctor,nino)
        instance.comments=comment
        instance.save()
        return instance



