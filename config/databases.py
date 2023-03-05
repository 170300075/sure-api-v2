######################################
#           Bibliotecas              #
######################################
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Recuperar variables de ambiente
load_dotenv("./config/.env")

# Cadena de conexión a base de datos
mongodb_uri = os.getenv("mongodb_uri")

# URL del root de la API
root_api = os.getenv("root_api")

# URL de la aplicación web
webapp_url = os.getenv("webapp_url")

def open_database(string_connection):
    # Crear una conexión a la base de datos
    client = MongoClient(string_connection)
    print("Connected to database: " + string_connection)
    return(client)

def close_database(client):
    client.close()
    print("Disconnected from database")

client = open_database(mongodb_uri)
db = client["sure"]