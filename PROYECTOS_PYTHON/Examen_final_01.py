# Sistema de gestión de reservas para un hotel
from tabulate import tabulate
from datetime import datetime
from random import randint
import pandas as pd

# Clase Habitacion (objeto de cada habitación)
class Habitacion:
    def __init__(self, numero, tipo, precio, disponibilidad):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = disponibilidad

# Clase para gestionar habitaciones
class RegistroHabitaciones:
    def __init__(self):
        self.lista_habitaciones = []

    def guardar_habitacion(self, numero, tipo, precio, disponibilidad):
        habitacion = Habitacion(numero, tipo, precio, disponibilidad)  # Crear objeto
        self.lista_habitaciones.append(habitacion)  # Guardar en lista

    def mostrar_habitaciones(self):
        if not self.lista_habitaciones:
            print("No hay habitaciones registradas")
        else:
            print("-" * 30)
        print("HABITACIONES REGISTRADAS:")
        print("-" * 30)

        data = []
        for h in self.lista_habitaciones:
            fila = [h.numero, h.tipo, h.precio, h.disponibilidad]
            data.append(fila)
        print(tabulate(data, headers=["NUMERO", "TIPO", "PRECIO", "DISPONIBILIDAD"], tablefmt="grid"))
        print("-" * 30)
        print("Total de habitaciones:", len(self.lista_habitaciones))
        print("-" * 30)

    def Registrar_habitacion(self):
        print("-" * 30)
        print("REGISTRO DE CLIENTES")
        print("-" * 30)
        
        while True:
            while True:
                numero = input("Ingrese el número de la habitación a reservar: ")
                if numero.isdigit():
                    numero = int(numero)
                    if 1 <= numero <= 1000 and not any(n.numero == numero for n in self.lista_habitaciones):
                        break 
                print("❌ Error: Ingrese un número válido y disponible (1-1000).")

            while True:
                tipo = input("Ingrese el tipo de habitacion (Simple/Doble/Triple): ")
                if tipo.lower() in ["simple", "doble", "triple"]:
                    break
                else:
                    print("Ingrese un tipo de habitacion valido (Simple/Doble/Triple)")
            
            while True:
                precio = float(input("Ingrese el precio de la habitacion: "))
                if precio > 0:
                    break
                else:
                    print("Ingrese un precio valido mayor a 0")
            while True:
                disponibilidad = input("Ingrese si la habitacion esta disponible (Si/No): ")
                if disponibilidad.lower() in ["si", "no"]:
                    break
                else:
                    print("Ingrese si la habitacion esta disponible (Si/No)")
            
            print("-"*60)
            print("Habitacion registrada con exito")
            print("-"*60)
            self.guardar_habitacion(numero, tipo, precio, disponibilidad)
            opcion  = input("Desea Registrar  la habitacion (SI/N0):").upper()
            if opcion == "NO":
                return 
            else:
                print()
                print("-"*60)
                print("ESTAMOS REGISTRANDO NUEVA HABITACION")
                print("-"*60)
    
    def Disponibilidad(self):
        contador = 0
        print("-"*60)
        print("HABITACIONES DISPONIBLES")
        print("-"*60)
        if not self.lista_habitaciones:
            print("No hay publicaciones Registradas")
        else:
            for reserva in self.lista_habitaciones:
                
                if reserva.disponibilidad == "si":
                    contador += 1
                    data = []
                    fila = [reserva.numero, reserva.tipo, reserva.precio, reserva.disponibilidad]
                    data.append(fila)
                    print(tabulate(data, headers=["NUMERO", "TIPO", "PRECIO", "DISPONIBILIDAD"], tablefmt="grid"))
                    print("-" * 30)
                    print("Total de habitaciones disponibles :",contador)
                    print("-" * 30)
                        
                

# Clase Cliente
class Cliente:
    def __init__(self, nombre,dni, correo_electronico, telefono):
        self.nombre = nombre
        self.dni = dni
        self.correo_electronico = correo_electronico
        self.telefono = telefono

class cliente_vip:
    def __init__(self, dni, nombre, codigo_cliente, correo_electronico , telefono):
        self.dni = dni 
        self.nombre = nombre
        self.codigo_cliente = codigo_cliente
        self.correo_electronico = correo_electronico
        self.telefono = telefono

# Clase para gestionar clientes
class RegistroClientes:
    def __init__(self):
        self.lista_clientes = []
        self.lista_clientes_vip = []

    def guardar_cliente(self,nombre,dni ,correo_electronico, telefono):
        cliente = Cliente(nombre,dni,correo_electronico, telefono)  # Crear objeto cliente
        self.lista_clientes.append(cliente)  # Guardar en lista

    def guardar_vip(self,dni, nombre, codigo_cliente,telefono, correo_vip):
        cliente = cliente_vip(dni,nombre, codigo_cliente,telefono, correo_vip)
        self.lista_clientes_vip.append(cliente)
    
    def mostrar_clientes_vip(self):
        if not self.lista_clientes_vip:
            print("No hay clientes registrados")
        else:
            print("-" * 30)
            print("CLIENTES REGISTRADOS:")
            print("-" * 30)
            data = [[c.dni, c.nombre, c.codigo_cliente, c.correo_electronico, c.telefono] for c in self.lista_clientes_vip]
            print(tabulate(data, headers=["DNI","NOMBRE", "CODIGO","CORREO ELECTRONICO", "TELÉFONO"], tablefmt="grid"))
            print("-" * 30)
            print("Total de clientes VIP :", len(self.lista_clientes_vip))
            print("-" * 30)
    def mostrar_clientes(self):
        if not self.lista_clientes:
            print("No hay clientes registrados")
        else:
            print("-" * 30)
            print("CLIENTES REGISTRADOS:")
            print("-" * 30)
            data = [[c.nombre, c.dni, c.correo_electronico, c.telefono] for c in self.lista_clientes]
            print(tabulate(data, headers=["NOMBRE","DNI", "EMAIL", "TELÉFONO"], tablefmt="grid"))
            print("-" * 30)
            print("Total de clientes:", len(self.lista_clientes))
            print("-" * 30)
    
    def Registrar_clientes(self):
        print("-" * 30)
        print("REGISTRO DE CLIENTES")
        print("-" * 30)
        
        while True:
            while True:
                nombre = input("Ingrese el nombre y apellidos del cliente: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacio")
                else:
                    break
            
            while True:
                dni = input("Ingrese el dni del cliente : ")
                if not (len(dni) == 8 and dni.isdigit()):
                    print("Error, El dni debe ser de 8 digitos numericos")
                    continue
                if any(d.dni == dni for d in self.lista_clientes):
                    print("Este DNI ya esta registrado")
                    continue
                break
            

            while True:
                correo_electronico = input("Ingrese el correo electronico del cliente: ").strip()
                if not correo_electronico:
                    print("El correo electronico no puede estar vacio")
                else:
                    break
            
            while True:
                telefono = input("Ingrese el telefono del cliente: ")
                if len(telefono) == 9 and telefono.isdigit():
                    break
                else:
                    print("El telefono debe tener 9 digitos y solo contener numeros")
            
            print("-"*60)
            print("Cliente registrado con exito")
            print("-"*60)
            self.guardar_cliente(nombre, dni,correo_electronico, telefono)
            opcion  = input("Desea Registrar de nuevo cliente (SI/N0):").upper()
            if opcion == "NO":
                break
            else:
                print()
                print("-"*60)
                print("ESTAMOS REGISTRANDO NUEVO CLIENTE")
                print("-"*60)

    def Registrar_clientes_vip(self):
        while True:
            dni = input("Ingrese su DNI: ")
            if not(len(dni) == 8 and dni.isdigit()):
                print("Error, el dni debe ser de 8 digitos numericos")
                continue
            if any(d.dni == dni for d in self.lista_clientes_vip):
                print("Este DNI ya esta registrado")
                continue
            break
        
        nombre = input("Ingrese su nombre y apellidos: ").title()
        while True:
            codigo_usuario = input("Ingrese su codigo de cliente : ")
            if len(codigo_usuario) == 4 and codigo_usuario.isdigit():
                break
            else:
                print("Codigo incorrecto, intente de nuevo")
        
         # validar correo electronico
        while True:
            correo_vip =  input("Ingrese su correo electronico: ")
            if "@" in correo_vip and correo_vip[-3:] == "com":
                break
            else:
                print("datos ingresados incorrectos, inetente de nuevo...")

        # validar telefono

        while True:
            telefono = input("Ingrese su numero de telefono:")
            if  len(telefono) == 9  and telefono.isdigit() and  telefono[0] == "9":
                break
            else:
                print("Telefono incorrecto..")

        
        self.guardar_vip(dni,nombre, codigo_usuario, correo_vip, telefono)
        print("----->>>>> USUARIO VIP REGISTRADO CON EXITO <<<<<-----------")


# Clase Reserva
class Reserva:
    def __init__(self, cliente,dni_cliente, habitacion, fecha_llegada, fecha_salida, precio_total):
        self.cliente = cliente
        self.dni_cliente = dni_cliente
        self.habitacion = habitacion
        self.fecha_llegada = fecha_llegada
        self.fecha_salida = fecha_salida
        self.precio_total = precio_total

# Clase para gestionar reservas
class RegistroReservas:
    def __init__(self,habitaciones, clientes):
        self.lista_reservas = []
        self.habitaciones = habitaciones
        self.clientes = clientes

    def guardar_reserva(self, cliente,dni_cliente, habitacion, fecha_llegada, fecha_salida, precio_total):
        reserva = Reserva(cliente,dni_cliente, habitacion, fecha_llegada, fecha_salida, precio_total)
        self.lista_reservas.append(reserva)

    def mostrar_reservas(self):
        if not self.lista_reservas:
            print("No hay reservas registradas")
        else:
            print("-" * 30)
            print("RESERVAS REGISTRADAS:")
            print("-" * 30)
            data = [[r.cliente.nombre,r.dni_cliente, r.habitacion.numero, r.fecha_llegada, r.fecha_salida, r.precio_total]
                    for r in self.lista_reservas]
            print(tabulate(data, headers=["CLIENTE","DNI", "HABITACIÓN", "LLEGADA", "SALIDA", "PRECIO"], tablefmt="grid"))
            print("-" * 30)
            print("Total de reservas:", len(self.lista_reservas))
            print("-" * 30)
    
    def validar_dni(self):
        """Solicita y valida un DNI de 8 dígitos."""
        while True:
            dni_cliente = input("Ingrese el DNI del cliente a realizar la reserva: ")
            if len(dni_cliente) == 8 and dni_cliente.isdigit():
                return dni_cliente
            print("El DNI debe tener 8 dígitos y solo contener números.")

    def buscar_cliente(self, dni_cliente):
        """Busca un cliente en la lista de clientes."""
        for c in self.clientes.lista_clientes:
            if c.dni == dni_cliente:
                return c
        return None

    def validar_numero_habitacion(self):
        while True:
            numero_habitacion = input("Ingrese el número de la habitación a reservar: ")
            
            if not numero_habitacion.isdigit():
                print("❌ Error: Ingrese un número válido.")
                continue

            numero_habitacion = int(numero_habitacion)

            if not (1 <= numero_habitacion <= 1000):
                print("❌ Error: El número de habitación debe estar entre 1 y 1000.")
                continue

            if any(n.numero == numero_habitacion for n in self.lista_reservas):
                print("❌ Error: La habitación ya está reservada.")
                continue

            return numero_habitacion  # Devuelve la habitación válida y disponible

    def buscar_habitacion(self, numero_habitacion):
        """Busca una habitación disponible en la lista de habitaciones."""
        for h in self.habitaciones.lista_habitaciones:
            if h.numero == numero_habitacion:
                return h if h.disponibilidad.lower() == "si" else None
        return None

    def Registrar_reservas(self):
        print("-" * 30)
        print("REGISTRO DE RESERVAS")
        print("-" * 30)

        # Validar DNI
        dni_cliente = self.validar_dni()

        # Buscar cliente
        cliente = self.buscar_cliente(dni_cliente)
        if cliente is None:
            print("El cliente no está registrado en el Hotel.")
            return  # Salimos de la función si el cliente no existe

        # Validar habitación
        numero_habitacion = self.validar_numero_habitacion()

        # Buscar habitación disponible
        habitacion = self.buscar_habitacion(numero_habitacion)
        if habitacion is None:
            print("La habitación no está disponible o no existe.")
            return  # Salimos de la función si la habitación no está disponible
        
        fecha_llegada = input("Fecha de llegada (DD-MM-YYYY): ")
        fecha_salida = input("Fecha de salida (DD-MM-YYYY): ")
        fecha_llegada = datetime.strptime(fecha_llegada, "%d-%m-%Y")
        fecha_salida = datetime.strptime(fecha_salida, "%d-%m-%Y")
        
        dias_estadia = (fecha_salida - fecha_llegada).days
        while True:
            precio_original = float(input("Ingrese el precio de la habitacion: "))
            if precio_original > 0:
                break
            else:
                print("Ingrese un precio valido mayor a 0")
        opcion = input("Desea aceptar la reservacion (SI: aceptar No: Cancelar): ")
        if opcion.upper() == "NO":
            print("-"*60)
            print("Reserva cancelada")
            print("-"*60)
            return
        else:
            for h in self.habitaciones.lista_habitaciones:
                if h.numero == numero_habitacion:
                    h.disponibilidad = "No"
                    break
                
            # Verificar si el precio existe en alguna habitación
            precio_encontrado = any(h.precio == precio_original for h in self.habitaciones.lista_habitaciones)
            precio_total = 0
            if not precio_encontrado:
                print("El precio no coincide con el registro del hotel.")
            else:
                print("😎😎😎 Precio válido, continuando con la reserva. 😎😎😎")
                precio_total = dias_estadia * precio_original
                self.guardar_reserva(cliente,dni_cliente,habitacion, fecha_llegada, fecha_salida, precio_total)
            
                # Generar y mostrar código de reserva
                codigo_reserva = randint(100000, 999999)
            
                # Confirmación de reserva
                print("-" * 60)
                print("Reserva registrada con éxito")
                print("-" * 60)
                print("-"*60)
                print("COMPROBANTE DE RESERVA DEL HOTEL '*CIELO AZUL*'")
                print("-"*60)
                print("Código de reserva   :", codigo_reserva)
                print("Nombre del cliente  :", cliente.nombre)
                print("DNI del cliente     :", cliente.dni)
                print("Número de habitación:", habitacion.numero)
                print("Fecha de llegada    :", fecha_llegada.strftime("%d-%m-%Y"))
                print("Fecha de salida     :", fecha_salida.strftime("%d-%m-%Y"))
                print("Dias de estadía     :", dias_estadia)
                print("Precio base sin DSCT:", precio_total , " $")
                print("-"*60)
        
    def Cancelar_reserva(self):
        print("-" * 30)
        print("CANCELAR RESERVAS")
        print("-" * 30)
        while True:
            dni = input("Ingrese el DNI del cliente a cancelar la reserva: ")
            if len(dni) == 8 and dni.isdigit():
                break
            print("El DNI debe tener 8 dígitos y solo contener números.")
        
        if not self.lista_reservas:
            print("⚠ No hay reservas registradas.")
            return
        
        for r in self.lista_reservas:
            if r.dni_cliente == dni:
                self.lista_reservas.remove(r)# Eliminar la reserva
                habitacion = r.habitacion
                habitacion.disponibilidad = "Si"
                print("-" * 60)
                print("✅ Reserva cancelada con éxito.")
                print("-" * 60)
                return  # Salir de la función una vez eliminada la reserva

        print("⚠ La reserva no existe o no ha sido realizada por este cliente.")
        

# Clase Pago
class Pago:
    def __init__(self, monto_total, fecha_pago, metodo_pago,reserva_encontrada):
        self.monto_total = monto_total
        self.fecha_pago = fecha_pago
        self.metodo_pago = metodo_pago
        self.reserva_encontrada = reserva_encontrada

class RegistroPagos:
    def __init__(self, registro_reservas):
        self.lista_pagos = []
        self.registro_reservas = registro_reservas

    def guardar_pagos(self, monto_total, fecha_pago, metodo_pago, reserva_encontrada):
        pago = Pago(monto_total, fecha_pago, metodo_pago, reserva_encontrada)
        self.lista_pagos.append(pago)
        print("-" * 60)
        print("Pago registrado con éxito")
        print("-" * 60)
        print("-"*60)
    
    def Mostrar_pagos(self):
        if not self.lista_pagos:
            print("🚩🚩 No hay pagos registrados")
            return
        else:
            print("-" * 30)
            print("PAGOS REGISTRADOS:")
            print("-" * 30)
            for p in self.lista_pagos:
                print("-" * 60)
                print("Monto total        :", p.monto_total, " $")
                print("Fecha de pago      :", p.fecha_pago)
                print("Método de pago     :", p.metodo_pago)
                print("Reserva encontrada :", p.reserva_encontrada)
                print("-" * 60)
            

    def Registrar_pago(self):
        print("-" * 30)
        print("REGISTRO DE PAGOS")
        print("-" * 30)

        # Validar monto total
        while True:
            try:
                monto_total = float(input("Ingrese el monto total a pagar: "))
                if monto_total > 0:
                    break
                else:
                    print("⚠ Ingrese un monto válido mayor a 0.")
            except ValueError:
                print("⚠ Error: Ingrese un número válido.")

        # Validar fecha de pago
        while True:
            fecha_pago = input("Ingrese la fecha de pago (DD-MM-YYYY): ")
            try:
                fecha_pago = datetime.strptime(fecha_pago, "%d-%m-%Y").strftime("%Y-%m-%d")
                break
            except ValueError:
                print("⚠ Error: Ingrese una fecha válida en el formato correcto (DD-MM-YYYY).")

        # Validar método de pago
        while True:
            try:
                metodo_pago = int(input("Ingrese el método de pago (1: Tarjeta, 2: Efectivo): "))
                if metodo_pago in [1, 2]:
                    break
                else:
                    print("⚠ Opción inválida. Elija 1 para Tarjeta o 2 para Efectivo.")
            except ValueError:
                print("⚠ Error: Ingrese un número válido (1 o 2).")

        # Obtener la reserva a pagar
        dni_cliente = input("Ingrese el DNI del cliente para buscar su reserva: ")
        reserva_encontrada = None

        for p in self.registro_reservas.lista_reservas:
            if p.cliente.dni == dni_cliente:
                reserva_encontrada = p
                break

        if reserva_encontrada is None:
            print("⚠ No se encontró una reserva para el DNI ingresado.")
            return

        # Aplicar descuento
        if metodo_pago == 1:
            metodo_pago_str = "Tarjeta"
            monto_final = monto_total * 0.80  # 20% de descuento
        else:
            metodo_pago_str = "Efectivo"
            monto_final = monto_total * 0.85  # 15% de descuento

        reserva_encontrada.precio_total = reserva_encontrada.precio_total  # Marcar la reserva como pagada

        # Guardar el pago
        self.guardar_pagos(monto_final, fecha_pago, metodo_pago_str, reserva_encontrada)

        # Mostrar confirmación
        print("-" * 60)
        print(f"✅ Pago registrado con éxito. Monto final: ${monto_final:.2f}")
        print(f"📅 Fecha de pago: {fecha_pago}")
        print(f"💳 Método de pago: {metodo_pago_str}")
        print("-" * 60)



class RegistroHotel:
    def __init__(self, RegistroHabitaciones, RegistroClientes, RegistroReservas):
        self.RegistroHabitaciones = RegistroHabitaciones
        self.RegistroClientes = RegistroClientes
        self.RegistroReservas = RegistroReservas
    
    print("-" * 80)
    def generar_reporte(self):
        if not self.RegistroReservas.lista_reservas:
            print("No hay reservas para generar reportes.")
            return
        
        datos = []
        for reserva in self.RegistroReservas.lista_reservas:
            datos.append({
                "Cliente": reserva.cliente.nombre,  # Acceder correctamente al nombre del cliente
                "Habitación": reserva.habitacion.numero,  # Acceder correctamente a la habitación
                "Monto Total": reserva.precio_total,  # Acceder correctamente al monto total
                "Fecha Llegada": reserva.fecha_llegada.strftime('%Y-%m-%d'),  # Formato correcto de fecha
                "Fecha Salida": reserva.fecha_salida.strftime('%Y-%m-%d')
            })

        df = pd.DataFrame(datos) 
        print("-"*80)
        print("\nReporte de Reservas:")
        print("-"*80)
        print(df)
        # Análisis estadístico
        ingresos_totales = df["Monto Total"].sum()
        
        total_habitaciones = len(self.RegistroHabitaciones.lista_habitaciones)
        if total_habitaciones > 0:
            ocupacion = (len(self.RegistroReservas.lista_reservas) / total_habitaciones * 100)
        else:
            ocupacion = 0  # Evitar división por cero
        print("-"*80)
        print("\nAnálisis Estadístico:")
        print("========================= ")     
        print(f"\nIngresos Totales: S/ {ingresos_totales:.2f}")
        print(f"Porcentaje de Ocupación: {ocupacion:.2f}%")
        print("-"*80)



def Menu_principal():
    print("-" * 30)
    print("MENU PRINCIPAL")
    print("-" * 30)
    print("1. Registros")
    print("2. Reportes")
    print("3. Salir")
    print("-" * 30)

# Menú de registro")
def Menu_registro():
    print("-" * 30)
    print("1. Registrar Habitaciones")
    print("2. Registrar Clientes")
    print("3. Registrar Reservas")
    print("4. Registrar Pagos")
    print("5. Salir")
    print("-" * 30)

# Menú principal
def Menu_reportes():
    print("-" * 30)
    print("MENU REPORTES")
    print("-" * 30)
    print("1. Mostrar Habitaciones")
    print("2. Mostrar Clientes")
    print("3. Mostrar reservas")
    print("4. Mostrar pagos")
    print("5. Consultar Disponibilidad de habitaciones")
    print("6. Reportes de ingresos y ocupación del hotel")
    print("7. Cancelar Reserva")
    print("8. Salir")
    print("-" * 30)

def Menu_opcionales():
    print("1. Registrar quejas en el servicio del hotel")
    print("2. Reportar daños en las habitaciones")
    print("3. Salir")
# Función principal
def main():
    habitacion = RegistroHabitaciones()
    cliente = RegistroClientes()
    reserva = RegistroReservas(habitacion,cliente)
    pago = RegistroPagos(reserva)
    hotel = RegistroHotel(habitacion,cliente, reserva)
    

    while True:
        while True:
            Menu_principal()
            while True:
                opcion = input("Ingrese una opción: ").strip()
                if not opcion:
                    print("La opcion no puede estar vacia..")
                    continue
                else:
                    break 
            opcion = int(opcion)

            if opcion == 1:
                while True:
                    Menu_registro()
                    while True:
                        subopcion = input("Ingrese una opción: ").strip()
                        if not subopcion:
                            print("la opcion no puede estar vacia")
                            continue 
                        else:
                            break
                    subopcion = int(subopcion)
                    if subopcion == 1:
                        habitacion.Registrar_habitacion()
                    elif subopcion == 2:
                        print("--"*20)
                        print("1. Registrar cllientes VIP")
                        print("2. Registrar clientes normales")
                        while True:
                            opc = input("ingrese una opcion: ").strip()
                            if not opc:
                                print("la opcion no puede estar vacìa")
                                continue
                            else:
                                break
                        opc = int(opc)
                        
                        if opc == 1:
                            cliente.Registrar_clientes_vip()
                        elif opc ==2:
                            cliente.Registrar_clientes()
                        else:
                            print("Opcion fuera de rango")
                    elif subopcion == 3:
                        reserva.Registrar_reservas()
                    elif subopcion == 4:
                        pago.Registrar_pago()
                    elif subopcion == 5:
                        print("Saliendo al menu principal")
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")
            elif opcion == 2:
                while True:
                    Menu_reportes()
                    while True:
                        subopcion = input("Ingrese una opción: ").strip()
                        if not subopcion:
                            print("La opcion no puede estar vacia")
                            continue 
                        else:
                            break
                    subopcion = int(subopcion)
                    
                    if subopcion == 1:
                        habitacion.mostrar_habitaciones()
                    elif subopcion == 2:
                        print("--"*20)
                        print("1. Mostrar cllientes VIP")
                        print("2. Mostrar clientes normales")
                        while True:
                            opc = input("ingrese una opcion: ").strip()
                            if not opc:
                                print("la opcion no puede estar vacìa")
                                continue
                            else:
                                break
                        opc = int(opc)
                        if opc == 1:
                            cliente.mostrar_clientes_vip()
                        elif opc == 2:
                            cliente.mostrar_clientes()
                        else:
                            print("opcion fuera de rango")
                            
                    elif subopcion == 3:
                        reserva.mostrar_reservas()
                    elif subopcion == 4:
                        pago.Mostrar_pagos()
                    elif subopcion == 5:
                        habitacion.Disponibilidad()
                    elif subopcion == 6:
                        hotel.generar_reporte()
                    elif subopcion == 7:
                        reserva.Cancelar_reserva()
                    elif subopcion == 8:
                        print("Saliendo al menu principal")
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")
                        continue
            elif opcion == 3:
                print("Saliendo del programa")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                continue
            
# Ejecutar el programa
main()
