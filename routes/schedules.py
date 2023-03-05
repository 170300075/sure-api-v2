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

schedules = APIRouter(
    tags = ["Horarios"],
    prefix = "/schedules"
)

@schedules.get("")
def get_schedules():
    """
    Permite consultar los horarios del estudiante.
    """

@schedules.post("/create")
def create_schedules():
    """
    Permite crear un horario para un estudiante.
    """

@schedules.put("/edit")
def edit_schedules():
    """
    Permite editar un horario existente del estudiante.
    """

@schedules.delete("/delete")
def delete_schedules():
    """
    Permite eliminar un horario del estudiante.
    """