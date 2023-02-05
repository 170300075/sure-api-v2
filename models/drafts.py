######################################
#           Bibliotecas              #
######################################
from pydantic import BaseModel
from datetime import datetime

class Draft(BaseModel):
    subject : str
    teacher : str
    modality : str
    monday : str
    tuesday : str
    wednesday : str
    thursday : str
    friday : str
    saturday : str