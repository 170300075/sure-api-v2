######################################
#           Bibliotecas              #
######################################
from fastapi import FastAPI

######################################
#           Importamos los routers   #                
######################################

######################################
#           Descripción de la API    #                
######################################
from routes.users import users
from routes.webscrapers import webscrapers
from routes.webdriver import webdriver

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
#      Añadir los routers a la API   #                
######################################
app.include_router(users)
app.include_router(webscrapers)
app.include_router(webdriver)