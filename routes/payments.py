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

payments = APIRouter(
    tags = ["Pagos"],
    prefix = "/payments"
)

@payments.get("")
def get_payments(id_user : str, mode : str = None):
    """
    Permite consultar la lista de adeudos y pagos
    efectuados por el estudiante a lo largo de su carrera
    """
    user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})

    if user is not None:
        if mode in [None, "all"]:
            payments = db.payments.find_one({"id_user" : id_user}, {"_id" : 0})
        elif mode == "billed":
            payments = db.payments.find_one({"id_user" : id_user}, {"_id" : 0})
        elif mode == "debt":
            payments = db.payments.find_one({"id_user" : id_user}, {"_id" : 0})
        else:
            raise HTTPException(status_code = 400, detail = f"{mode} is not a valid mode")

        return(payments)
    else:
        raise HTTPException(status_code = 404, detail = f"User {id_user} not found")
    
@payments.post("/create")
def create_payments():
    """
    Permite crear un nuevo registro de adeudos y pagos 
    de un estudiante.
    """
    return "Hello world!"

@payments.put("/edit")
def edit_payments():
    """
    Permite editar el registro de adeudos y pagos 
    de un estudiante
    """
    return "Hello world!"

@payments.delete("/delete")
def delete_payments():
    """
    Permite eliminar el registro de adeudos y pagos
    de un estudiante.
    """
    return "Hello world!"