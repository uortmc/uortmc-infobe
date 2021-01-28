
from .authenticatedDto import AuthenticatedDTO
from ..etc.dict_util import DictUtils as util
from ..models import Patient,Doctor
from ..serializer.doctor import DoctorSerializer
from ..serializer.patient import PatientSerializer


class PatientDTO(AuthenticatedDTO):
    def __init__(self,handlerName:str):
        super(PatientDTO, self).__init__(handlerName)

    def successGetPatients(self, patients:list)->dict:
        return self.successWithResponce(
            [PatientSerializer.toDict(x) for x in patients]
        )
    def successAddPatient(self, patient:Patient)->dict:
        return self.successWithResponce(
            PatientSerializer.toDict(patient)
        )









