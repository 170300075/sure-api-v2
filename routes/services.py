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

services = APIRouter(
    tags = ["Servicio social"],
    prefix = "/service"
)

@services.get("")
def get_social_service_offer():
    """
    Permite consultar la oferta de servicio social
    """
    return "Hello world!"

@services.post("/create")
def create_social_service_offer():
    """
    Permite crear una oferta de servicio social
    """
    return "Hello world!"

@services.put("/edit")
def edit_social_service_offer():
    """
    Permite editar una oferta de servicio social
    """
    return "Hello world!"

@services.delete("/delete")
def delete_social_service_offer():
    """
    Permite eliminar una oferta de servicio social
    """
    return "Hello world!"