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
    first_partial : int | str
    second_partial : int | str
    third_partial : int | str
    mean : float | str
    final_grade : float | str

class Period(BaseModel):
    mean : float | str
    grades : list[SubjectGrades]

class Periods(BaseModel):
    period : Period

class Grades(BaseModel):
    id_user : str
    periods : Periods
    last_updated : datetime