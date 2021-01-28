
from .authenticatedDto import AuthenticatedDTO
from ..etc.dict_util import DictUtils as util
from ..models import Patient, Doctor, Notification
from ..serializer.doctor import DoctorSerializer
from ..serializer.notification import NotificationSerializer
from ..serializer.patient import PatientSerializer


class NotificationDTO(AuthenticatedDTO):
    def __init__(self,handlerName:str):
        super(NotificationDTO, self).__init__(handlerName)

    def successGetNotifications(self, notifications:list)->dict:
        return self.successWithResponce(
            [NotificationSerializer.toDict(each) for each in notifications]
        )
    def successAddNotification(self, notification:Notification)->dict:
        return self.successWithResponce(NotificationSerializer.toDict(notification))









