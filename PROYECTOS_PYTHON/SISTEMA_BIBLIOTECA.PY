from datetime import datetime, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt

class Lectores:
    def __init__(self,edad,nombre,
        apellido,dni,celular,sexo,calle,ciudad,distrito,numero):
        self.edad = edad
        self.nombre = nombre
        self.apellido =apellido
        self.dni = dni
        self.celular =celular
        self.sexo = sexo
        self.calle = calle
        self.ciudad = ciudad
        self.distrito = distrito
        self.numero = numero

        
class Datos_lectores:
    def __init__(self):
        self.lista_lectores = []
        self.lectores = 0
    def Guardar_lectores (self,edad,nombre, apellido,dni, celular, sexo, calle, ciudad, distrito, numero):
        lectores = {'EDAD' : edad, 'NOMBRE' : nombre, 'APELLIDOS' : apellido, 'DNI' : dni, 'CELULAR' : celular, 
                    'SEXO': sexo, 'CALLE':calle, 'CIUDAD': ciudad, 'DISTRITO': distrito, 'NUMERO DE VIVIENDA': numero}
        self.lista_lectores.append(lectores)
        
    def Mostrar_lectores(self):
        if not self.lista_lectores:
            print("-" * 60)
            print("No hay lectores registrados")
            print("-" * 60)
        else:
            print("LISTADO DE LECTORES")
            print(tabulate(self.lista_lectores, headers ="keys", tablefmt = "grid"))
            
    def Registrar_lector(self):
        while True:
            try:
                dni = input("ingrese su dni : ")
                if len(dni) != 8 and not dni.isdigit():
                    print("DNI incorrecto ")
                    continue
                if any(DNI["DNI"] == dni for DNI in self.lista_lectores):
                    print("el lector no debe repetirse")
                else:
                    self.lectores +=1
                    break
            except ValueError:
                print("datos incorrectos, intente de nuevo")
                
        while True:
            edad = int (input("Ingrese su edad : "))
            if 10<= edad <= 80:
                break
            else:
                print("Edad incorrecta")
        nombre = input("ingrese su nombre : ").title()   
        apellido = input("ingrese su apellido : ").title()
        
        while True:
            try:
                celular = input ("Ingrese su numero de telefono : ")
                if len(celular) == 9 and celular.isdigit():
                    break
                else:
                    print("numero de telefono incorrecto")
            except ValueError:
                print("datos incorrectos, intente de nuevo")
        while True:
            sexo = input("Ingrese su genero (F, M , O): ").upper()
            if sexo in ["F", "M", "O"]:
                break
            else:
                print("datos de sexo, incorrectos")
        
        calle = input("Ingrese la calle de ubicacion: ").capitalize()
        ciudad = input("Ingrese la ciudad de residencia actual: ").capitalize()
        distrito = input("ingrese el distrito en donde se encuentra: ").capitalize()
        while True:
            try:
                numero = int(input("Ingrese el numero de vivienda( 100 - 999 ): "))
                if 100 <= numero <= 999:
                    break
                else:
                    print("Datos incorrectos, intente de nuevo")
            except ValueError:
                print("datos incorrectos")
        self.Guardar_lectores(edad, nombre, apellido,dni, celular, sexo, calle, ciudad, distrito, numero)
        print("\nLECTOR REGISTRADO CON EXITO")
    def Lectores_registrados(self):
        self.Guardar_lectores(18,"Antony Yomar", "Peña Roña", "62540531", "973156243", "M","lOS LOBOS", "LIMA","CHORRILLOS", 102)
        self.Guardar_lectores(25, "Maria Isabel", "Gomez Perez", "62540532", "987654321", "F", "Avenida Principal", "AREQUIPA", "Cayma", 505)
        self.Guardar_lectores(20, "Carlos Alberto", "Rodriguez Soto", "62540533", "945612378", "M", "Calle Las Flores", "TRUJILLO", "Victor Larco", 222)
    
    def buscar_lectores(self):
        while True:
            dni_lector = input("ingrese el dni del lector a buscar: ")
            if len(dni_lector) == 8 and dni_lector.isdigit():
                break
            else:
                print("dni incorrecto , intente de nuevo")
        for lectores in self.lista_lectores:
            if lectores["DNI"] == dni_lector:
                print("\nDATOS DEL LECTOR BUSCADO")
                print("====================================================")
                print(f"EDAD     : {lectores["EDAD"]}")
                print(f"NOMBRE   : {lectores["NOMBRE"]}")
                print(f"APELLIDOS: {lectores["APELLIDOS"]}")
                print(f"DNI      : {lectores["DNI"]}")
                print(f"CELULAR  : {lectores["CELULAR"]}")
                print(f"GENERO   : {lectores["SEXO"]}")
                print(f"CALLE    : {lectores["CALLE"]}")
                print(f"CIUDAD   : {lectores["CIUDAD"]}")
                print(f"DISTRITO : {lectores["DISTRITO"]}")
                print(f"NUMERO DE VIVIENDA : {lectores["NUMERO DE VIVIENDA"]}")
                print("====================================================")
                return
            
        print("lector no encontrado, verifique si esta registrado en la base de datos")
    
    def Eliminar_lectores(self):
        while True:
            dni_lector = input("Ingrese el DNI del lector a Eliminar: ")
            if len(dni_lector) == 8 and dni_lector.isdigit():
                break
            else:
                print("El DNI ingresado no es correcto , intente de nuevo")
        
        for lector in self.lista_lectores:
            if lector['DNI'] == dni_lector:
                while True:
                    opcion = input("Desea aceptar la eliminacion (si / no): ").upper()
                    if opcion in ['SI', 'NO']:
                        break
                    else:
                        print("Formato no encontrado")
                if opcion == 'SI':
                    self.lista_lectores.remove(lector)
                    print("-"*60)
                    print(f"Lector con DNI : {lector['DNI']} eliminado con exitos de la base de datos")
                    print("-"*60)
                    return 
                if opcion == 'NO':
                    print("operacion de Delete Cancelada....")
                    return 
        print("EL DNI del lector no ha sido encontrado en la base de datos")
               
                           
class Publicaciones():
    def __init__(self, codigo, titulo, tipo, local, disponible):
        self.codigo = codigo 
        self.titulo = titulo
        self.tipo = tipo 
        self.local = local 
        self.disponible = disponible
        
class Datos_publicaciones(): 
    def __init__(self):
        self.lista_publicaciones = []
        self.publicaciones = 0
        
    def Guardar_publicaciones(self, codigo, titulo, tipo, local, disponible):
        publicaciones = {'CODIGO':codigo, 'TITULO':titulo, 'TIPO':tipo,'LOCAL': local, 'DISPONIBILIDAD': disponible}
        self.lista_publicaciones.append(publicaciones)
    
    def Mostrar_publicaciones(self):
        if not self.lista_publicaciones:
            print("-" * 60)
            print("No existen publicaciones registradas")
            print("-" * 60)
        else:
            print("   PUBLICATIONES REGISTRADAS  ")
            print("================================")
            print(tabulate(self.lista_publicaciones, headers = "keys",tablefmt = "grid" ))
    
    
    def Registrar_publicaciones(self):
        while True:
            codigo = input("Ingrese el código de la publicación: ")
            if len(codigo) != 8 or  not codigo.isdigit():
                print("codigo incorrecto debe tener 8 caracteres")
                continue 
            if  any(publicacion["CODIGO"] == codigo for publicacion in self.lista_publicaciones): 
                print("el codigo no debe repetirse..")
            else:
                self.publicaciones +=1
                break
            
        titulo = input("Ingrese el titulo de la publicacion: ")
        
        while True:
            try: 
                print("\nTIPO DE PUBLICACION\n")
                print("1. Revista \n2. Periodico  \n3. Libro")
                opcion =  int(input("selecione el tipo de publicaion: "))
                if opcion == 1 :
                    tipo = 'Revista'
                    break
                elif opcion == 2 :
                    tipo = 'Periodico'
                    break
                elif opcion == 3 :
                    tipo = 'Libro'
                    break
                else:
                    print("opcion fuera de rango")
            except ValueError:
                print("datos incorrectos")
    
        while True:
            print("\nLOCAL DE ATENCION AL LECTOR\n")
            print("1.Miraflores\n2.Chorrilos\n3.Abancay\n")
            opcion = int(input("elija una opcion : "))
            if opcion == 1:
                local = 'Miraflores'
                break
            elif opcion == 2:
                local = 'Chorrilos'
                break
            elif opcion == 3:
                local = 'Abancay'
                break
            else:
                print("opcion fuera de rango")
        while True:
            disponible = input("ingrese la disponiblidad (Si - No): ").capitalize()
            if disponible in ['Si' , 'No']:
                break
            else:
                print("no se reconocio su respuesta de disponibilidad")
    
        self.Guardar_publicaciones(codigo,titulo,tipo,local,disponible)
        print("-"*60)
        print("\nPUBLICACION REGISTRADA CON EXIITO\n")
        print("-"*60)

    def Publicaciones_registradas(self):
        # Se deben pasar valores individuales, no listas
        self.Guardar_publicaciones("12345678", "Lima Sur", "Revista", "Chorrillos", "Si")
        self.Guardar_publicaciones("12345778", "El Universo", "Libro", "Abancay", "No")
        self.Guardar_publicaciones("12345555", "Tiempo Real", "Revista", "Miraflores", "Si")
    
    def Buscar_publicaciones(self):
        codigo_publicacion = input("Ingrese el código de la publicación: ")
        
        for publicacion in self.lista_publicaciones:  # ✅ Sin paréntesis
            if publicacion["CODIGO"] == codigo_publicacion:
                print("\nDATOS DE LA PUBLICACION")
                print("====================================================")
                print(f"CÓDIGO         : {publicacion['CODIGO']}")
                print(f"TÍTULO         : {publicacion['TITULO']}")
                print(f"TIPO           : {publicacion['TIPO']}")
                print(f"LOCAL          : {publicacion['LOCAL']}")
                print(f"DISPONIBILIDAD : {publicacion['DISPONIBILIDAD']}")
                print("====================================================")
                return  # ✅ Salimos de la función si encontramos la publicación
        
        # ✅ Si no encontramos nada, mostramos el mensaje una sola vez
        print("El código de publicación no existe en la base de datos.")
        
    def Graficar_publicaciones(self):
        revista = libro = periodico = 0
        for publicacion in self.lista_publicaciones:
            if publicacion['TIPO'] == 'Revista':  
                revista += 1
            if publicacion['TIPO'] == 'Periodico':   
                periodico += 1
            if publicacion['TIPO']== 'Libro':   
                libro += 1

        categorias = ['Revistas', 'Periódicos', 'Libros']
        cantidades = [revista, periodico, libro]

        # Graficar 
        plt.bar(categorias, cantidades, color=['blue', 'green', 'skyblue'])
        plt.xlabel("Tipo de recurso")
        plt.ylabel("Cantidad por tipo de recurso bibliotecario")
        plt.title("Gráfico de publicaciones")

        # Mostrar el gráfico
        plt.show(block=False)

    def cambiar_datos_publicaciones(self):
        while True:
            id_publicacion = input("ingrese el ID publicacion : ")
            if len(id_publicacion) == 8 and id_publicacion.isdigit():
                break
            else:
                print("datos de publicacion incorrectos")
                
        for publicacion in self.lista_publicaciones:
            if publicacion['CODIGO'] == id_publicacion:
                print("\nMENU DE MODIFICACION DE DATOS")
                print("=="*15)
                print('1. Modificar codigo de publicacion')
                print('2. Modificar titulo de publicacion')
                print('3. Modificar el tipo de publicacion')
                print('4. Modificar Local  de publicacion')
                print('5. Disponibilidad')
                
                opcion = int(input("Ingrese la opcion : "))
                while True:
                    if 1<= opcion <= 5:
                        break
                    else:
                        print("Opcion de publicacion incorrect")
                for publicacion in self.lista_publicaciones:
                    if opcion == 1:
                        publicacion['CODIGO'] = input("Ingrese el nuevo codigo de publicacion: ")
                    
                    elif opcion == 2:
                        publicacion['TITULO'] = input("Ingrese el nuevo titulo de publicacion: ")
                    elif opcion == 3: 
                        publicacion['TIPO'] = input("Ingrese el nuevo tipo de publicacion:")
                    elif opcion == 4:
                        publicacion['LOCAL'] = input("Ingrese el nuevo local de publicacion: ")
                    elif opcion  == 5:
                        while True:
                            disponible = input("ingrese disponibiblidad de la publicacion: ").upper()
                            if disponible in ['SI', 'NO']:
                                break
                            else:
                                print("Formato no aceptado")
                        publicacion['DISPONIBILIDAD'] = disponible
                        
                    print("-"*60)
                    print("DATOS DE PUBLICACION ACTUALIZADOS CON EXITO")
                    print("-"*60)
                    return 
        print("Codigo de publicacion no encontrado")

    def Eliminar_publicaciones(self):
        while True:
            id_publicacion = input("Ingrese el ID publicacion: ")
            if len(id_publicacion) == 8 and id_publicacion.isdigit():
                break
            else:
                print("id de la publicacion incorrecto ")
        
        for publicacion in self.lista_publicaciones:
            if publicacion['CODIGO'] == id_publicacion:
                while True:
                    opcion = input("Desea aceptar la eliminación (SI / NO ): ").upper()
                    if opcion in ['SI', 'NO']:
                        break
                    else:
                        print("Fomato de opcion incorrecto")
                
                if opcion == 'SI':
                    self.lista_publicaciones.remove(publicacion)
                    print('-'*60)
                    print(f"publicacion con id : {publicacion['CODIGO']} eliminada con exito")
                    print('-'*60)
                    return 
                if opcion == 'NO':
                    print("Proceso de delete cancelado con exito.....")
                    return
        print("publicacion no encontrada")

    
class Prestamos():
    def __init__(self, dni_lector, codigo_publicacion,fecha_prestamo,
                fecha_devolucion, tipo_publicacion):
        self.dni_lector = dni_lector
        self.codigo_publicacion = codigo_publicacion
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.tipo_publicacion = tipo_publicacion

class Datos_prestamo:
    def __init__(self, datos_lectores, datos_publicaciones):
        self.lista_prestamos  = []
        self.datos_lectores = datos_lectores
        self.datos_publicaciones = datos_publicaciones
        self.prestamos = 0
    
    def Guardar_prestamos(self,dni_lector , codigo_publicacion,fecha_prestamo, fecha_devolucion, tipo_publicacion):
        prestamos = {'DNI': dni_lector, 'CODIGO': codigo_publicacion, 
                'FECHA PRESTAMO': fecha_prestamo, 'FECHA DEVOLUCION': fecha_devolucion , 'TIPO PUBLICACION': tipo_publicacion}
        self.lista_prestamos.append(prestamos)
    
    def Mostrar_Prestamos(self):
        if not self.lista_prestamos:
            print("-" * 60)
            print("no hay prestamos registrados")
            print("-" * 60)
        else:
            print("\nLISTA DE PRESTAMOS REGISTRADOS\n")
            print(tabulate(self.lista_prestamos,headers = "keys", tablefmt = "grid"))
    
    def Registrar_Prestamos(self):
        while True:
            dni_lector = input("ingrese el dni del lector a registrar el  prestamo : ")
            if len(dni_lector) == 8 and dni_lector.isdigit():
                break
            else:
                print("dni incorrecto")
            
        if any(lector["DNI"] == dni_lector for lector in self.datos_lectores.lista_lectores):      
            while True:
                codigo_publicacion = input("Ingrese el codigo de la publicacion : ")
                if codigo_publicacion.isdigit() and len(codigo_publicacion)== 8:
                    break
                else:
                    print("codigo de publicacion incorrecto")
            while True:
                print("\nTIPO DE PUBLICACION\n")
                print("1. Revista \n2. Periodico  \n3. Libro")
                opcion =  int(input("selecione el tipo de publicaion"))
                if opcion == 1 :
                    tipo_publicacion = 'Revista'
                    break
                elif opcion == 2 :
                    tipo_publicacion = 'Periodico'
                    break
                elif opcion == 3 :
                    tipo_publicacion = 'Libro'
                    break
                else:
                    print("opcion fuera de rango")
                
            while True:
                try:
                    fecha_ingresada =input("Ingrese la fecha del prestamo (DD/MM/AAAA): ")
                    fecha_prestamo = datetime.strptime(fecha_ingresada, '%d/%m/%Y')
                    self.prestamos +=1
                    break
                except ValueError:
                    print("Fecha incorrecta")
                    
            while True:
                try:
                    print("1.Pendiente\n2.Entregado")
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        devolucion = 'Pendiente'
                        break
                    elif opcion == 2:
                        devolucion == 'Entregado'
                        break
                    else:
                        print("opcion fuera de rango")
                        opcion = int(input("Ingrese una opcion: "))
                except ValueError:
                    print("Fecha incorrecta") 
            
            self.Guardar_prestamos(dni_lector, codigo_publicacion,fecha_prestamo,devolucion,tipo_publicacion)
            print("\nREGISTRO DE PRESTAMO ACTUALIZADO CON EXITO\n")
            print("---" * 30)
            print("\nCOMPROBANTE DE PRESTAMO")
            print("---" * 30)
            print(f"DNI LECTOR : {dni_lector}")
            print(f"CODIGO DE PUBLICACION: {codigo_publicacion}")
            print(f"TIPO DE PUBLICACION : {tipo_publicacion}")
            print(f"FECHA PRESTAMO: {fecha_prestamo.strftime('%Y-%m-%d')}")
            print(f"ESTADO DE PRESTAMO: {devolucion}")

            # Definir fecha de devolución según el tipo de publicación
            if tipo_publicacion == "Revista" or tipo_publicacion == "Periodico":
                fecha_devolver = fecha_prestamo + timedelta(days=5)
            elif tipo_publicacion == "Libros":
                fecha_devolver = fecha_prestamo + timedelta(days=14)
            else:
                fecha_devolver = "Tipo no válido"
            print("FECHA DE DEVOLUCIÓN :", end=" ")

            if isinstance(fecha_devolver, datetime):
                print(fecha_devolver.strftime('%Y-%m-%d'))
            else:
                print(fecha_devolver)
            print("---" * 30)

        else:
            print("No se encuentra el lector en la base de datos")  
    

    def cambiar_datos_prestamo(self):
        fecha_ingresada = input("Ingrese la fecha del préstamo (DD/MM/AAAA): ")
        try:
            fecha_prestamo = datetime.strptime(fecha_ingresada, '%d/%m/%Y')
        except ValueError:
            print("❌ Fecha incorrecta. Use el formato DD/MM/AAAA.")
            return

        # Buscar el préstamo con la fecha exacta ingresada
        prestamo_encontrado = None
        for prestamo in self.lista_prestamos:
            if prestamo['FECHA PRESTAMO'].date() == fecha_prestamo.date(): # Para comparar solo fecha mas no la hora exacta
                prestamo_encontrado = prestamo
                break

        if not prestamo_encontrado:
            print("❌ No se encontró un préstamo con esa fecha exacta.")
            return

        print("\n📌 MENU DE ACTUALIZACIÓN DE DATOS EN LOS PRÉSTAMOS")
        print("1. Modificar el DNI")
        print("2. Modificar el código de publicación")
        print("3. Modificar la fecha del préstamo")

        while True:
            try:
                opcion = int(input("Ingrese una opción: "))
                if 1 <= opcion <= 3:
                    break
                else:
                    print("⚠️ Opción incorrecta, intente de nuevo.")
            except ValueError:
                print("⚠️ Entrada inválida. Ingrese un número del 1 al 3.")

        # 🔹 Opción 1: Modificar el DNI (Verifica que esté en la base de datos)
        if opcion == 1:
            while True:
                nuevo_dni = input("Ingrese el nuevo DNI para el préstamo: ")
                if len(nuevo_dni) == 8 and nuevo_dni.isdigit():
                    if any(lector["DNI"] == nuevo_dni for lector in self.datos_lectores.lista_lectores):
                        prestamo_encontrado['DNI'] = nuevo_dni  # ✅ Asignación corregida
                        print("✅ DNI actualizado con éxito.")
                        break
                    else:
                        print("❌ El DNI ingresado no está registrado en la base de datos.")
                else:
                    print("⚠️ El DNI es incorrecto, intente de nuevo.")

        # 🔹 Opción 2: Modificar el código de publicación (Verifica que esté en la base de datos)
        elif opcion == 2:
            while True:
                nuevo_codigo = input("Ingrese el nuevo código de publicación: ")
                if any(pub['CODIGO'] == nuevo_codigo for pub in self.datos_publicaciones.lista_publicaciones):
                    prestamo_encontrado['CODIGO'] = nuevo_codigo  # ✅ Asignación corregida
                    print("✅ Código de publicación actualizado con éxito.")
                    break
                else:
                    print("❌ El código ingresado no pertenece a ninguna publicación registrada.")

        # 🔹 Opción 3: Modificar la fecha del préstamo
        elif opcion == 3:
            while True:
                nueva_fecha = input("Ingrese la nueva fecha del préstamo (DD/MM/AAAA): ")
                try:
                    nueva_fecha_prestamo = datetime.strptime(nueva_fecha, '%d/%m/%Y')
                    prestamo_encontrado['FECHA PRESTAMO'] = nueva_fecha_prestamo  # ✅ Asignación corregida
                    print("✅ Fecha de préstamo actualizada con éxito.")
                    break
                except ValueError:
                    print("❌ Fecha incorrecta. Use el formato DD/MM/AAAA.")

        print("-" * 60)

class Devoluciones:
    def __init__(self, fecha_devolucion, dni_lector,codigo_publicacion):
        self.fecha_devolucion = fecha_devolucion
        self.dni_lector = dni_lector
        self.codigo_publicacion = codigo_publicacion
        
class Datos_devoluciones:
    def __init__(self, datos_prestamos):
        self.lista_devoluciones = []
        self.lista_devoluciones_pendientes = []
        self.datos_prestamos = datos_prestamos
        self.devoluciones = 0
    
    def Guardar_devoluciones(self,fecha_devolucion, dni_lector,codigo_publicacion):
        devoluciones = {'FECHA DEVOLUCION': fecha_devolucion, 'DNI LECTOR': dni_lector , 'CODIGO DEVOLUCION': codigo_publicacion}
        self.lista_devoluciones.append(devoluciones)
    def Mostrar_devolucion(self):
        if not self.lista_devoluciones:
            print("-" * 60)
            print("No hay devoluciones registradas")
            print("-" * 60)
            return 
        else: 
            print("DEVOLCIONES REGISTRADOS")
            print(tabulate(self.lista_devoluciones, headers = "keys", tablefmt = "grid"))
    
    def Registrar_devoluciones(self):
        while True:
            try:
                fecha_ingresada =input("Ingrese la fecha del prestamo (DD/MM/AAAA): ")
                fecha_devolucion = datetime.strptime(fecha_ingresada.strip(), '%d/%m/%Y')
                break
            except ValueError:
                print("Fecha incorrecta")
        
        while True:
            dni_lector = input("Ingrese el dni del lector : ")
            if dni_lector.isdigit() and len(dni_lector) == 8:
                self.devoluciones +=1
                break
            else:
                print("dni incorrecto")
        while True:
            codigo_publicacion = input("ingrese el codigo de la publicacion : ")
            if codigo_publicacion.isdigit() and len(codigo_publicacion) == 8:
                break
            else:
                print("codigo de publicacion incorrecto")
    
        self.Guardar_devoluciones(fecha_devolucion, dni_lector, codigo_publicacion)
        for prestamo in self.datos_prestamos.lista_prestamos[:]:
            if prestamo["CODIGO"] == codigo_publicacion:
                self.datos_prestamos.lista_prestamos.remove(prestamo)
                
        print("DEVOLUCION REALIZADA CON EXITO")
        
        

class Validar_devolucion:
    def __init__(self, datos_devolucion, datos_prestamo ):
        self.datos_prestamo = datos_prestamo
        self.datos_devolucion = datos_devolucion
        self.lista_devoluciones_pendientes = []
    
    def devoluciones_pendientes(self):
        """
        Verifica los préstamos pendientes y registra aquellos que están fuera de fecha.
        """
        hoy = datetime.now()
        print("---"*30)
        print("\n🔍 VERIFICACIÓN DE DEVOLUCIONES PENDIENTES\n")

        for prestamo in self.datos_prestamo.lista_prestamos:
            try:
                # Aseguramos que la fecha de préstamo se almacene como string
                if isinstance(prestamo["FECHA PRESTAMO"], datetime):
                    fecha_prestamo_str = prestamo["FECHA PRESTAMO"].strftime("%d/%m/%Y")
                else:
                    fecha_prestamo_str = prestamo["FECHA PRESTAMO"]

                fecha_prestamo = datetime.strptime(fecha_prestamo_str, "%d/%m/%Y")
            except ValueError:
                print(f"⚠️ Error: Formato de fecha incorrecto en el préstamo {prestamo.get('CODIGO', 'Desconocido')}")
                continue
            
            rango_fecha = (hoy - fecha_prestamo).days  # Diferencia en días
            tipo_publicacion = prestamo["TIPO PUBLICACION"]
            codigo = prestamo["CODIGO"]
            titulo = prestamo.get("TITULO", "Desconocido")
            dni_lector = prestamo.get("DNI", "No registrado")
            fecha_devolucion = prestamo["FECHA DEVOLUCION"]

            if fecha_devolucion == "Pendiente":
                print(f"📌 Préstamo pendiente: Código {codigo}")
                print(f"   Tipo: {tipo_publicacion}")
                print(f"   Fecha préstamo: {fecha_prestamo_str}")

                # Verificar si ha excedido el plazo permitido
                limite_dias = {
                    "Periodico": 5,
                    "Revista": 5,
                    "Libro": 14
                }

                if tipo_publicacion in limite_dias and rango_fecha > limite_dias[tipo_publicacion]:
                    print(f"⚠️ ¡Este préstamo ha excedido el plazo de {limite_dias[tipo_publicacion]} días para {tipo_publicacion}!")
                else:
                    print("✅ El préstamo está dentro del plazo permitido.")
                print("---"*30)
            else:
                print(f"✔️ Préstamo devuelto: Código {codigo}")
                print(f"   Fecha devolución: {fecha_devolucion}")
            print("---"*30)


class RangoEdad:
    def __init__(self, datos_lectores, datos_publicaciones):
        self.datos_lectores = datos_lectores
        self.datos_publicaciones = datos_publicaciones

    def Lectores_x_rango_de_edad(self):
        # Diccionario para almacenar los conteos por tipo de publicación
        conteo = {
            "Revista": {"Jóvenes": 0, "Adultos": 0, "Adultos Mayores": 0},
            "Periodico": {"Jóvenes": 0, "Adultos": 0, "Adultos Mayores": 0},
            "Libro": {"Jóvenes": 0, "Adultos": 0, "Adultos Mayores": 0}
        }

        if not self.datos_lectores.lista_lectores or not self.datos_publicaciones.lista_publicaciones:
            print("No hay suficientes datos de lectores o publicaciones para procesar.")
            return

        for publicacion in self.datos_publicaciones.lista_publicaciones:
            tipo_publicacion = publicacion["TIPO"]  # Puede ser "Revista", "Periódico" o "Libro"
            
            for lector in self.datos_lectores.lista_lectores:
                edad = lector.get("EDAD", 0)  # Obtener la edad del lector
                if 12<= edad <= 30:
                    conteo[tipo_publicacion]["Jóvenes"] += 1
                elif edad <= 50:
                    conteo[tipo_publicacion]["Adultos"] += 1
                else:
                    conteo[tipo_publicacion]["Adultos Mayores"] += 1

        # Preparar los datos para la tabla
        tabla = []
        for tipo in conteo:
            valores = conteo[tipo]
            tabla.append([tipo, valores["Jóvenes"], valores["Adultos"], valores["Adultos Mayores"]])

        # Imprimir la tabla de resultados
        print("\nLista de Usuarios Suscritos por Rango de Edad y Tipo de Publicación:")
        print(tabulate(tabla, headers=["Tipo de Publicación", "Jóvenes", "Adultos", "Adultos Mayores"], tablefmt="grid"))

class libro:
    def __init__(self,nombre, id_libro, genero,cantidad, precio):
        self.nombre = nombre
        self.id_libro = id_libro
        self.gnero = genero 
        self.cantidad = cantidad
        self.precio = precio
        
class Ventas:
    def __init__(self):
        self.lista_ventas = []
        self.lista_libros_registrados = []
        self.ventas = 0
        
    def guardar_libros(self,nombre, id_libro, genero,cantidad, precio):
        libro = {'NOMBRE': nombre, 'ID_LIBROS': id_libro,'GENERO': genero, 'CANTIDAD': cantidad,'PRECIO': precio}
        self.lista_libros_registrados.append(libro)
    
    def mostrar_libros(self):
        if not self.lista_libros_registrados:
            print("-" * 60)
            print("No hay registro de libros")
            print("-" * 60)
        else:
            print("LIBROS DISPONIBLES EN LA BIBLIOTECA\n")
            print(tabulate(self.lista_libros_registrados, headers = "keys", tablefmt ="grid"))
    def guardar_ventas(self,titulo,id_libro,precio,cantidad,pago_unico, pago_global):
        venta = {"TITULO" : titulo, "ID_LIBRO" : id_libro, "PRECIO":precio,"CANTIDAD": cantidad ,
                 "IMPORTE CANCELADO": pago_unico, "IMPORTE ACUMULADO": pago_global}
        self.lista_ventas.append(venta)
        
    def mostrar_ventas(self):
        if not self.lista_ventas:
            print("-" * 60)
            print("No hay ventas registrados")
            print("-" * 60)
        else:
            print("="*97)
            print("VENTAS REGISTRADAS".center(60))
            print(tabulate(self.lista_ventas, headers="keys", tablefmt="grid"))
            print("="*97)
    
        
    def registrar_libro(self):
        nombre = input("ingrese el nombre del libro : ").title()
        while True:
            id_libro = input("ingrese el codigo ID del libro ( 4 caracteres ) : ").title()
            if len(id_libro) == 4 and id_libro.isdigit():
                if not any(id["ID_LIBROS"] == id_libro for id in self.lista_libros_registrados):
                    break
                else:
                    print("El codigo no debe repetirse")
            else:
                print("Error el codigo debe tener 4 cacarteres y no debe estar repetido")
                    
        genero = input("Ingrese el genero literario al  que pertenece el libro : ").title()
        while True:
            cantidad = int(input("ingrese la cantidad de unidades a registrar : "))
            if cantidad > 0:
                break
            else:
                print("cantidad incorrecta , intente de nuevo")
        
        while True:
            precio = float(input("ingrese el precio por unidad : "))
            if precio > 0 :
                break
            else:
                print("el precio ingresado es incorrecto")
        self.guardar_libros(nombre, id_libro, genero, cantidad, precio)
        print("-"*60)
        print("LIBRO REGISTRADO CON EXITO")
        print("-"*60)
        
    def Vender_libros(self):
        pago_global = 0
        while True:
            # Solicitar código ID del libro
            while True:
                id_libro = input("Ingrese el código ID del libro a buscar: ")
                if len(id_libro) == 4 and id_libro.isdigit():
                    break
                else:
                    print("Código ID no válido. Debe tener 4 dígitos.")

            # Buscar el libro en la lista
            libro_encontrado = None
            for libro in self.lista_libros_registrados:
                if libro["ID_LIBROS"] == id_libro:
                    libro_encontrado = libro
                    break
            
            if not libro_encontrado:
                print(f"El libro con ID {id_libro} no ha sido encontrado.")
                continue

            # Mostrar datos del libro encontrado
            print("=" * 60)
            print("DATOS DEL LIBRO ENCONTRADO")
            print("=" * 60)
            print(f"NOMBRE   : {libro_encontrado['NOMBRE']}")
            print(f"ID       : {libro_encontrado['ID_LIBROS']}")
            print(f"GÉNERO   : {libro_encontrado['GENERO']}")
            print(f"CANTIDAD : {libro_encontrado['CANTIDAD']}")
            print(f"PRECIO   : {libro_encontrado['PRECIO']}")
            print("=" * 60)

            # Solicitar cantidad a comprar
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad de unidades a comprra : "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                    elif cantidad > libro_encontrado["CANTIDAD"]:
                        print(f"Solo hay {libro_encontrado['CANTIDAD']} unidades disponibles.")
                    else:
                        self.ventas +=1
                        break
                except ValueError:
                    print("Ingrese un número válido.")

            if cantidad == 0:
                print("Compra cancelada.")
                break

            # Calcular pagos
            pago_unico = cantidad * libro_encontrado["PRECIO"]
            libro_encontrado["CANTIDAD"] -= cantidad  # Actualizar stock
            pago_global += pago_unico
            # Mostrar boleta de venta
            print("=" * 60)
            print("BOLETA DE VENTA".center(50))
            print("=" * 30)
            print(f"TÍTULO DEL LIBRO   : {libro_encontrado['NOMBRE']}")
            print(f"ID DEL LIBRO       : {libro_encontrado['ID_LIBROS']}")
            print(f"PRECIO UNITARIO    : {libro_encontrado['PRECIO']}")
            print(f"CANTIDAD COMPRADA  : {cantidad}")
            print(f"PAGO DE COMPRA     : {pago_unico}")
            print(f"PAGO TOTAL         : {pago_global}")
            print("-" * 60)
            print("GRACIAS POR SU COMPRA << VENTA REALIZADA CON ÉXITO >>")
            print("LIBRERÍA #--- D I N O B O O K ---#")
            print("-" * 60)
            self.guardar_ventas(libro_encontrado["NOMBRE"], libro_encontrado["ID_LIBROS"],
                                libro_encontrado["PRECIO"], cantidad, pago_unico, pago_global)
            
            # Preguntar si desea continuar comprando
            while True:
                opcion = input("¿Desea continuar comprando? (si/no): ").strip().upper()
                if opcion in ["SI", "NO"]:
                    break
                print("Opción ingresada no reconocida. Intente nuevamente.")

            if opcion == "NO":
                print("<<<<  -- COMPRA DE LIBROS FINALIZADA, GRACIAS POR SU PREFERENCIA -- >>>>")
                break
    
    def Eliminar_libros(self):
        while True:
            id_libro = input("ingrese el ID del libro a eliminar :")
            if len(id_libro) == 4 and id_libro.isdigit():
                break
            else:
                print("el codigo debe ser de 4 caracteres nmericos")
        for libro in self.lista_libros_registrados:
            if libro["ID_LIBROS"] == id_libro:
                self.lista_libros_registrados.remove(libro)  # Eliminar correctamente el diccionario
                print("-" * 60)
                print(f"EL LIBRO CON ID {id_libro} HA SIDO ELIMINADO CON ÉXITO")
                print("-" * 60)
                return  # Salir de la función después de eliminar

        print("El ID no ha sido encontrado.")  # Se ejecuta solo si no se encontró el ID
            
class Graficos:
    def __init__(self,datos_lectores, datos_publicaciones, datos_prestamos, datos_devoluciones, datos_ventas):
        
        self.datos_lectores = datos_lectores 
        self.datos_publicaciones = datos_publicaciones 
        self.datos_prestamos = datos_prestamos
        self.datos_devoluciones  = datos_devoluciones 
        self.datos_ventas = datos_ventas
    def grafica_general(self):
        categorias = ['Lectores', 'Publicaciones', 'Prestamos','Devoluciones','ventas']
        cantidades = [self.datos_lectores.lectores,
                      self.datos_publicaciones.publicaciones,
                      self.datos_prestamos.prestamos,
                      self.datos_devoluciones.devoluciones,
                      self.datos_ventas.ventas
                    ]
        #graficar 
        plt.bar(categorias,cantidades, color = ['blue', 'green', 'skyblue', 'red','orange'])
        plt.xlabel("Tipo de Datos")
        plt.ylabel("Cantidades Registradas")
        plt.title("GRAFICO DE REGISTRO DE DATOS")
        
        # Mostrar el grafico
        plt.show( block = False)
        
def menu_principal():
    print("\nMENU PRINCIPAL\n")
    print("1.Registrar")
    print("2.Reportes")
    print("3.Presentacion")
    print("4.Opciones de soporte de datos")
    print("5.Venta de Libros")
    print("6.Mostrar Graficos")
    print("7.Salir")

def Submenu_registrar():
    print("\nMENU REGISTRAR\n")
    print("1. Publicacion")
    print("2. Lector")
    print("3. Prestamo")
    print("4. Devolucion")
    print("5. Salir")

def Submenu_reporte():
    print("\nREPORTES")
    print("1. Publicaciones")
    print("2. Lectores")
    print("3. Prestamos")
    print("4. Devoluciones")
    print("5. Listado de publicaciones pendientes de devolucion fuera de fecha")
    print("6. Numero de lectores por rango de edad para cada tipo de Publicacion ")
    print("7. Salir\n")
    
def submenu_inventario():
    print("REPORTES\n")
    print("1.Buscar Publicaciones")
    print("2.Eliminar Publicaciones")
    print("3.Buscar Lectores")
    print("4.Eliminar Lectores")
    print("5.Cambiar datos de la publicacion")
    print("6.Cambiar datos del prestamo")   
    print("7. Salir")

def menu_ventas():
    print("\nSECCION DE VENTA DE LIBROS")
    print("1.Registrar libros")
    print("2.Venta de libros")
    print("3.Mostrar libros")
    print("4.Mostrar ventas")
    print("5.Eliminar libros")
    print("6.Salir")

def menu_graficos():
    print('1. Grafico de tipo de publicaciones')
    print('2. Grafico General')
    print("3. Salir")
    
    
def Presentacion():
    print("                          .-                              ")
    print("                         -*-                              ")
    print("                 .      =**:           .                  ")
    print("               :-      =***=           .=.                ")
    print("              ==      .*****:           .+:               ")
    print("            =*.      :******=.          -*:               ")
    print("           =*=       :********-         .**.              ")
    print("           .**-       .*********=         +*=             ") 
    print("          =**-        -*********:        ***.             ")
    print("           +**=         -********+       .***-            ") 
    print("           ****.         :+*******       =***=            ")
    print("           ****+           -*****+      :****-            ") 
    print("           +****=           :****-     :*****:            ") 
    print("           -*****+:          +**+     -*****+             ")
    print("            +******=:        +*=   .-+******:             ") 
    print("            .********+-:.   .+: .-=********=              ") 
    print("             .+***********+++++***********=               ") 
    print("              .=*************************:                ")
    print("                :+*********************=.                 ")
    print("                  :=****************+-.                   ") 
    print("                     :-=++*****++=:.                      ")
    print("                            .                             ")

    print ("Integrantes: ")
    print ("Pena Roña Antony Yomar (U202421102)\n")
    input ("Presione una tecla para regresar...")
    
        
def main():
    lectores = Datos_lectores()
    publicaciones = Datos_publicaciones()
    prestamos = Datos_prestamo(lectores, publicaciones)
    devoluciones = Datos_devoluciones(prestamos)
    rango_edad = RangoEdad(lectores, publicaciones)
    devolucion_validar = Validar_devolucion(publicaciones, prestamos)
    ventas = Ventas()
    graficos = Graficos(lectores, publicaciones,prestamos,devoluciones,ventas)
    while True:
        menu_principal()
        try:
            opcion = input("Ingrese una opción: ").strip() 
            if not opcion: 
                print("La opción no puede estar vacía. Intente nuevamente.")
                continue
            opcion = int(opcion)
            
            if opcion ==1:
                while True:
                    Submenu_registrar()
                    try:
                        subopcion = input("Ingrese una opción: ").strip() 
                        if not subopcion: 
                            print("La opción no puede estar vacía. Intente nuevamente.")
                            continue
                        subopcion = int(subopcion)
                        if subopcion == 1:
                            publicaciones.Registrar_publicaciones()
                        elif subopcion == 2:
                            lectores.Registrar_lector()
                        elif subopcion == 3:
                            prestamos.Registrar_Prestamos()
                        elif subopcion == 4:
                            devoluciones.Registrar_devoluciones()
                        elif subopcion == 5:
                            print("Saliendo del submenu registrar.......")
                            break 
                        else:
                            print("opcion fuera de rango intente de nuevo")
                    except ValueError:
                        print("datos incorrectos, intente de nuevo")
                        
            elif opcion ==2:
                while True:
                    Submenu_reporte()
                    try:
                        subopcion = int(input("ingrese una opcion: "))
                        if subopcion == 1:
                            publicaciones.Publicaciones_registradas()
                            publicaciones.Mostrar_publicaciones()
                        elif subopcion == 2:
                            lectores.Lectores_registrados()
                            lectores.Mostrar_lectores()
                        elif subopcion == 3:
                            prestamos.Mostrar_Prestamos()
                        
                        elif subopcion == 4:
                            devoluciones.Mostrar_devolucion()
                        elif subopcion == 5:
                            devolucion_validar.devoluciones_pendientes()
                        elif subopcion == 6:
                            rango_edad.Lectores_x_rango_de_edad()
                        elif subopcion == 7:
                            print("Saliendo del submenu reportes ......")
                            break
                        else:
                            print("opcion fuera de rango intente de nuevo")
                    except ValueError:
                        print("datos incorrectos , intente de nuevo")
                        
            elif opcion == 3:
                Presentacion()
            elif opcion == 4:
                while True:
                    submenu_inventario()
                    subopcion = input("ingrese una opcion :").strip()
                    if not subopcion:
                        print("la opcion no debe estar vacia")
                        continue
                    subopcion = int(subopcion)
                    
                    if subopcion == 1:
                        publicaciones.Buscar_publicaciones()
                    elif subopcion == 2:
                        publicaciones.Eliminar_publicaciones()
                    elif subopcion == 3:
                        lectores.buscar_lectores()
                    elif subopcion == 4:
                        lectores.Eliminar_lectores()
                    elif subopcion == 5:
                        publicaciones.cambiar_datos_publicaciones()
                    elif subopcion == 6:
                        prestamos.cambiar_datos_prestamo()
                    elif subopcion == 7:
                        break
                    else:
                        print("opcion fuera de rangp")
            elif opcion == 5:
                while True:
                    menu_ventas()
                    subopcion = input("ingrese una opcion : ").strip()
                    if not subopcion :
                        print("la opcion no puede estar vacia")
                        continue
                    subopcion = int(subopcion)
                    
                    if subopcion == 1:
                        ventas.registrar_libro()
                    elif subopcion == 2:
                        ventas.Vender_libros()
                    elif subopcion == 3:
                        ventas.mostrar_libros()
                    elif subopcion == 4:
                        ventas.mostrar_ventas()
                    elif subopcion == 5:
                        ventas.Eliminar_libros()
                    elif subopcion ==6:
                        break
                    else:
                        print("opcion fuera de rango")
                        
            elif opcion == 6:
                while True:
                    menu_graficos()
                    subopcion = input("Ingrese una opcion : ").strip()
                    if not subopcion :
                        print("La opcion no puede estar vacia")
                        continue
                    subopcion = int(subopcion)
                    if subopcion == 1:
                        publicaciones.Graficar_publicaciones()
                    elif subopcion == 2:
                        graficos.grafica_general()
                    elif subopcion ==3:
                        break
                    else:
                        print("opcion fuera de tiempo")

            elif opcion == 7:
                print("Saliendo del sistema , gracias por utilizar nuestros servicios.....")
                break
            else:
                print("opcion fuera de rango")
                
        except ValueError:
            print("datos incorrectos")

# ejecutar el programa
if __name__ == "__main__":
    main()
