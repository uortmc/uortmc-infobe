from .base import InfobeException


class UserDoctorAscNotFound(InfobeException):
    def __init__(self):
        super(UserDoctorAscNotFound, self).__init__("Doctor-User association not found, this is probably because you "
                                                    "own a session of a superuser(User that is not Doctor, etc root)")
