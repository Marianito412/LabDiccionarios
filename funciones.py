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
