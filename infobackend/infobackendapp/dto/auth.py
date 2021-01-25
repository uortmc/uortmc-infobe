
from ..etc.dict_util import DictUtils as util
from .abstract import AbstractDTO
class SystemAuthDTO(AbstractDTO):
    def __init__(self):
        super(SystemAuthDTO, self).__init__("SystemAuth")
    
    def loginSuccess(self)->dict:
        return SystemAuthDTO.success(self)

    
    def loginFailed(self,reason: str) -> dict:
        return util.merge(
                SystemAuthDTO.fail(self),
                {"reason": reason})

    
    def invalidCredentials(self) -> dict:
        return SystemAuthDTO.loginFailed(self,"Invalid Credentials")

    
    def alreadyExists(self) -> dict:
        return SystemAuthDTO.loginFailed(self,"User already exists")



    def signupSuccess(self) -> dict:
        return SystemAuthDTO.success(self)

    
    def signUpFailed(self,reason: str) -> dict:
        return util.merge(
                SystemAuthDTO.fail(self),
                {"reason": reason})

