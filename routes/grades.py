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
from routes.users import verify_user_existence

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
        my_grades = db.grades.find_one({"id_user" : id_user, "periods" : period}, {"_id" : 0})
        if my_grades is not None:
            return(my_grades)
        
@grades.post("/create")
def create_user_grades(id_user : str, grades : Grades):
    user_exists = verify_user_existence(id_user)
    if user_exists == True:
        return("User created : test")
    else:
        return("User not created : test")

@grades.put("/edit")
def edit_user_grades():
    """
    Permite editar las calificaciones del estudiantes
    en un periodo especificado.
    """
    return "Hello world!"

@grades.delete("/delete")
def delete_user_grades():
    """
    Permite eliminar los registros de calificaciones
    de un estudiante especificado.
    """
    return "Hello world!"