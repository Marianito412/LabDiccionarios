import re
import funciones

def validarCedula(pCedula: str):
    while True:
        if re.match(r"[\d]{1}-[\d]{4}-[\d]{4}", pCedula):
            return pCedula
        else:
            pCedula = input("EROR: Cédula inválida, recuerde usar el siguente formato: 0-0000-0000\nIntente de nuevo: ")

def validarNombre(pNombre):
    while True:
        if re.match(r"[\w]+ [\w]+ [\w]+", pNombre):
            return pNombre
        else:
            pNombre = input("EROR: Nombre inválida, se espera el formato Nombre Apellido1 Apellido2 (cuide los espacios)\nIntente de nuevo: ")

def validarBin(pString: str):
    while True:
        if pString in ["1", "2"]:
            return pString == "1"
        else:
            pString = input("EROR: Opción inválida, ingrese 1 o 2 (1: si, 2: no)\nIntente de nuevo: ")

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
            pNumero = input("No ingresó un valor valido ya que no es un digito\nIntente de nuevo: ")

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

def menu():
    menuDicc = {
        1: ["Modificar Datos", ESModificarDatos],
        2: ["Eliminar Datos", ESEliminarDatos],
        3: ["Reportes", ESReportes]
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
