from ..models import Scan


class ScanComplete:
    @staticmethod
    def build(scan:Scan)->str:
        return "Scan "+str(scan.token).split("-")[0]+" of Patient "+scan.ascPatient.first_name+" "+scan.ascPatient.last_name+" Completed"