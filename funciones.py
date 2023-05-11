

def modificarDatos(pDicc, pCedula, pNombre, pPersonalidad):
    genero = pDicc[pCedula][1]
    pDicc[pCedula] = [pNombre, genero, pPersonalidad]

def eliminarDatos(pDicc: dict, pCedula):
    pDicc.pop(pCedula)
    return pDicc