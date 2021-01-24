

class SystemAuthDTO:
    @staticmethod
    def status(status:bool)->dict:
        return {status:status}
    @staticmethod
    def loginAction(status:bool)->dict:
        return SystemAuthDTO.status(status) | \
               {"action": "LoginAction"}
    @staticmethod
    def loginSuccess()->dict:
        return SystemAuthDTO.loginAction(True)

    @staticmethod
    def loginFailed(reason: str) -> dict:
        return SystemAuthDTO.loginAction(False) | \
               {"reason": reason}

    @staticmethod
    def loginFailedWithException(exception: Exception) -> dict:
        return SystemAuthDTO.loginAction(False) | \
               {"reason": str(exception)}