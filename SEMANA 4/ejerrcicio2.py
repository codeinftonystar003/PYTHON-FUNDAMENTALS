agenda = {}
while True:
    print("\n")
    print("1.Añadir / modificar")
    print("2.Buscar")
    print("3.Borrar")
    print("4.Listar")
    print("5.Salir")
    
    opcion = int(input("Ingrese opcion : "))
    if opcion == 1:
        nombre =  input("Ingrese nombre: ")
        if nombre in agenda: 
            print("%s ya existe y su telefono es %s" %(nombre, agenda[nombre]))
            opcion = input("Presiona  s si quieres continuar .Otra tecla para continuar")
            if opcion == "s":
                numero = input("Ingrese numero: ")
                agenda[nombre] = numero
        else:
            numero = input("Ingrese el numero: ")
            agenda[nombre] = numero
    elif opcion == 2:
        cadena = input("Nombre de la  persona a buscar: ")
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El numero de telefono de %s es el %s" %(nombre, numero))
    elif opcion == 3:
        nombre = input("Nombre de la persona a borrar: ")
        if nombre in agenda:
            opcion = input("Presiona s si quieres borrar .Otra tecla para continuar")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("El contacto no existe")
    elif  opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre, "--> ", numero)
    elif opcion == 5:
        break
    else:
        print("Opcion fuera de rango")