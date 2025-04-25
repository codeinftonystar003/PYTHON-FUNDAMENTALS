def menu():
    print("[1] Pulgadas")
    print("[2] Yardas")
    print("[3] Millas")
    print("[4] Milímetros")
    print("[5] Centímetros")
    print("[6] Metros")
    print("[7] Resumen")
    print("[8] Salir")
def main():
    lista_conversiones = []
    menu()
    while True:
        while True:
            try:
                opcion = int(input("Ingrese una opcion : "))
                if 1<= opcion <= 8:
                    break
                else:
                    print("Opcion fuera de rango")
            except ValueError:
                print("Error en los datos de ingreso...")
    
        if opcion == 8:
            print("Saliendo del programa.....")
            break
        if opcion == 7:
            print("MOSTRAR RESUMEN DE CONVERSIONES")
            if not lista_conversiones:
                print("La lista esta vacia") 
            else:
                print("-"*50)
                print("RESUMEN DE LAS CONVERSIONES")
                print("-"*50)
                print("N° ", "Pies"  , "Convertir a : ", "Convertido ")
                for i, (x,y,z) in enumerate(lista_conversiones, start= 1):
                    print(f"{i:<2} {x:>5}  {y:>7} {z:>14}")
                print("-"*50)
            continue
        
        while True:
            try:
                pies = int(input("Ingrese el numero de pies a convertir : "))
                if pies>0:
                    break
                else:
                    print("El dato debe ser mayor a cero")
            except ValueError:
                print("error en los datos de ingreso...")
            
        if opcion == 1:
            unidad = "Pulgadas"
            resultado = pies * 12
        elif opcion == 2:
            unidad = "Yardas"
            resultado = pies * 0.33
        elif opcion == 3:
            unidad = "Millas"
            resultado =  pies * 0.0002
        elif opcion == 4:
            unidad = "Milimetros"
            resultado = pies * 304.8
        elif opcion == 5:
            unidad  = "Centimetros"
            resultado = pies * 30.48
        elif opcion ==  6:
            unidad = "Metros"
            resultado = pies * 0.3048
        else:
            print("Opcion fuera de rango...")
            
        lista_conversiones.append((pies,unidad,resultado))
            
        salir = input("Desea salir (s/n)")
        if salir.lower() == 's':
            break
        elif salir.lower() == 'n':
            pass
        else:
            print("Error dato invalido")
                
    if not lista_conversiones:
        print("La lista esta vacia") 
    else:
        print("-"*50)
        print("RESUMEN  FINAL DE LAS CONVERSIONES")
        print("-"*50)
        print("N° ", "Pies"  ,   "Convertir a : ", "Convertido ")
        for i, (x,y,z) in enumerate(lista_conversiones, start= 1):
            print(f"{i:<2} {x:>5}  {y:>7} {z:>14}")
        print("-"*50)
main()
        
        