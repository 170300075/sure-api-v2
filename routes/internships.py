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

internships = APIRouter(
    tags = ["Prácticas profesionales"],
    prefix = "/practices"
)

@internships.get("")
def get_intenships_offer():
    return "Hello world!"

@internships.post("/create")
def create_intenships_offer():
    return "Hello world!"

@internships.put("/edit")
def edit_intenships_offer():
    return "Hello world!"

@internships.delete("/delete")
def delete_intenships_offer():
    return "Hello world!"