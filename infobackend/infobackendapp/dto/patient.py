
from .authenticatedDto import AuthenticatedDTO
from ..etc.dict_util import DictUtils as util
from ..models import Patient,Doctor
from ..serializer.doctor import DoctorSerializer
from ..serializer.patient import PatientSerializer


class PatientDTO(AuthenticatedDTO,DoctorSerializer,PatientSerializer):
    def __init__(self,handlerName:str):
        super(PatientDTO, self).__init__(handlerName)

    def successAddPatients(self,patients:list)->dict:
        return self.successWithResponce(
            [PatientSerializer.toDict(x) for x in patients]
        )









