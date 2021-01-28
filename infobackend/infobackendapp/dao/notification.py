from ..exceptions.doctordao import UserDoctorAscNotFound
from ..models import Doctor, Notification
from django.contrib.auth.models import User
class NotificationDAO:

    def getNotifications(self,doctor:Doctor)->list:
        return Notification.objects.filter(ascDoctor__username__exact=doctor.username)

    def constructNotification(self,message: str, doctor: Doctor) -> Notification:
        new = Notification(message=message, ascDoctor=doctor)
        new.save()
        return new





