from ..models import Doctor


class DoctorSerializer():
    @staticmethod
    def toDict(doctor: Doctor) -> dict:
        return {
                "username": doctor.username,
                "first_name": doctor.first_name,
                "last_name": doctor.last_name,
                "title": doctor.title,
                "enrolled_date": doctor.enrolled_date,
                "last_seen": doctor.last_seen,
                "online_status": doctor.online_status,
                "tasks": doctor.tasks
            }
