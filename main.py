######################################
#           Bibliotecas              #
######################################
from fastapi import FastAPI
import pandas as pd
import numpy as np

from selenium import webdriver

######################################
#           Dependencias             #
######################################
from config.utilities import dataframe_to_dict
from config.databases import client, db

######################################
#           Importamos los routers   #                
######################################
from routes.users import users
from routes.grades import grades
from routes.schedules import schedules
from routes.payments import payments
from routes.careers import careers
from routes.academic_offer import offer
from routes.drafts import drafts
from routes.internships import internships
from routes.services import services
from routes.calendars import calendars
from routes.webscrapers import webscrapers

######################################
#           Descripción de la API    #                
######################################
description = """
SURE API ayuda a obtener información para la SURE APP. 
Todos los cálculos se han realizado desde los diferentes endpoints
por lo que en muchos casos, solo será necesario consultar esta información
directamente desde algún endpoint.

SURE API está desarrollado para hacer cosas maravillosas 🚀.
Hecho con ❤ por Kenneth a.k.a BlackMaster (170300075).
"""

######################################
#         Definir instancia de API   #                
######################################
app = FastAPI(
    title = "SURE API",
    version = "1.0.0",
    description = description,
    contact = {
        "name" : "Kenneth Díaz González",
        "email" : "kennethdiazgonzalez@hotmail.com"
    }
)

######################################
#      Procesos startup and shudown  #                
######################################
@app.on_event("startup")
def startup_event():
    print(mongodb_uri)

@app.on_event("shutdown")
def shutdown_event():
    client.close()

######################################
#      Añadir los routers a la API   #                
######################################
app.include_router(users)
app.include_router(grades)
app.include_router(schedules)
app.include_router(payments)
app.include_router(careers)
app.include_router(offer)
app.include_router(drafts)
app.include_router(internships)
app.include_router(services)
app.include_router(calendars)
app.include_router(webscrapers)