
from ..models import Patient, Doctor


class PatientDAO:
    def getPatients(self,doctor:Doctor):
        return Patient.objects.filter(ascDoctor__username__exact=doctor.username)


