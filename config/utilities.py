def dataframe_to_dict(dataframe):
    """
    Permite convertir un dataframe a un
    diccionario de Python
    """
    
    # Convertir a dataframe
    data_dict = dataframe.to_dict("records")
    return(data_dict)