from config.databases import db

def dataframe_to_dict(dataframe):
    """
    Permite convertir un dataframe a un
    diccionario de Python
    """
    
    # Convertir a dataframe
    data_dict = dataframe.to_dict("records")
    return(data_dict)

def verify_user_existence(id_user : str):
    user = db.users.find_one({"id_user" : id_user}, {"_id" : 0})
    if user is not None:
        return(True)
    else:
        return(False)