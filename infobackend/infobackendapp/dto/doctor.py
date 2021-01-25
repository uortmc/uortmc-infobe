from .abstract import AbstractDTO
from ..etc.dict_util import DictUtils as util
from ..models import Doctor


class DoctorDTO(AbstractDTO):
    def __init__(self):
        super(DoctorDTO, self).__init__("DoctorInfo")

    def failWithReason(self, reason: str):
        return util.merge(self.fail(),
                            {"reason": reason})

    def noActiveSession(self):
        return self.failWithReason("Authenticated endpoint without active session")

    def successWithResponce(self,responce:dict):
        return util.merge(self.success(),
                    {"responce":responce})
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
