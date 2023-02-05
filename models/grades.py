######################################
#           Bibliotecas              #
######################################
from pydantic import BaseModel
from datetime import datetime

class SubjectGrades(BaseModel):
    number : int
    type : str
    section : int
    id_subject : str
    teacher : str
    modality : str
    subject : str
    first_partial : float | str
    second_partial : float | str
    third_partial : float | str
    mean : float | str
    final_grade : float | str

class Period(BaseModel):
    mean : float | str
    grades : list[SubjectGrades]

class Grades(BaseModel):
    id_user : str
    periods : dict[str, Period]
    last_updated : datetime