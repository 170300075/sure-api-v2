######################################
#           Bibliotecas              #
######################################
import pymongo
from pymongo import MongoClient

# Importar variables de ambiente
from config.envs import mongodb_uri

def open_database(string_connection):
    # Crear una conexión a la base de datos
    client = MongoClient(mongodb_uri)
    return(client)

def close_database(client):
    client.close()

# Abrir una conexión con la base de datos
client = open_database(mongodb_uri)

# Crear una conexión a la colección de datos 
db = client.sure