######################################
#           Bibliotecas              #
######################################
import pymongo
from pymongo import MongoClient

# Importar variables de ambiente
from config.envs import mongodb_uri

# Crear una conexión a la base de datos
client = MongoClient(mongodb_uri)
# Crear una conexión a la colección de datos 
db = client.sure