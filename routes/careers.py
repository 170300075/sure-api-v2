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

careers = APIRouter(
    tags = ["Licenciaturas"],
    prefix = "/careers"
)

@careers.get("")
def get_careers():
    return "Hello world!"

@careers.post("/create")
def create_career():
    return "Hello world!"

@careers.put("/edit")
def edit_career():
    return "Hello world!"

@careers.delete("/delete")
def delete_career():
    return "Hello world!"