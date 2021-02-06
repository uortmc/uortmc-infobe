from .base import InfobeException


class NinoUniquenessViolation(InfobeException):
    def __init__(self):
        super(NinoUniquenessViolation,self).__init__("Given NINO already exists")
class NinoNotFound(InfobeException):
    def __init__(self):
        super(NinoNotFound,self).__init__("Given NINO Not found or not permitted")