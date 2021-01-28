from django.db import IntegrityError

from ..exceptions.patient import NinoUniquenessViolation
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


