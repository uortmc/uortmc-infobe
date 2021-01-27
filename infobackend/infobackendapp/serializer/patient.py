from ..models import Patient
from .doctor import DoctorSerializer


class PatientSerializer():
    @staticmethod
    def toDict(patient: Patient) -> dict:
        return {
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "nino": patient.nino,
            "enrolled_date": patient.enrolled_date,
            "comments": patient.comments,
            "ascDoctor": DoctorSerializer.toDict(patient.ascDoctor)
        }
