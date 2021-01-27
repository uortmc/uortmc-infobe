
from .abstract import AbstractDTO
from ..etc.dict_util import DictUtils as util
from ..models import Patient


class AuthenticatedDTO(AbstractDTO):
    def __init__(self,handlerName:str):
        super(AuthenticatedDTO, self).__init__(handlerName)

    def noActiveSession(self):
        return self.fail("Authenticated endpoint without active session")






