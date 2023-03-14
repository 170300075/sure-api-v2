######################################
#           Bibliotecas              #
######################################
import requests
import json

######################################
#           Dependencias             #
######################################
from config.databases import db

def dataframe_to_dict(dataframe):
    """
    Permite convertir un dataframe a un
    diccionario de Python
    """
    
    # Convertir a dataframe
    data_dict = dataframe.to_dict("records")
    return(data_dict)

def verify_user_existence(id_user : str):
    user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})
    if user is not None:
        return(True)
    else:
        return(False)

def get(url : str, payload : dict | None = None):
    if payload is not None:
        res = requests.get(url = url, params = payload)
    else:
        res = requests.get(url = url)
    return(res)

def post(url : str, payload : dict | None = None, body : dict | None = None):
    if payload is not None:
        res = requests.post(url = url, params = payload)
    elif body is not None:
        res = requests.post(url = url, data = json.dumps(body))
    else:
        res = requests.post(url = url)
    return(res)

def put(url : str, payload : dict | None = None):
    if payload is not None:
        res = requests.put(url = url, params = payload)
    else:
        res = requests.put(url = url)
    return(res)

def delete(url : str, payload : dict | None = None):
    if payload is not None:
        res = requests.delete(url = url, params = payload)
    else:
        res = requests.delete(url)
    return(res)