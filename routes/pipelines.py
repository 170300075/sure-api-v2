######################################
#           Bibliotecas              #
######################################
from fastapi import APIRouter, HTTPException
from selenium import webdriver


######################################
#           Dependencias             #
######################################
from config.utilities import dataframe_to_dict
from config.databases import db

from config.webscrapers import login_sigmaa, logout_sigmaa
from config.webscrapers import login_sipp, logout_sipp
from config.webscrapers import login_sass, logout_sass

######################################
#           Modelos                  #
######################################
# from models.users import User

# Inicializar la variable global
driver = None

pipelines = APIRouter(
    tags = ["pipelines"],
    prefix = "/pipelines"
)

@pipelines.get("/open", status_code = 200)
def initialize_webdriver(debug : bool | None = None):
    global driver
    # Opciones para el webdriver
    options = webdriver.ChromeOptions()

    if debug == True:
        options.add_argument("--headless")

    # Iniciar sesión del navegador
    driver = webdriver.Chrome(options = options)

@pipelines.get("/close", status_code = 200)
def close_webdriver():
    global driver

    # Cerrar la sesión
    driver.quit()

@pipelines.post("/sigmaa/login", status_code = 200)
def login_into_sigmaa(id_user : str, password : str):
    """
    Permite iniciar sesión en una cuenta de SIGMAA
    usando las credenciales del estudiante
    """
    global driver
    # Si el inicio de sesión no pudo efectuarse
    if login_sigmaa(driver, id_user, password) == False:
        # Lanzar un error
        raise HTTPException(status_code = 400, 
        detail = "We couldn't connect to SIGMMA using these credentials")

@pipelines.get("/sigmaa/logout", status_code = 200)
def logout_from_sigmaa():
    """
    Permite cerrar la sesión de usuario del SIGMAA
    """
    # Cerrar la sesión de usuario existente
    logout_sigmaa()

@pipelines.post("/sipp/login", status_code = 200)
def login_into_sipp(id_user : str, password : str):
    """
    Permite iniciar sesión en el Sistema Integral de
    Prácticas Profesionales usando las credenciales del
    estudiante que se envian en el body del request
    """
    login_sipp(id_user, password)

@pipelines.get("/sipp/logout", status_code = 200)
def logout_from_sipp():
    """
    Permite cerrar la sesión de usuario del SIPP
    """
    logout_sipp()

@pipelines.post("/sass/login", status_code = 200)
def login_into_sass(id_user : str, password : str):
    """
    Permite iniciar sesión en el Sistema Automatizado de
    Servicio Social usando las credenciales del estudiante
    que se envian en el body del request
    """
    login_sass(id_user, password)

@pipelines.get("/sass/logout", status_code = 200)
def logout_from_sass():
    """
    Permite cerrar la sesión de usuario del SASS
    """
    logout_sass()