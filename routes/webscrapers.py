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

webscrapers = APIRouter(
    tags = ["Webscrapers"],
    prefix = "/webscrapers"
)

@webscrapers.get("/user_info", response_model = list[User])
def get_user_info():
    """
    Permite recuperar la información personal del
    estudiante directamente del sigmaa
    """

@webscrapers.get("/payments_info", status_code = 201)
def get_payments_info():
    """
    Permite recuperar la información de los pagos
    del estudiante y almacenar los PDF con las referencias
    de pago para el banco 
    """

@webscrapers.get("/grades_info", status_code = 201)
def get_grades_info():
    """
    Permite recuperar la información de las 
    calificaciones en los periodos escolares disponibles
    """

@webscrapers.get("/academic_offer_info", status_code = 201)
def get_academic_offer_info():
    """
    Permite recuperar la lista de asignaturas disponibles
    en la oferta curricular del SIGMAA.
    """

@webscrapers.get("/practices_info", status_code = 201)
def get_practices_offer_info():
    """
    Permite recuperar las listas de empresas ofertadas
    para realizar las prácticas profesionales correspondientes
    a las claves de asignaturas disponibles para el estudiante
    """

@webscrapers.get("/social_service_info", status_code = 201)
def get_social_service_info():
    """
    Permite recuperar la oferta de instituciones y empresas 
    disponibles para realizar el servicio social
    """