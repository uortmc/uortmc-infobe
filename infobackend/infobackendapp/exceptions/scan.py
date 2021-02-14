from .base import InfobeException


class ScanNotFound(InfobeException):
    def __init__(self):
        super(ScanNotFound, self).__init__("Given scan token not found")