######################################
#           Bibliotecas              #
######################################
from pydantic import BaseModel
from datetime import datetime

class Birthplace(BaseModel):
    country : str
    state : str
    city : str

class Relatives(BaseModel):
    first_relative : str
    second_relative : str
    relatives_marital_status : str

class Highschool(BaseModel):
    country : str
    state : str
    region : str
    city : str
    school_name : str
    campus : str
    school_system : str

class Career(BaseModel):
    career_name : str
    situation : str
    status : str
    social_service : str
    study_plan : str
    department : str

class Job(BaseModel):
    status : str
    company : str
    address : str
    phone : str

class User(BaseModel):
    id_user : str
    password : str
    username : str
    first_lastname : str
    second_lastname : str
    profile_picture : str
    curp : str
    rfc : str
    nationality : str
    nss : str
    personal_phone : str
    home_phone : str
    marital_status : str
    personal_address : str
    birthplace : Birthplace
    relatives : Relatives
    highschool : Highschool
    career : Career
    job : Job
    last_updated : datetime