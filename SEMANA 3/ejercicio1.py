"""
Convierte pies a diferentes unidades usando un menú como el siguiente:
[1] Pulgadas
[2] Yardas
[3] Millas
[4] Milímetros
[5] Centímetros
[6] Metros
[7] Resumen
[8] Salir
La conversión de pies a las diferentes medidas es la siguiente:
Unidad Conversión
Pulgadas 12
Yardas 0.33
Millas 0.0002
Milímetros 304.8
Centímetros 30.48
Metros 0.3048

"""
from tabulate import tabulate
lista_conversion = []
def Menu():
    print("[1] Pulgadas")
    print("[2] Yardas")
    print("[3] Millas")
    print("[4] Milímetros")
    print("[5] Centímetros")
    print("[6] Metros")
    print("[7] Resumen")
    print("[8] Salir")

def Conversion(pies, opcion):
    resultado  = 0
    if opcion == 1:
        unidad = "Pulgadas"
        resultado = pies * 12
    elif opcion == 2:
        unidad = "Yardas"
        resultado = pies * 0.33
    elif opcion == 3:
        unidad = "Millas"
        resultado = pies * 0.0002
    elif opcion == 4:
        unidad = "Milímetros"
        resultado = pies * 304.8
    elif opcion == 5:
        unidad = "Centímetros"
        resultado = pies * 30.48
    elif opcion == 6:
        unidad = "Metros"
        resultado = pies * 0.3048
    else:
        print("Opción no válida")
        
    Guadar_datos(pies, resultado, unidad)

def Guadar_datos(pies, resultado, unidad):
    conversion = {
        "pies": pies,
        "resultado": resultado,
        "unidad": unidad
    }
    lista_conversion.append(conversion)
def Resumen():
    print("Resumen de conversiones")
    print(tabulate(lista_conversion, headers="keys", tablefmt="grid"))
    print("Total de conversiones: ", len(lista_conversion))

def main():
    Menu()
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 8:
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Opción no válida. Intente de nuevo.")
    
    while True:
        try:
            pies = float(input("Ingrese la cantidad de pies : "))
            if pies > 0:
                break
            else:
                print("Ingrese un número positivo")
        except ValueError:
            print("Ingrese un número válido") 
    Conversion(pies, opcion)
    
    salir = input("¿Desea continuar? (s/n): ")
    if salir.lower() == "s":
        Resumen()
    elif salir.lower() == "n":
        main()
    else:
        print("Opción no válida. Saliendo...")
main()