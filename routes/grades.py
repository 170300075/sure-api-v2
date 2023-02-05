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
from models.grades import Grades

grades = APIRouter(
    tags = ["Calificaciones"],
    prefix = "/grades"
)

@grades.get("", response_model = Grades)
def get_user_grades(id_user : str, period : str = None):
    """
    Permite obtener las calificaciones del estudiante 
    en todos los periodos o en uno especifico.
    """

    user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})

    if user is not None:
        my_grades = db.users.find_one({"id_user" : id_user, "periods" : period}, {"_id" : 0})
        if my_grades is not None:
            return(my_grades)