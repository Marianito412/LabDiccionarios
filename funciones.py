#Importación de bibliotecas
import random

def registrarDatos(pDicc, pCedula, pNombre, pGenero):
    """
    Funcionalidad: Registra una nueva persona en la base de datos
    Entradas:
    -pDicc(dict): Diccionario a modificar
    -pCedula(str): Cedula de nueva persona
    -pNombre(str): Nombre de nueva persona
    -pGenero(bool): Genero de nueva persona
    Salidas:
    -pDicc(str): Diccionario modificado
    """
    if pCedula not in pDicc:
        personalidad = random.randint(1, 16)
        pDicc[pCedula] = [pNombre, pGenero, personalidad]
    else:
        print("Esta cédula ya se registró previamente")
    return pDicc

def modificarDatos(pDicc, pCedula, pNombre, pPersonalidad):
    """
    Funcionalidad: Modifica una persona en la base de datos
    Entradas:
    -pDicc(dict): Diccionario a modificar
    -pCedula(str): Cedula de persona
    -pNombre(str): Nuevo nombre de nueva persona
    -pGenero(bool): Nuevo genero de persona
    Salidas:
    -pDicc(str): Diccionario modificado
    """
    genero = pDicc[pCedula][1]
    pDicc[pCedula] = [pNombre, genero, pPersonalidad]
    return pDicc

def eliminarDatos(pDicc: dict, pCedula):
    """
    Funcionalidad: Elimina una persona de la base de datos
    Entradas: 
    -pDicc(dict): El diccionario a modificar
    -pCedula(str): La cédula de la persona a eliminar
    Salidas:
    -pDicc(dict): El diccionario modificado
    """
    pDicc.pop(pCedula)
    return pDicc

def reportePersona(pDicc: dict, pCedula):
    """
    Funcionalidad: Muestra el reporte de una persona
    Entradas:
    -pDicc(dict): El diccionario sobre el que buscar
    Salidas: NA
    """
    personalidades={1: "INTJ",2: "INTP",3:"ENTJ",4:"ENTP",5:"INFJ",6:"INFP",7:"ENFJ",8:"ENFP",9:"ISTJ",10:"ISFJ",11:"ESTJ",12:"ESFJ",13:"ISTP",14:"ISFP",15:"ESTP",16:"ESFP"}
    persona = pDicc[pCedula]
    print(f"\tNombre: {persona[0]}\n\tGénero: {'Hombre' if persona[1] else 'Mujer'}\n\tPersonalidad: {personalidades[persona[2]]}")
