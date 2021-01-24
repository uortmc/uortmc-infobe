
from ..etc.dict_util import DictUtils as util
class SystemAuthDTO:
    @staticmethod
    def status(status:bool)->dict:
        return {"status":status}
    @staticmethod
    def loginAction(status:bool)->dict:
        return util.merge(
                SystemAuthDTO.status(status),
                {"action": "LoginAction"})
    @staticmethod
    def loginSuccess()->dict:
        return SystemAuthDTO.loginAction(True)

    @staticmethod
    def loginFailed(reason: str) -> dict:
        return util.merge(
                SystemAuthDTO.loginAction(False),
                {"reason": reason})

    @staticmethod
    def loginFailedWithException(exception: Exception) -> dict:
        return util.merge(
                SystemAuthDTO.loginAction(False),
                {"reason": str(exception)})

    @staticmethod
    def signUpAction(status: bool) -> dict:
        return util.merge(
                SystemAuthDTO.status(status),
                {"action": "SignUpAction"})
    @staticmethod
    def signupSuccess() -> dict:
        return SystemAuthDTO.signUpAction(True)

    @staticmethod
    def signUpFailed(reason: str) -> dict:
        return util.merge(
                SystemAuthDTO.signUpAction(False),
                {"reason": reason})

    @staticmethod
    def signUpFailedWithException(exception: Exception) -> dict:
        return util.merge(
                SystemAuthDTO.signUpAction(False),
                {"reason": str(exception)})