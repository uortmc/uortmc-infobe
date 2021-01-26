from .abstract import AbstractDTO
from ..etc.dict_util import DictUtils as util
from ..models import Doctor


class DoctorDTO(AbstractDTO):
    def __init__(self,handlerName:str):
        super(DoctorDTO, self).__init__(handlerName)

    def noActiveSession(self):
        return self.fail("Authenticated endpoint without active session")


    def successProfile(self,doctor:Doctor):
        return self.successWithResponce(
            {
                "username":doctor.username,
                "first_name":doctor.first_name,
                "last_name":doctor.last_name,
                "title":doctor.title,
                "enrolled_date":doctor.enrolled_date,
                "last_seen":doctor.last_seen,
                "online_status":doctor.online_status,
                "tasks":doctor.tasks
            }
        )
