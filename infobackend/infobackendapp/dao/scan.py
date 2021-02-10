from django.db import IntegrityError

from ..exceptions.base import NinoUniquenessViolation
from ..models import Patient, Doctor,Scan
class ScanDAO:
    def getScansFromDoctor(self,doctor:Doctor)->list:
        return Scan.objects.filter(ascPatient__ascDoctor__username__iexact=doctor.username)
    def addScan(self,patient:Patient)->Scan:
        try:
            newScan=Scan(ascPatient=patient)
            newScan.save()
            return newScan
        except IntegrityError as e:
            raise NinoUniquenessViolation
