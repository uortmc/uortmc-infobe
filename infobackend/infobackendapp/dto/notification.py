
from .authenticatedDto import AuthenticatedDTO
from ..etc.dict_util import DictUtils as util
from ..models import Patient,Doctor
from ..serializer.doctor import DoctorSerializer
from ..serializer.patient import PatientSerializer


class NotificationDTO(AuthenticatedDTO):
    def __init__(self,handlerName:str):
        super(NotificationDTO, self).__init__(handlerName)

    def successGetNotifications(self, patients:list)->dict:
        pass
    def successAddNotification(self, patient:Patient)->dict:
        pass









