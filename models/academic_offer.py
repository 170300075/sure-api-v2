from pydantic import BaseModel
from datetime import datetime

class OfferedSubject(BaseModel):
    type : str
    id_subject : str
    section : int
    modality : str
    subject : str
    teacher : str
    monday : str
    tuesday : str
    wednesday : str
    thursday : str
    friday : str
    saturday : str

class AcademicOffer(BaseModel):
    id_career : str
    career : str
    title : str
    additionals : list[OfferedSubject]
    workshops : list[OfferedSubject]
    foreign_languages : list[OfferedSubject]
    last_updated : datetime