from .abstract import AbstractDTO
from ..etc.dict_util import DictUtils as util
class DoctorDTO(AbstractDTO):
    def __init__(self):
        super(DoctorDTO, self).__init__("DoctorInfo")


