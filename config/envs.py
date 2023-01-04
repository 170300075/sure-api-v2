######################################
#           Bibliotecas              #
######################################
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