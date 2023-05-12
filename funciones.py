import random

def registrarDatos(pDicc, pCedula, pNombre, pGenero):
    personalidad = random.randint(1, 16)
    pDicc[pCedula] = [pNombre, pGenero, personalidad]
    print(pDicc)
    return pDicc

def modificarDatos(pDicc, pCedula, pNombre, pPersonalidad):
    genero = pDicc[pCedula][1]
    pDicc[pCedula] = [pNombre, genero, pPersonalidad]
    return pDicc

def eliminarDatos(pDicc: dict, pCedula):
    pDicc.pop(pCedula)
    return pDicc

def reportePersona(pDicc: dict, pCedula):
    personalidades={1: "INTJ",2: "INTP",3:"ENTJ",4:"ENTP",5:"INFJ",6:"INFP",7:"ENFJ",8:"ENFP",9:"ISTJ",10:"ISFJ",11:"ESTJ",12:"ESFJ",13:"ISTP",14:"ISFP",15:"ESTP",16:"ESFP"}
    persona = pDicc[pCedula]
    print(f"\tNombre: {persona[0]}\n\tGénero: {'Hombre' if persona[1] else 'Mujer'}\n\tPersonalidad: {personalidades[persona[2]]}")
