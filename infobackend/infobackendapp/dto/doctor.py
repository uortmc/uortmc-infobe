from .authenticatedDto import AuthenticatedDTO
from ..etc.dict_util import DictUtils as util
from ..models import Doctor
from ..serializer.doctor import DoctorSerializer


class DoctorDTO(AuthenticatedDTO,DoctorSerializer):
    def __init__(self,handlerName:str):
        super(DoctorDTO, self).__init__(handlerName)

    def successProfile(self,doctor:Doctor):
        return self.successWithResponce(self.toDict(doctor))


