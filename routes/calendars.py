######################################
#           Bibliotecas              #
######################################
from fastapi import APIRouter, HTTPException

######################################
#           Dependencias             #
######################################
from config.utilities import dataframe_to_dict
from config.databases import db

######################################
#           Modelos                  #
######################################
from models.users import User

calendars = APIRouter(
    tags = ["Calendarios"],
    prefix = "/calendars"
)

@calendars.get("")
def get_calendars():
    return "Hello world!"

@calendars.post("/create")
def create_calendar():
    return "Hello world!"

@calendars.put("/edit")
def edit_calendar():
    return "Hello world!"

@calendars.delete("/delete")
def delete_calendar():
    return "Hello world!"