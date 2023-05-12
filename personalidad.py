import re
import funciones
import random

def validarCedula(pCedula: str):
    while True:
        if re.match(r"[\d]{1}-[\d]{4}-[\d]{4}", pCedula):
            return pCedula
        else:
            pCedula = input("ERROR: Cédula inválida, recuerde usar el siguente formato: 0-0000-0000\nIntente de nuevo: ")

def validarNombre(pNombre):
    while True:
        if re.match(r"[\w]+ [\w]+ [\w]+", pNombre):
            return pNombre
        else:
            pNombre = input("ERROR: Nombre inválida, se espera el formato Nombre Apellido1 Apellido2 (cuide los espacios)\nIntente de nuevo: ")

def validarGenero(pString: str):
    while True:
        if pString=="1":
            return True
        elif pString=="2":
            return False
        else:
            pString = input("ERROR: Opción inválida, ingrese 1 o 2 (1: hombre, 2: mujer)\nIntente de nuevo: ")

def validarBin(pString: str):
    while True:
        if pString in ["1", "2"]:
            return pString == "1"
        else:
            pString = input("ERROR: Opción inválida, ingrese 1 o 2 (1: si, 2: no)\nIntente de nuevo: ")

def validarPersonalidad(pNumero):
    """
    Funcionalidad: Valida que un número dado sea entero
    Entradas:
    -pNumero(str): El numero a validar
    Salidas:
    return(int): El entero si es válido
    """
    while True:
        if pNumero.isdigit():
            if int(pNumero)>=1 and int(pNumero)<= 16:
                return int(pNumero)
            else:
                pNumero = input("Debe ingresar un numero de 1 a 16\nIntente de nuevo: ")
        else:
            pNumero = input("No ingresó un valor valido ya que no es un digito\nIntente de nuevo: ")

def ESRegistrarDatos(pDicc):
    cedula = validarCedula(input("Ingrese el número de cédula: "))
    nombre = validarNombre(input("Ingrese el nombre: "))
    genero = validarGenero(input("Es un hombre? (Ingrese 1=si, 2=no): "))
    pDicc = funciones.registrarDatos(pDicc, cedula, nombre, genero)
    print("Datos registrados exitosamente")
    return pDicc

def ESModificarDatos(pDicc):
    cedula = validarCedula(input("Ingrese el número de cédula a modificar: "))
    nombre = validarNombre(input("Ingrese el nuevo nombre: "))
    personalidad = validarPersonalidad(input("Ingrese la nueva personalidad: "))
    if validarBin(input("Está segur@ que desea modificar este valor?\nIngrese 1 o 2 (1: sí, 2: no): ")):
        pDicc = funciones.modificarDatos(pDicc, cedula, nombre, personalidad)
        print("Datos modificados exitosamente")
    else:
        print("Se canceló la modificación de los datos")
    return pDicc

def ESEliminarDatos(pDicc: dict):
    cedula = validarCedula(input("Ingrese el número de cédula a eliminar: "))
    if validarBin(input("Está segur@ que desea eliminar esta persona?\nIngrese 1 o 2 (1: sí, 2: no): ")):
        pDicc = funciones.eliminarDatos(pDicc, cedula)
        print(f"Se eliminó exitosamente la persona con cédula {cedula}")
    else:
        print("Se canceló la eliminación")
    return pDicc

def ESReportePersona(pDicc):
    cedula = validarCedula(input("Ingrese el número de cédula a eliminar: "))
    persona = pDicc[cedula]
    print(f"Nombre: {persona[0]}\nGénero: {'Hombre' if persona[1] else 'Mujer'}\nPersonalidad: {persona[2]}")

def ESReporteTotal(pDicc):
    ...

def SalirReporte(pDicc):
    print("Regresando a menu principal...")

def ESReportes(pDicc):
    menuDicc = {
        1: ["Por personalidad", ESModificarDatos],
        2: ["Por categoría", ESEliminarDatos],
        3: ["Por persona", ESReportePersona],
        4: ["Reporte total", ESReporteTotal],
        5: ["Salir a menu", SalirReporte]
    }
    while True:
        for key in menuDicc:
            print(f"{key}. {menuDicc[key][0]}")
        try:
            opcion = int(input("Ingrese el número de su opción a elegir: "))
            menuDicc[opcion][1](pDicc)
            if opcion == 5:
                break
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")
    return pDicc

def ESReportes2(pDicc):
    personalidades={1: "INTJ",2: "INTP",3:"ENTJ",4:"ENTP",5:"INFJ",6:"INFP",7:"ENFJ",8:"ENFP",9:"ISTJ",10:"ISFJ",11:"ESTJ",12:"ESFJ",13:"ISTP",14:"ISFP",15:"ESTP",16:"ESFP"}
    for i in personalidades:
        print(f"{i}. {personalidades[i]}")
        for j in pDicc:
            if i in pDicc[j]:
                print("\n"
                      f" ---Usuarios con personalidad {personalidades[i]} ---\n"
                      f"    cedula: {j}\n"
                      f"    nombre: {pDicc[j][0]}\n"
                      f"    genero: {pDicc[j][1]}\n"
                      )
    print("Reporte")
    return pDicc

def menu():
    menuDicc = {
        1: ["Registrar Datos", ESRegistrarDatos],
        2: ["Modificar Datos", ESModificarDatos],
        3: ["Eliminar Datos", ESEliminarDatos],
        4: ["Reportes", ESReportes]
    }
    personalidad = {}
    while True:
        for key in menuDicc:
            print(f"{key}. {menuDicc[key][0]}")
        try:
            opcion = int(input("Ingrese el número de su opción a elegir: "))
            personalidad = menuDicc[opcion][1](personalidad)
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")

menu()
