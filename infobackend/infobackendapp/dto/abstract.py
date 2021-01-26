from ..etc.dict_util import DictUtils as util
class AbstractDTO:
    def __init__(self,handlerName:str):
        self.handlerName=handlerName

    def status(self,status: bool) -> dict:
        return {
            "complete": status,
            "handler":self.handlerName
        }
    def fail(self,reason:str):
        return util.merge(
                self.status(False),
                {'reason':reason})

    def success(self):
        return self.status(True)

    def successWithResponce(self,responce:dict):
        return util.merge(self.success(),
                    {"responce":responce})
