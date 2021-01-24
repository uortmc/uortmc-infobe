
class SystemAuthException(Exception):
    def __init__(self ,reason :str):
        self.reason =reason
    def __str__(self):
        return "SystemAuthException: " +self.reason
