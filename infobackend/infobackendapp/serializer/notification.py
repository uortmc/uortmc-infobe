from .doctor import DoctorSerializer
from ..models import Notification


class NotificationSerializer():
    @staticmethod
    def toDict(notification: Notification) -> dict:
        return {
            "created": notification.created,
            "message": notification.message,
            "ascDoctor": DoctorSerializer.toDict(notification.ascDoctor)
        }
