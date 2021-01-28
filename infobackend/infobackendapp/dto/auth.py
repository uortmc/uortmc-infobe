
from ..etc.dict_util import DictUtils as util
from .abstract import AbstractDTO
from ..serializer.doctor import DoctorSerializer


class SystemAuthDTO(AbstractDTO):
    def __init__(self,handlerName:str):
        super(SystemAuthDTO, self).__init__(handlerName)

    def loginSuccess(self)->dict:
        return SystemAuthDTO.success(self)


    def invalidCredentials(self) -> dict:
        return SystemAuthDTO.fail(self,"Invalid Credentials")


    def signUpSuccess(self,doctor) -> dict:
        return SystemAuthDTO.successWithResponce(self,DoctorSerializer.toDict(doctor))


