from django.db import IntegrityError

from ..exceptions.base import NinoUniquenessViolation
from ..exceptions.scan import ScanNotFound
from ..models import Patient, Doctor,Scan
class ScanDAO:
    def getScansFromDoctor(self,doctor:Doctor)->list:
        return Scan.objects.filter(ascPatient__ascDoctor__username__iexact=doctor.username)

    def getScanFromDoctor(self,doctor:Doctor,token:str)->Scan:
        filterop=self.getScansFromDoctor(doctor).filter(token=token)
        if(len(filterop)==0):
            raise ScanNotFound # Token is unique, so this list will always have 1 or 0 elements
        return filterop[0]

    def updateScanComment(self,scan:Scan,comment:str)->Scan:
        scan.comment=comment
        scan.save()
        return scan

    def declareScanComplete(self, token)->Scan:
        s = Scan.objects.filter(token=token)
        if (len(s) == 0):
            raise ScanNotFound
        scan=s[0]  # Token is unique, so this list will always have 1 or 0 elements
        scan.status=scan.Status.COMPLETED
        scan.save()
        return scan

    def addScan(self,patient:Patient)->Scan:
        try:
            newScan=Scan(ascPatient=patient)
            newScan.save()
            return newScan
        except IntegrityError as e:
            raise NinoUniquenessViolation
