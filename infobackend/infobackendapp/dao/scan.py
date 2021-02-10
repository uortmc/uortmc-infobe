from ..models import Patient, Doctor,Scan
class ScanDAO:
    def getScansFromDoctor(self,doctor:Doctor)->list:
        return Scan.objects.filter(ascPatient__ascDoctor__username__iexact=doctor.username)
