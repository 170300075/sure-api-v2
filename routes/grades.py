######################################
#           Bibliotecas              #
######################################
from fastapi import APIRouter, HTTPException

######################################
#           Dependencias             #
######################################
from config.utilities import dataframe_to_dict
from config.databases import db
from config.utilities import get, post

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

@grades.get("")#, response_model = Grades)
def get_user_grades(id_user : str, period : str | None = None):
    """
    Permite obtener las calificaciones del estudiante 
    en todos los periodos o en uno especifico.
    """
    found_user = verify_user_existence(id_user)
    # Si se el usuario existe
    if found_user == True:
        # Si el periodo se especifica
        if period is not None:
            # Obtener la lista de calificaciones del periodo especificado del estudiante
            user_grades = db.grades.find_one({"id_user" : id_user, "periods" : period}, {"_id" : 0})
        # Si el periodo no se especifica
        else:
            # Obtener la lista general de calificaciones del estudiante
            user_grades = list(db.grades.find({"id_user" : id_user}, {"_id" : 0}))
        
        # Si existen resultados
        if len(user_grades) > 0 and None not in user_grades:
            return(user_grades)
        else:
            raise HTTPException(status_code = 404, detail = f"Grades not found for user {id_user}")

@grades.post("/create", status_code = 201)
def create_user_grades(grades : Grades):
    found_user = verify_user_existence(grades.id_user)
    if found_user == True:
        inserted_id = db.grades.insert_one({"id_user" : grades.id_user}, grades.dict())
    else:
        raise HTTPException(status_code = 404, detail = f"User {grades.id_user} doesn't exists")

@grades.put("/edit")
def edit_user_grades(grades : Grades):
    """
    Permite editar las calificaciones del estudiantes
    en un periodo especificado.
    """
    found_user = verify_user_existence(grades.id_user)
    if found_user == True:
        inserted_id = db.grades.replace_one({"id_user" : grades.id_user}, grades.dict())
    else:
        raise HTTPException(status_code = 404, detail = f"User {grades.id_user} doesn't exists")


@grades.delete("/delete")
def delete_user_grades(id_user):
    """
    Permite eliminar los registros de calificaciones
    de un estudiante especificado.
    """
    found_user = verify_user_existence(id_user)
    if found_user == True:
        db.grades.delete_one({"id_user" : id_user})
    else:
        raise HTTPException(status_code = 404, detail = f"User {id_user} doesn't exists")
    