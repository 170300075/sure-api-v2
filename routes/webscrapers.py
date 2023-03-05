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

from config.webscrapers import personal_information
from config.webscrapers import mean_grades, grades
from config.webscrapers import academic_offer
from config.webscrapers import payments
from config.webscrapers import internships_offer
# from config.webscrapers import services_offer

######################################
#           Modelos                  #
######################################
from models.users import User
from models.grades import Grades
from models.payments import PaymentsList
from models.academic_offer import AcademicOffer

# Inicializar la variable global
driver = None

webscrapers = APIRouter(
    tags = ["Webscrapers"],
    prefix = "/webscrapers"
)

@webscrapers.post("/open", status_code = 200)
def initialize_webdriver(debug : bool | None = None):
    global driver
    # Opciones para el webdriver
    options = webdriver.ChromeOptions()

    if debug == True:
        options.add_argument("--headless")

    # Iniciar sesión del navegador
    driver = webdriver.Chrome(options = options)

@webscrapers.delete("/close", status_code = 200)
def close_webdriver():
    global driver

    # Cerrar la sesión
    driver.quit()

@webscrapers.post("/sigmaa/login", status_code = 200)
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

@webscrapers.get("/user_info", response_model = User)
def get_user_info(id_user : str, password : str):
    """
    Permite recuperar la información personal del
    estudiante directamente del sigmaa
    """
    global driver
    # Obtener la información personal del estudiante
    data = personal_information(driver, id_user, password)

    return(data)
    

@webscrapers.get("/payments_info", response_model = PaymentsList, status_code = 201)
def get_payments_info(id_user : str):
    """
    Permite recuperar la información de los pagos
    del estudiante y almacenar los PDF con las referencias
    de pago para el banco 
    """
    global driver
    # Obtener la información de los pagos
    data = payments(driver, id_user)

    return(data)

@webscrapers.get("/grades_info", response_model = Grades, status_code = 201)
def get_grades_info(id_user : str):
    """
    Permite recuperar la información de las 
    calificaciones en los periodos escolares disponibles
    """
    global driver
    # Obtener las boletas de calificaciones
    data = grades(driver, id_user)

    return(data)

@webscrapers.get("/academic_offer_info", response_model = AcademicOffer, status_code = 201)
def get_academic_offer_info(id_career : str, career : str):
    """
    Permite recuperar la lista de asignaturas disponibles
    en la oferta curricular del SIGMAA.
    """
    global driver
    # Obtener la oferta académica
    data = academic_offer(driver, id_career, career)

    return(data)

@webscrapers.delete("/sigmaa/logout", status_code = 200)
def logout_from_sigmaa():
    """
    Permite cerrar la sesión de usuario del SIGMAA
    """
    global driver
    # Cerrar la sesión de usuario existente
    logout_sigmaa(driver)

@webscrapers.post("/sipp/login", status_code = 200)
def login_into_sipp(id_user : str, password : str):
    """
    Permite iniciar sesión en el Sistema Integral de
    Prácticas Profesionales usando las credenciales del
    estudiante que se envian en el body del request
    """
    global driver
    login_sipp(driver, id_user, password)

@webscrapers.get("/internships_info", status_code = 201)
def get_internships_offer_info():
    """
    Permite recuperar las listas de empresas ofertadas
    para realizar las prácticas profesionales correspondientes
    a las claves de asignaturas disponibles para el estudiante
    """
    # Obtener la oferta de prácticas profesionales
    data = internships_offer(driver, "IDEIO")

    return(data)

@webscrapers.delete("/sipp/logout", status_code = 200)
def logout_from_sipp():
    """
    Permite cerrar la sesión de usuario del SIPP
    """
    global driver
    logout_sipp(driver)

@webscrapers.post("/sass/login", status_code = 200)
def login_into_sass(id_user : str, password : str):
    """
    Permite iniciar sesión en el Sistema Automatizado de
    Servicio Social usando las credenciales del estudiante
    que se envian en el body del request
    """
    global driver
    login_sass(driver, id_user, password)

@webscrapers.get("/social_service_info", status_code = 201)
def get_social_service_info():
    """
    Permite recuperar la oferta de instituciones y empresas 
    disponibles para realizar el servicio social
    """
    # Obtener la oferta de servicio social
    data = services_offer()

    return(data)

@webscrapers.delete("/sass/logout", status_code = 200)
def logout_from_sass():
    """
    Permite cerrar la sesión de usuario del SASS
    """
    global driver
    logout_sass(driver)