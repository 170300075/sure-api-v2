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
# from models.users import User

webdriver = APIRouter(
    tags = ["Webdriver"],
    prefix = "/webdriver"
)

@webdriver.post("/sigmaa/login", status_code = 200)
def login_into_sigmaa(id_user : str, password : str):
    """
    Permite iniciar sesión en una cuenta de SIGMAA
    usando las credenciales del estudiante que se 
    envian en el body del request
    """

@webdriver.get("/sigmaa/logout", status_code = 200)
def logout_from_sigmaa():
    """
    Permite cerrar la sesión de usuario del SIGMAA
    """

@webdriver.post("/sipp/login", status_code = 200)
def login_into_sipp(id_user : str, password : str):
    """
    Permite iniciar sesión en el Sistema Integral de
    Prácticas Profesionales usando las credenciales del
    estudiante que se envian en el body del request
    """

@webdriver.get("/sipp/logout", status_code = 200)
def logout_from_sipp():
    """
    Permite cerrar la sesión de usuario del SIPP
    """

@webdriver.post("/sass/login", status_code = 200)
def login_into_sass(id_user : str, password : str):
    """
    Permite iniciar sesión en el Sistema Automatizado de
    Servicio Social usando las credenciales del estudiante
    que se envian en el body del request
    """

@webdriver.get("/sass/logout", status_code = 200)
def logout_from_sass():
    """
    Permite cerrar la sesión de usuario del SASS
    """