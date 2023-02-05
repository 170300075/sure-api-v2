from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pandas as pd
import numpy as np
from datetime import datetime
import string
from lxml import etree
import pdfkit

from config.utilities import dataframe_to_dict

def xpath(driver, xpath : str):
    elements = driver.find_elements(By.XPATH, xpath)
    if len(elements) > 0:
        if len(elements) == 1:
            return(elements[0])
        else:
            return(elements)
    else:
        return("Elemento no encontrado")

def login_sigmaa(driver, id_user : str, password : str):
    """
    Permite iniciar sesion en el SIGMAA 
    usando las credenciales del estudiante
    
    Regresa `true` si el incio de sesión se pudo concretar
    Regresa `false` si no se pudo iniciar sesión
    """
    # Acceder al SIGMAA
    url = "https://uclb.ucaribe.edu.mx/sigmaav2/"
    driver.get(url)

    # Buscar el campo de usuario y escribir el username
    id_user_input = xpath(driver, "/html/body/div[2]/form/div/span[2]/input")
    id_user_input.clear()
    id_user_input.send_keys(id_user)
    
    # Buscar el campo de contraseña y escribir el password
    password_input = xpath(driver, "/html/body/div[2]/form/div/input")
    password_input.clear()
    password_input.send_keys(password)
    
    # Buscar el botón de submit y dar clic para iniciar sesión
    submit_input = driver.find_element(By.XPATH, "/html/body/div[2]/form/button")
    submit_input.click()

    # Si se intenta loguear pero se queda en la misma página de logueo
    if driver.title == "Ingresar · SIGMAA - Unicaribe":
        # Inicio de sesion erroneo
        return(False)
    else:
        # Inicio de sesion exitoso
        return(True)

def logout_sigmaa(driver):
    """
    Permite cerrar la sesión de un usuario en SIGMAA
    """
    # Encontrar el botón de cierre de sesión
    logout = xpath(driver, "/html/body/div[2]/div/form/a")
    # Clic para cerrar sesión
    logout.click()

def login_sipp(driver, id_user : str, password : str):
    # Acceder al SIPP
    url = "https://uclb.ucaribe.edu.mx/practicas/"
    driver.get(url)

    # Buscar el campo de usuario y escribir el username
    userinput = xpath(driver, "/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input")
    userinput.send_keys(id_user)

    # Buscar el campo de contraseña y escribir el password
    passinput = xpath(driver, "/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input")
    passinput.send_keys(password)
    # Buscar el botón de submit y dar clic para iniciar sesión
    submitinput = xpath(driver, "/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/input")
    submitinput.click()

def logout_sipp(driver):
    # Encontrar el botón de cierre de sesión
    logout = xpath(driver, "/html/body/div[3]/div/div/div[1]/ul/li[3]/a")
    # Clic para cerrar sesión
    logout.click()

def login_sass(driver, id_user : str, password : str):
    # Acceder al SASS
    url = "https://uclb.ucaribe.edu.mx/sass/"
    driver.get(url)

    # Buscar el campo de usuario y escribir el username
    userinput = xpath(driver, "/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input")
    userinput.send_keys(id_user)

    # Buscar el campo de contraseña y escribir el password
    passinput = xpath(driver, "/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input")
    passinput.send_keys(password)
    # Buscar el botón de submit y dar clic para iniciar sesión
    submitinput = xpath(driver, "/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/input")
    submitinput.click()


def logout_sass(driver):
    # Encontrar el botón de cierre de sesión
    logout = xpath(driver, "/html/body/div[3]/div/div/div[1]/ul/li[3]/a")
    # Clic para cerrar sesión
    logout.click()

def personal_information(driver, id_user : str, password : str):
    """
    Permite recuperar la información personal del estudiante
    en esa sección en SIGMAA
    """
    # Dirigirse a la sección de información personal
    personal_information_tab = xpath(driver, "/html/body/div[1]/div/div/div/div/div/ul[2]/li[6]/a")
    personal_information_tab.click()
    
    # Recuperar los datos de la tabla con la información
    # del estudiante
    df = pd.read_html(driver.page_source)
    # print(len(df))
    df = df[1]
    
    # Determinar si existen registros de beca
    scholarship = False if xpath(driver, "/html/body/center/table/tbody/tr[1]/th").text == "Datos personales" else True
    
    # Recuperar la información dependiendo de la estructura
    # de la página en donde se encuentran los datos
    if scholarship == True:
        username = xpath(driver, "/html/body/center/table/tbody/tr[6]/td[3]").text
        first_lastname = xpath(driver, "/html/body/center/table/tbody/tr[6]/td[1]").text
        second_lastname = xpath(driver, "/html/body/center/table/tbody/tr[6]/td[2]").text
        curp = xpath(driver, "/html/body/center/table/tbody/tr[7]/td[2]").text
        rfc = xpath(driver, "/html/body/center/table/tbody/tr[7]/td[1]").text
        nationality = xpath(driver, "/html/body/center/table/tbody/tr[8]/td[2]").text
        nss = xpath(driver, "/html/body/center/table/tbody/tr[9]/td[1]").text
        personal_email = xpath(driver, "/html/body/center/table/tbody/tr[9]/td[2]").text
        birthday = xpath(driver, "/html/body/center/table/tbody/tr[8]/td[3]").text
        sex = xpath(driver, "/html/body/center/table/tbody/tr[7]/td[3]").text
        personal_phone = xpath(driver, "/html/body/center/table/tbody/tr[11]/td[2]").text
        home_phone = xpath(driver, "/html/body/center/table/tbody/tr[11]/td[1]").text
        marital_status = Select(xpath(driver, "/html/body/center/table/tbody/tr[8]/td[1]/select")).first_selected_option.text
        personal_address = xpath(driver, "/html/body/center/table/tbody/tr[10]/td[1]").text
        birthplace_country = Select(xpath(driver, "/html/body/center/table/tbody/tr[16]/td/select")).first_selected_option.text
        birthplace_state = Select(xpath(driver, "//*[@id='uiNacEstado']/select")).first_selected_option.text
        birthplace_city = Select(xpath(driver, "//*[@id='uiNacCiudad']/select")).first_selected_option.text
        first_relative = xpath(driver, "/html/body/center/table/tbody/tr[14]/td[1]").text
        second_relative = xpath(driver, "/html/body/center/table/tbody/tr[14]/td[2]").text
        relatives_marital_status = Select(xpath(driver, "/html/body/center/table/tbody/tr[14]/th[4]/select")).first_selected_option.text
        highschool_country = Select(xpath(driver, "/html/body/center/table/tbody/tr[20]/td/select")).first_selected_option.text
        highschool_state = Select(xpath(driver, "//*[@id='uiEscEstado']/select")).first_selected_option.text
        highschool_region = xpath(driver, "/html/body/center/table/tbody/tr[22]/td[1]").text
        highschool_city = xpath(driver, "/html/body/center/table/tbody/tr[22]/td[2]").text
        highschool_name = xpath(driver, "/html/body/center/table/tbody/tr[23]/td").text
        highschool_campus = xpath(driver, "/html/body/center/table/tbody/tr[24]/td[1]").text
        school_system = xpath(driver, "/html/body/center/table/tbody/tr[24]/td[2]").text
        working_status = xpath(driver, "/html/body/center/table/tbody/tr[12]/td[1]").text
        company_name = xpath(driver, "/html/body/center/table/tbody/tr[12]/td[2]").text
        company_address = xpath(driver, "/html/body/center/table/tbody/tr[12]/td[3]").text
        company_phone = xpath(driver, "/html/body/center/table/tbody/tr[11]/td[3]").text
    
    else:
        username = xpath(driver, "/html/body/center/table/tbody/tr[2]/td[3]").text
        first_lastname = xpath(driver, "/html/body/center/table/tbody/tr[2]/td[1]").text
        second_lastname = xpath(driver, "/html/body/center/table/tbody/tr[2]/td[2]").text
        curp = xpath(driver, "/html/body/center/table/tbody/tr[3]/td[2]").text
        rfc = xpath(driver, "/html/body/center/table/tbody/tr[3]/td[1]").text
        nationality = xpath(driver, "/html/body/center/table/tbody/tr[4]/td[2]").text
        nss = xpath(driver, "/html/body/center/table/tbody/tr[5]/td[1]").text
        personal_email = xpath(driver, "/html/body/center/table/tbody/tr[5]/td[2]").text
        birthday = xpath(driver, "/html/body/center/table/tbody/tr[4]/td[3]").text
        sex = xpath(driver, "/html/body/center/table/tbody/tr[3]/td[3]").text
        personal_phone = xpath(driver, "/html/body/center/table/tbody/tr[7]/td[2]").text
        home_phone = xpath(driver, "/html/body/center/table/tbody/tr[7]/td[1]").text
        marital_status = Select(xpath(driver, "/html/body/center/table/tbody/tr[4]/td[1]/select")).first_selected_option.text
        personal_address = xpath(driver, "/html/body/center/table/tbody/tr[6]/td[1]").text
        birthplace_country = Select(xpath(driver, "/html/body/center/table/tbody/tr[12]/td/select")).first_selected_option.text
        birthplace_state = Select(xpath(driver, "//*[@id='uiNacEstado']/select")).first_selected_option.text
        birthplace_city = Select(xpath(driver, "//*[@id='uiNacCiudad']/select")).first_selected_option.text
        first_relative = xpath(driver, "/html/body/center/table/tbody/tr[10]/td[1]").text
        second_relative = xpath(driver, "/html/body/center/table/tbody/tr[10]/td[2]").text
        relatives_marital_status = Select(xpath(driver, "/html/body/center/table/tbody/tr[10]/th[4]/select")).first_selected_option.text
        highschool_country = Select(xpath(driver, "/html/body/center/table/tbody/tr[16]/td/select")).first_selected_option.text
        highschool_state = Select(xpath(driver, "//*[@id='uiEscEstado']/select")).first_selected_option.text
        highschool_region = xpath(driver, "/html/body/center/table/tbody/tr[18]/td[1]").text
        highschool_city = xpath(driver, "/html/body/center/table/tbody/tr[18]/td[2]").text
        highschool_name = xpath(driver, "/html/body/center/table/tbody/tr[19]/td").text
        highschool_campus = xpath(driver, "/html/body/center/table/tbody/tr[20]/td[1]").text
        school_system = xpath(driver, "/html/body/center/table/tbody/tr[20]/td[2]").text
        working_status = xpath(driver, "/html/body/center/table/tbody/tr[8]/td[1]").text
        company_name = xpath(driver, "/html/body/center/table/tbody/tr[8]/td[2]").text
        company_address = xpath(driver, "/html/body/center/table/tbody/tr[8]/td[3]").text
        company_phone = xpath(driver, "/html/body/center/table/tbody/tr[7]/td[3]").text
        
    # Dirigirse a la seccion de la boleta escolar
    grades_tab = xpath(driver, "/html/body/div[1]/div/div/div/div/div/ul[2]/li[4]/a")
    grades_tab.click()
    
    # Recuperar la información de la carrera
    career_name = xpath(driver, "/html/body/center/table[1]/tbody/tr[2]/td").text.split(" / ")[1]
    situation = xpath(driver, "/html/body/center/table[1]/tbody/tr[3]/td").text
    status = xpath(driver, "/html/body/center/table[1]/tbody/tr[4]/td").text
    social_service = xpath(driver, "/html/body/center/table[1]/tbody/tr[6]/td").text
    id_career = xpath(driver, "/html/body/center/table[1]/tbody/tr[2]/td").text.split(" / ")[0]
    
    # Obtener el departamento de acuerdo a la carrera
    department = "Ciencias Básicas e Ingenierías"
    
    personal_information = {
        # Información personal básica
        "id_user" : id_user,
        "password" : password,
        "username" : string.capwords(username),
        "first_lastname" : string.capwords(first_lastname),
        "second_lastname" : string.capwords(second_lastname),
        "profile_picture" : "default_avatar.jpg",
        "curp" : curp,
        "rfc" : rfc,
        "nationality" : nationality,
        "nss" : nss,
        "personal_email" : personal_email.lower(),
        "birthday" : datetime.strptime(birthday,"%Y-%m-%d"),
        "sex" : sex,
        "personal_phone" : personal_phone,
        "home_phone" : home_phone,
        "marital_status" : marital_status,
        "personal_address" : personal_address.title(),
        
        # Información de nacimiento
        "birthplace" : {
            "country" : birthplace_country.capitalize(),
            "state" : birthplace_state,
            "city" : birthplace_city
        },
        
        # Información de familiares
        "relatives" : {
            "first_relative" : first_relative.title(),
            "second_relative" : second_relative.title(),
            "relatives_marital_status" : relatives_marital_status
        },
        
        # Información de la escuela de procedencia
        "highschool" : {
            "country" : highschool_country.capitalize(),
            "state" : highschool_state,
            "region" : highschool_region,
            "city" : highschool_city,
            "school_name" : highschool_name,
            "campus" : highschool_campus,
            "school_system" : school_system 
        },
        
        # Información de la carrera
        "career" : {
            "career_name" : career_name,
            "situation" : situation,
            "status" : status,
            "social_service" : social_service,
            "id_career" : id_career,
            "department" : department
        },
        
        # Información laboral (IMPORTANTE)
        "job" : {
            "status" : working_status,
            "company" : company_name,
            "address" : company_address,
            "phone" : company_phone
        },
        
        # Última fecha de actualización
        "last_updated" : datetime.utcnow()
    }
    
    return(personal_information)

def mean_grades(grades):
    """
    Permite obtener el promedio de las calificaciones
    para las asignaturas cuantificables del periodo
    """

    # Lista de calificaciones finales cuantificables
    # en el periodo
    quantifiables = []

    # Para cada calificacion final
    for grade in grades["final_grade"]:
        # Si es una asignatura cuantificable (numérica)
        if grade not in ["Aprobado", "Reprobado", "-"]:
            # Añadir a la lista de cuantificables
            quantifiables.append(float(grade))
    
    # Promedio de calificaciones por default
    mean = "-"

    # Si hay registros de calificaciones cuantificables
    if len(quantifiables) > 0:
        # Calcular el promedio y redondear al segundo decimal
        mean = round(np.mean(quantifiables), 2)

    return(mean)

def grades(driver, id_user : str):
    """
    Permite obtener las boletas las boletas de calificaciones
    disponibles para el estudiante en la sección de horario/boleta
    """

    # Dirigirse a la seccipon de la boleta escolar
    school_grades_tab = xpath(driver, "/html/body/div[1]/div/div/div/div/div/ul[2]/li[4]/a")
    school_grades_tab.click()

    # Recuperar el dropdown para cambiar los periodos de consulta
    periods_dropdown = Select(xpath(driver, "/html/body/center/form/select"))

    # Obtener todos los periodos del menú desplegable
    periods = [[period.get_attribute("value"), period.text] for period in periods_dropdown.options][1:]

    # Diccionario que contendrá las calificaciones por periodos
    periods_grades = {}

    # Iterar sobre los periodos disponibles en menú desplegable
    for period_code, period_name in periods:
        # Recuperar el dropdown cada vez que se consulta
        # ya que el web element cambia de dirección cuando se refresca
        # la página
        periods_dropdown = Select(xpath(driver, "/html/body/center/form/select"))
        
        # Seleccionar el periodo actual
        periods_dropdown.select_by_value(period_code)
        
        # Consultar el periodo actual
        button = xpath(driver, "/html/body/center/form/input[4]")
        button.click()
        
        # Recuperar las calificaciones en la consulta actual
        df = pd.read_html(driver.page_source)[1]
        
        # Nombre para las columnas
        column_names = ["number", "type", "section", "subject", "first_partial", "second_partial", "third_partial", "mean", "final_grade", "U1", "U2"]
        
        # Limpiar el dataframe de las calificaciones actuales
        # Cambiar el nombre de las columnas
        df = df.set_axis(column_names, axis = "columns")
        
        # Eliminar columnas no deseadas
        del df["U1"]
        del df["U2"]
        
        # Eliminar filas con valores nulos
        df.dropna(how = "all", inplace = True)
        
        # Recuperar el html de la vista actual
        html = etree.HTML(driver.page_source)
        
        # Obtenemos la lista de claves de asignatura
        id_subjects = html.xpath("//table[2]/tbody/tr/td[contains(@align, 'left')]/text()[1]")

        # Obtenemos los nombres de las asignaturas
        subjects = html.xpath("//table[2]/tbody/tr/td[contains(@align, 'left')]/b/text()[1]")

        # Obtenemos los profesores de cada asignatura
        tr_nodes = html.xpath("//table[2]/tbody/tr/td[contains(@align, 'left')]/text()[3]")
        teachers = [node.split("\n")[2].split("            ")[1] for node in tr_nodes]

        # Obtenemos las modalidades
        modalities = html.xpath("//table[2]/tbody/tr/td[contains(@align, 'left')]/span[contains(@style, 'color:#08c;')]/text()")
        
        # Sobreescribir los nombres de asignaturas
        df["subject"] = subjects
        # Insertar nuevas columnas para las claves, docentes y modalidades
        df.insert(3, "id_subject", id_subjects)
        df.insert(4, "teacher", teachers)
        df.insert(5, "modality", modalities)
        
        # Imputar valores faltantes con un guión
        df = df.fillna("-")

        # Insertar las calificaciones en una lista
        periods_grades[period_code] = {
            # Calcular el promedio del periodo actual
            "mean" : mean_grades(df),
            # Insertar los registros de calificaciones del periodo actual
            "grades" : dataframe_to_dict(df)
        }

    # Consolidar la información en un diccionario con información 
    # del usuario y las calificaciones para cada periodo encontrado
    student_grades = {
        "id_user" : id_user,
        "periods" : periods_grades,
        "last_updated" : datetime.utcnow()
    }

    return(student_grades)

def academic_offer(driver, id_career : str, career : str):
    # Dirigirse a la sección de la oferta académica
    academic_offer_tab = xpath(driver, "/html/body/div[1]/div/div/div/div/div/ul[2]/li[1]/a")
    academic_offer_tab.click()

    # xpath de pestañas
    tabs = [
        # Secciones
        "/html/body/center/ul/li[1]/a",
        # Talleres
        "/html/body/center/ul/li[2]/a",
        # Lengua Extranjera
        "/html/body/center/ul/li[3]/a"
    ]

    title = xpath(driver, "/html/body/center/div").text

    academic_offer = {
        "id_career" : id_career,
        "career" : career,
        "title" : title
    }

    # Recorrer los tabs para sección de oferta
    for index, tab in enumerate(tabs):

        section = ""
        if index == 0:
            section = "additionals"
        elif index == 1:
            section = "workshops"
        else:
            section = "foreign_languages"

        # Intercambiar de pestaña en cada iteración
        current_tab = xpath(driver, tab)
        current_tab.click()

        # Recuperar las tablas con la información de 
        # la oferta en la sección actual. 
        # NOTA: Es una lista de dataframes, el indice 0 corresponde
        # al titulo de la oferta del periodo actual. Los dataframes con 
        # las asignaturas ofertadas se encuentran a partir del
        # indice 1 en adelante.
        df = pd.read_html(driver.page_source)[1:]

        # Variable para controlar el table data
        # Servirá más adelante para obtener la posición con 
        # el nombre del docente de cada asignatura
        td = 0

        # La estructura de las columnas cambia de acuerdo
        # al tipo de oferta académica. En el caso de las asignaturas
        # adicionales, existe una columna para el tipo
        if section == "additionals":
            # La columna de las asignaturas está en la columna 4 para adicionales
            td = 4
            # Nombres para las columnas
            column_names = ["type", "id_subject", "section", "subject", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "U1", "U2", "U3", "U4"]
            # Columnas que se desean conservar
            desired_columns = ["type", "id_subject", "section", "subject", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

        else:
            # La columna de las asignaturas está en la columna 3 para ingles y talleres
            td = 3
            # Nombres para las columnas
            column_names = ["id_subject", "section", "subject", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "U1", "U2", "U3", "U4", "U5"]
            # Columnas que se desean conservar
            desired_columns = ["id_subject", "section", "subject", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
            
        # Recorrer cada dataframe en la pestaña actual
        for i in range(len(df)):
            # Renombrar las columnas de la tabla de acuerdo a la sección
            df[i] = df[i].set_axis(column_names, axis = "columns")

            # Filtrar las columnas de interés
            df[i] = df[i].iloc[:, df[i].columns.isin(desired_columns)]

            # Guardar el contenido de cada tabla para
            # cada indice en el diccionario que contiene la oferta
            # académica
            # Si es la primera tabla en la lista
            if i == 0:
                # Insertar las asignaturas por primera vez
                academic_offer[section] = df[i]
            else:
                # Concatenar con los datos existentes
                academic_offer[section] = pd.concat([academic_offer[section], df[i]], ignore_index = True)

        # Recuperar el html de la pestaña actual
        html = etree.HTML(driver.page_source)

        # Se necesita separar el docente y el nombre de asignatura
        # de la columna subject

        # Buscamos las asignaturas, docentes y modalidades usando XPATH
        subjects = html.xpath("//table[contains(@class, 'datos')]/tbody/tr/td[" + str(td) + "]/b/text()")
        # Lista de asignaturas en todas las tablas de la sección actual
        subjects = [subject.split("\n")[0] for subject in subjects]

        tr_nodes = html.xpath("//table[contains(@class, 'datos')]/tbody/tr/td[" + str(td) + "]/text()[2]")
        # Lista de docentes en todas las tablas de la sección actual
        teachers = [tr.split("\n                        ")[0] for tr in tr_nodes]

        # Lista de modalidades de asignatura en la sección actual
        modalities = html.xpath("//table[contains(@class, 'datos')]/tbody/tr/td[" + str(td) + "]/span[contains(@style, 'color:#08c;')]/text()")
            
        # Si la sección no son adicionales
        if section != "additionals":
            # Se inserta el tipo ya que solo aparece en adicionales pero no en
            # los demas tipos de asignaturas en la oferta
            academic_offer[section].insert(0, "type", "")

        # Reasignar la columna con las asignaturas separadas de los demas
        academic_offer[section]["subject"] = subjects
        # Insertar una nueva columna con los docentes
        academic_offer[section].insert(3, "teacher", teachers)
        # Insertar una nueva columna con las modalidades de asignaturas
        academic_offer[section].insert(4, "modality", modalities)
        

        # Convertir el dataframe de la sección actual a diccionario
        academic_offer[section] = dataframe_to_dict(academic_offer[section])
        
    # Última fecha de actualización
    academic_offer["last_updated"] = datetime.utcnow()
    return(academic_offer)

def payments(driver, id_user : str):
    # Dirigirse a la sección de pagos
    payments_tab = xpath(driver, "/html/body/div[1]/div/div/div/div/div/ul[2]/li[7]/a")
    payments_tab.click()
    # Extraer las tablas de la vista actual
    df = pd.read_html(driver.page_source)

    # Filtrar las tablas que tienen la información de los pagos
    df[0].drop(["Opciones", "Opciones.1"], axis = 1, inplace = True)
    # Renombrar las columnas de la tabla de pagos
    column_names = ["number", "id", "period", "date", "description", "amount", "expiration", "status"]
    df[0] = df[0].set_axis(column_names, axis = "columns", copy = False)
    
    # Cambiar el formato por un tipo de datos valido para las fechas
    df[0]["date"] = df[0]["date"].astype("datetime64[ns]")
    df[0]["expiration"] = df[0]["expiration"].astype("datetime64[ns]")
    
    # Convertir el dataframe de pagos a un diccionario
    my_payments = dataframe_to_dict(df[0])


    # Revisar la existencia de un enlace de pago
    link = xpath(driver, "//table[contains(@class, 'datos')]/tbody/tr/td[9]/a")

    # Si se encontró un enlace de pago
    if link != "Elemento no encontrado":
        # Obtener la dirección URL de la página con los datos de pago
        url = link.get_attribute("href")
        # Guardamos esa página como un PDF
        pdfkit.from_url(url, "payments/Referencia de pago - " + id_user + ".pdf")

    # Crear un diccionario con la información final del estudiante
    payments_dictionary = {
        "id_user" : id_user,
        "payments" : my_payments,
        "last_updated" : datetime.utcnow()
    }

    return(payments_dictionary)

def internships_offer(driver):
    """
    Permite obtener la oferta de prácticas profesionales
    """
    # Dar clic en el dropdown del menu
    dropdown = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/ul/li[2]/a')
    dropdown.click()

    # Ir a la oferta de proyectos
    projects_section = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/ul/li[2]/ul/li[2]/a')
    projects_section.click()

    # Obtener el selector
    select = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/table[1]/tbody/tr/td/form/fieldset/div/select")
    # Crear un objecto Select para interactuar con el
    select = Select(select)

    # Creamos una variable que almacene la lista de opciones
    # del dropdown
    options = []

    # Obtenemos una lista de las opciones disponibles en el dropdown
    for item in select.options:
        options.append(item.get_attribute("innerHTML"))

    # Print available dropdown options
    print("Opciones: ", options)

    # Lista de perioos de practicas disponibles
    available_offers = []
    # Para cada opcion en el dropdown
    for option in options:
        # Encontramos el dropdown de nuevo
        dropdown = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/table[1]/tbody/tr/td/form/fieldset/div/select")
        # Enviamos la opcion actual
        dropdown.send_keys(option)
        
        # Encontramos el boton de la consulta
        search = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/table[1]/tbody/tr/td/form/fieldset/input")
        # Damos clic en el boton
        search.click()
        
        # Creamos un diccionario donde meteremos los datos
        practices_offer = {
            "id_offer" : "",
            "career" : student_information["career"]["name"],
            "period" : option.split()[0],
            "offer" : {}
        }

        # practices_offer
        # Encontramos todos los enlaces para consultar más info de la practica
        botones = driver.find_elements(By.XPATH, "//table[contains(@class, 'tbuscar')]/tbody/tr/td[7]/a")

        # Creamos una lista para almacenar los url
        urls = []
        # para cada boton extraemos su link
        for b in botones:
            # Guardamos cada link en la lista anterior
            urls.append(str(b.get_attribute("href")))

        # Imprimimos los links encontrados y la cantidad
        # print("Links: " + str(len(urls)))
        # print(urls)

        def getCompanyInfo(driver):
            """
            This function allows us to extract the data 
            inside each form when a 'more info' button is
            pressed in the list of companies offered 
            in the SIPP
            """
            # Encontramos las etiquetas html donde se encuentra la info
            # que nos interesa
            form_data = driver.find_elements(By.XPATH, "//valor")
            # Extraemos el texto de cada etiqueta en una lista
            data = [datum.text for datum in form_data]
            # Extraemos la direccion email del campo con la info
            email = re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", data[8]) # Get the email

            # Si el email no se encuentra
            if email == None:
                # Se fija este campo en cadena vacia
                email = ""
            # Si el email se encuentra usando regex
            else:
                # Se obtiene el texto del email encontrado
                email = email.group(0)

            # Imprimimos la lista de datos encontrados en formulario  
            # print(data)

            # Creamos un diccionario con los datos encontrados
            # y les datos nombres
            information = {
                "id_practice" : data[1].split(" / ")[0],
                "practice_name" : data[1].split(" / ")[1],
                "company_name" : data[0],
                "required_practitioners" : data[2],
                "available_spaces" : data[3],
                "type" : data[4],
                "endeavor" : data[5],
                "activities" : data[6],
                "required_english" : data[7] + "%",
                "contact_info" : data[8],
                "email" : email,
                "teacher" : data[9], 
                "comments" : data[10] 
            }

            # Returnamos el diccionario creado
            return(information)

        # Lista donde se guardarán los diccionarios 
        # con la información adicional consultada de 
        # cada empresa en la oferta (en el periodo previamente
        # seleccionado)
        info = []
        # Para cada url en la lista de urls
        for url in urls:
            # Vamos ese link
            driver.get(url)
            # Guardamos la informaciön extraida del formulario en la lista de 
            # información de las ofertas (aqui se guardan los diccionarios)
            info.append(getCompanyInfo(driver))
            # Regresar a la pagina anterior para repetir el proceso iterativamente
            driver.back()

        # En un diccionario final de practicas, guardamos la lista de diccionarios
        # en el campo "offer"
        practices_offer["offer"] = info
        practices_offer["id_offer"] = info[0]["id_practice"]
        # Guardamos este diccionario en una lista que contiene la info de todos los periodos
        # disponibles en el SIPP (Ej. 202202 Verano, 202203 Otoño...)
        available_offers.append(practices_offer)

    # Retornamos la lista con los diccionarios de las ofertas
    # que contienen la información de las ofertas de practicas
    return(available_offers)