
from ..etc.dict_util import DictUtils as util
from .abstract import AbstractDTO
class SystemAuthDTO(AbstractDTO):
    def __init__(self,handlerName:str):
        super(SystemAuthDTO, self).__init__(handlerName)

    def loginSuccess(self)->dict:
        return SystemAuthDTO.success(self)


    def invalidCredentials(self) -> dict:
        return SystemAuthDTO.fail(self,"Invalid Credentials")


    def alreadyExists(self) -> dict:
        return SystemAuthDTO.fail(self,"User already exists")



    def signupSuccess(self) -> dict:
        return SystemAuthDTO.success(self)


