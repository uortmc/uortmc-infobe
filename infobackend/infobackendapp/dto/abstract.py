from ..etc.dict_util import DictUtils as util
class AbstractDTO:
    def __init__(self,action):
        self.action=action

    def status(self,status: bool) -> dict:
        return {
            "complete": status,
            "action":self.action
        }
    def fail(self):
        return self.status(False)

    def success(self):
        return self.status(True)
