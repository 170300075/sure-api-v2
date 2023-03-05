######################################
#           Bibliotecas              #
######################################
from fastapi import APIRouter, HTTPException

######################################
#           Dependencias             #
######################################
from config.utilities import dataframe_to_dict
from config.databases import db
from config.utilities import verify_user_existence

######################################
#           Modelos                  #
######################################
from models.users import User

users = APIRouter(
    tags = ["Usuarios"],
    prefix = "/users"
)

@users.get("", response_model = list[User])
def get_user(id_user : str | None = None):
    """
    Regresa la información de un estudiante 
    o de todos aquellos que estén registrados.
    """
    # Si se consulta para todos los usuarios
    if id_user == None:
        data = list(db.users.find({}, {"_id" : 0}))
    # Si se consulta para un usuario especifico
    else:
        data = [db.users.find_one({"id_user" : id_user}, {"_id" : 0})]

    if len(data) > 0 and None not in data: 
        return(data)
    else:
        raise HTTPException(status_code = 404, detail = "User(s) not found")

@users.post("/create", status_code = 201)
def create_user(user : User):
    """
    Crea un nuevo usuario en la base de datos 
    a partir de la información pasada en el body
    """
    # Verificar la existencia del usuario
    found_user = verify_user_existence(user.id_user)

    # Si el usuario no existe
    if found_user == False:
        # Crear un nuevo usuario 
        identifier = db.users.insert_one(user.dict())

    # El usuario ya existe
    else:
        # Lanzar una excepción
        raise HTTPException(status_code = 400, detail = f"User {user.id_user} already exists")

@users.put("/edit", status_code = 200)
def edit_user(user : User):
    """
    Modifica la información de un usuario existente
    """
    # Verifica la existencia del usuario
    found_user = verify_user_existence(user.id_user)

    # Si el usuario existe
    if found_user == True:
        # Reemplazar la información de usuario en la base de datos
        db.users.replace_one({"id_user" : user.id_user}, user.dict())
    
    # Si el usuario no existe
    else:
        # Lanzar una excepción
        raise HTTPException(status_code = 404, detail = f"User {user.id_user} doesn't exists")

@users.delete("/delete", status_code = 200)
def delete_user(id_user : str, mode : str | None = None):
    """
    Elimina un usuario registrado en la base de datos
    """
    # Obtener los datos del usuario a partir de su matricula
    found_user = verify_user_existence(id_user)
    
    # Si el usuario existe
    if found_user == True:
        # Si es un hard delete
        if mode == "hard":
            # Eliminar la cuenta del usuario permanentemente
            db.users.delete_one({"id_user" : id_user})

        # Si es un soft delete
        elif mode == "soft" or mode is None:
            # Recuperar la información del usuario
            user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})
            # Cambiar el estado de la cuenta a desactivada
            user["career"]["status"] = "deactivated"

            # Guardar los cambios de activación de la cuenta
            db.users.replace_one({"id_user" : id_user}, user, upsert = True)
        
        # Si es un modo que no existe
        else:
            raise HTTPException(status_code = 400, detail = f"Mode {mode} not valid")
    # Si el usuario no existe
    else: 
        raise HTTPException(status_code = 400, detail = f"User {id_user} doesn't exists")
