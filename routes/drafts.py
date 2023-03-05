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
from models.drafts import Draft

drafts = APIRouter(
    tags = ["Borradores"],
    prefix = "/drafts"
)

@drafts.get("", response_model = list[Draft])
def get_drafts(id_user : str, id_draft : str = None):
    """
    Permite recuperar los borradores con las asignaturas
    de las cargas curriculares guardadas por el estudiante
    """
    # Verificar la existencia del usuario
    user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})
    draft = None

    # Si el usuario existe
    if user is not None:
        # Si se consultan todos los borradores
        if id_draft is not None:
            # Obtener todos los borradores disponibles
            draft = list(db.drafts.find({"id_user" : id_user}, {"_id" : 0}))

        # Si se consulta un borrador por id
        else:
            # Obtener el borrador por su ID
            draft = db.drafts.find_one({"id_user" : id_user, "id_draft" : id_draft}, {"_id" : 0})
    
        # Si se encontraron borradores
        if draft is not None:
            return(draft)
        # Si no se encontraron borradores disponibles
        else:
            raise HTTPException(status_code = 404, detail = f"Draft(s) not found")
    else:
        raise HTTPException(status_code = 404, detail = f"User {id_user} not found")

@drafts.post("/create")
def create_draft(id_user : str, my_draft: Draft):
    """
    Permite guardar un borrador curricular en
    la base de datos para su posterior consulta
    """
    # Verificar la existencia del usuario
    user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})

    # Si el usuario existe
    if user is not None:
        inserted_id = db.drafts.insert_one({"id_user" : id_user}, my_draft)
    else:
        raise HTTPException(status_code = 404, detail = f"User {id_user} not found")
    
@drafts.put("/edit")
def edit_draft():
    """
    Permite editar un borrador curricular existente
    """
    return "Hello world!"

@drafts.delete("/delete")
def delete_draft():
    """
    Permite eliminar un borrador curricular existente
    """
    return "Hello world!"