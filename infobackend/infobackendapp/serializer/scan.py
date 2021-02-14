from ..models import Scan
from ..serializer.patient import PatientSerializer


class ScanSerializer():
    @staticmethod
    def toDict(scan: Scan) -> dict:
        return {
            "ascPatient":PatientSerializer.toDict(scan.ascPatient),
            "token":scan.token,
            "created": scan.created,
            "status": scan.status,
            "comment":scan.comment
        }
