from ..exceptions.doctordao import UserDoctorAscNotFound
from ..models import Doctor, Notification
from django.contrib.auth.models import User
class NotificationDAO:

    def getNotifications(self,doctor:Doctor)->list():
        Notification.objects.filter(ascDoctor__username__exact=doctor.username)





