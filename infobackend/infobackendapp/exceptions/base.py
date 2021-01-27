
class InfobeException(Exception):
    def __init__(self,reason:str):
        self.reason=reason

class FieldsMissingException(InfobeException):
    def __init__(self):
        super(FieldsMissingException,self).__init__("Bad request: Request without the necessary fields has being "
                                                    "raised.")
