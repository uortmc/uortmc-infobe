

from .authenticatedDto import AuthenticatedDTO
from ..etc.dict_util import DictUtils as util
from ..models import Patient,Doctor
from ..serializer.doctor import DoctorSerializer
from ..serializer.patient import PatientSerializer
from ..serializer.scan import ScanSerializer


class ScanDTO(AuthenticatedDTO):
    def __init__(self,handlerName:str):
        super(ScanDTO, self).__init__(handlerName)

    def successGetScans(self, scans:list)->dict:
        return self.successWithResponce(
            [ScanSerializer.toDict(x) for x in scans]
        )


