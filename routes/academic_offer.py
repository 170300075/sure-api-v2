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

offer = APIRouter(
    tags = ["Oferta académica"],
    prefix = "/academic_offer"
)

@offer.get("")
def get_academic_offer(id_user : str, mode : str = None):
    """
    Permite consultar la oferta académica a partir
    de modificadores pasados como argumentos
    """
    # Verificar la existencia del usuario
    user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})

    # Si el usuario existe
    if user is not None:
        # Obtener el programa educativo del estudiante
        id_career = user["career"]["id_career"]

        # Si se necesita consultar la oferta completa
        if mode in [None, "all"]:
            # Consultar la oferta academica de la carrera
            offer = db.academic_offer.find_one({})
        # Si se requieren las asignaturas que le faltan por acreditar
        # al estudiante
        elif mode == "student":
            # Consultar la oferta completa
            offer = db.academic_offer.find_one({})

            # Filtrar las asignaturas por acreditar para el estudiante
            # ...
        # Si se necesita consultar la oferta con las asignaturas obligatorias
        # ofertadas en el último periodo escolar
        elif mode == "mandatory":
            # Consultar la oferta completa
            offer = db.academic_offer.find_one({})

            # Filtrar las asignaturas obligatorias de la oferta
            # ...
        else:
            raise HTTPException(status_code = 400, detail = f"{mode} is not a valid mode")
        
        return(offer)
    # Si no existe el usuario
    else:
        # Lanzar error de usuario no encontrado
        raise HTTPException(status_code = 404, detail = f"User {id_user} not found")
    

@offer.post("/create")
def create_academic_offer():
    """
    Permite crear una nueva oferta académica
    para un programa educativo.
    """
    return "Hello world"

@offer.put("/edit")
def edit_academic_offer():
    """
    Permite editar una oferta académica existente 
    de un programa educativo.
    """
    return "Hello world"

@offer.delete("/delete")
def delete_academic_offer():
    """
    Permite eliminar la oferta académica de un
    periodo especificado en un programa educativo.
    """
    return "Hello world"