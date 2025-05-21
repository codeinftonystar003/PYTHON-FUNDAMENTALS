# -*- coding: latin-1 -*- 

from tabulate import tabulate
from datetime import datetime
#----Revisado final-------------
#---------------------------- Listas para registros---------------------------------------------
# lista de mesas y mozos
Lista_mesas= []
Lista_mozos= []
# ----------------------------Lista para pedidos-----------------------------------------------
#lista general
lista_clientes = []
#Listas dentro de los clientes
lista_platos = []
lista_postres = []
lista_bebidas = []
lista_h_pedido = []
lista_h_maxima = []
lista_h_entrega = []
#--------------------------------- Listas para pagos---------------------------------------------
dato_pago_mesa=[]
pagos_finales=[]

# TODO: Antony Yomar Peña Roña ------------------------------------------------------------------

def Guardar_mesas(numero_mesa, zona_mesa, capacidad_mesa, estado_mesa):
    mesas = { "numero_mesa": numero_mesa,
                "zona_mesa": zona_mesa,
                "capacidad_mesa": capacidad_mesa,
                "estado_mesa": estado_mesa}
    Lista_mesas.append(mesas)

def Mostrar_mesas():
    if not Lista_mesas:
        print("No hay mesas registradas")
    else:
        print("Mesas registradas:")
        print(tabulate(Lista_mesas, headers="keys", tablefmt="grid"))      

def Guardar_mozos( id_mozo, nombre_mozo, telefono_mozo, estado_mozo, capacidad_mozo):
    mozos = { "id_mozo": id_mozo,
                "nombre_mozo": nombre_mozo,
                "telefono_mozo": telefono_mozo,
                "estado_mozo": estado_mozo,
                "capacidad_mozo": capacidad_mozo,
                "mesa_asignadas": [] 
                }
    Lista_mozos.append(mozos)

def Mostrar_mozos():
    if not Lista_mozos:
        print("No hay mozos registrados")
    else:
        print("Mozos registrados:")
        print(tabulate(Lista_mozos, headers="keys", tablefmt="grid"))
         
def Registrar_mesas():
    print("Registro de mesas".center(80, "-"))
    print("-" * 80)
    
    while True:
        existe_mesa = False
        numero_mesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
        if 1<= numero_mesa <= 100:
            for  id  in Lista_mesas:
                if id["numero_mesa"] == numero_mesa:
                    existe_mesa = True
                    break
            
        if  not existe_mesa and 1<= numero_mesa <= 100:
            break
        else:
            print("Error, el numero de mesa no esta en rango o ya existe")
    
    while True:
        zona_mesa = input("Ingrese la zona de disponibilidad de la mesa (sala/terraza): ").lower()
        if zona_mesa in ["sala","terraza"]:
            break
        else:
            print("Error, la zona no es correcta")
            
    while True:
        try:
            capacidad_mesa = int(input("Ingrese la capacidad de la mesa (1 - 4): "))
            if 1<= capacidad_mesa <= 4:
                break
            else:
                print("Error, la capacidad de la mesa no es correcta")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estado_mesa = input("Ingrese el estado de la mesa (libre/ocupada/reservada): ").lower()
        if estado_mesa in ["libre","ocupada","reservada"]:
            break
        else:
            print("Error, el estado de la mesa no es correcto")
    print("-" * 80)
    print("Mesa registrada correctamente".center(80))
    print("-" * 80)
    Guardar_mesas(numero_mesa, zona_mesa, capacidad_mesa, estado_mesa)

def Registrar_mozos():
    print("-" * 80)
    print("Registro de mozos".center(80, "-"))
    print("-" * 80)
    
    while True:
        existe_mozo = False
        id_mozo = input("Ingrese el id del mozo (4 digitos): ")
        if len(id_mozo) == 4 and id_mozo.isdigit():
            for id in Lista_mozos:
                if id["id_mozo"] == id_mozo:
                    existe_mozo = True
                    break
            if not existe_mozo:
                break
            else:
                print("Error, el id del mozo ya existe")
        else:
            print("Error en los datos de ingreso")
            
            
    while True:
        nombre_mozo = input("Ingrese el nombre y apellido del mozo: ")
        contiene_num = False 
        for caracter in nombre_mozo:
            if caracter.isdigit():
                contiene_num = True
                print("El nombre no debe tener numeros")
                break
            
        if not contiene_num:
            break

        
    while True:
        telefono = False
        try:
            telefono_mozo = input("Ingrese el telefono del mozo (9 digitos): ")
            if len(telefono_mozo) == 9:
                for id in Lista_mozos:
                    if id["telefono_mozo"] == telefono_mozo:
                        telefono = True
                        break
                if not telefono:
                    break
                else:
                    print("El telefono del mozo ya existe")
            else:
                print("Error, el telefono del mozo no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estado_mozo = input("Ingrese el estado del mozo (activo/inactivo) sin espacios: ").lower()
        if estado_mozo in ["activo","inactivo"]:
            break
        else:
            print("Error, el estado del mozo no es correcto")
            
    capacidad_mozo = 4
    Guardar_mozos(id_mozo, nombre_mozo, telefono_mozo, estado_mozo, capacidad_mozo)
    print("-" * 80)
    print("Mozo registrado correctamente".center(80))
    print("-" * 80)

def Asignar_mozo():
    Mostrar_mozos()
    if not Lista_mozos:
        print("No hay mozos registrados")
        return
    while True:
        id_mozo = input("Ingrese el id del mozo a asignar (4 digitos): ")
        if len(id_mozo) == 4 and id_mozo.isdigit():
            break
        else:
            print("Error, el id del mozo no es correcto")
            
    mozo_selecc = None
    for id in Lista_mozos:
        if id["id_mozo"] == id_mozo :
            if id["estado_mozo"] == "activo":
                mozo_selecc = id
                break
            else:
                print("Error, el mozo no esta disponible")
                return
    else:
        print("Error, el id del mozo no esta registrado")
        return
    
    if len(mozo_selecc["mesa_asignadas"]) >= 4:
        print("-" * 80)
        print("Error, el mozo no puede atender mas mesas".center(80))
        print("-" * 80)
        return
    
    while True:
        try:
            numero_mesa = int(input("Ingrese el numero de mesa a reservar (1 - 100) sin espacios: "))
            if 1<= numero_mesa <= 100:
                break
            else:
                print("Error, el numero de mesa no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
    
            
    for id in Lista_mesas:
        if id["numero_mesa"] == numero_mesa:
            mesas_asig = id["numero_mesa"]
            if mesas_asig not in mozo_selecc["mesa_asignadas"]:
                if id["estado_mesa"] == "libre":
                    confir_pedido = input("¿Desea confirmar la reserva? (si/no): ").lower()
                    if confir_pedido == "si":
                        id["estado_mesa"] = "reservada"
                        print("-" * 80)
                        print("Mesa reservada correctamente".center(80))
                        print("-" * 80)
                        mozo_selecc["mesa_asignadas"].append(numero_mesa)
                        
                           # Cambiar estado del mozo a "inactivo" si tiene 4 mesas asignadas
                        if len(mozo_selecc["mesa_asignadas"]) == 4:
                            mozo_selecc["estado_mozo"] = "inactivo"
                            print("-" * 80)
                            print(f"El mozo {mozo_selecc['nombre_mozo']} ahora esta inactivo.".center(80))
                            print("-" * 80)
                        break    
                    elif confir_pedido == "no":
                        print("Reserva cancelada")
                        break
                    else:
                        print("Error, la opcion no es correcta")
                else:
                    print("Error, la mesa no esta disponible")
                    break
            else:
                print("Error, la mesa ya esta asignada")
                break
    else:
        print("La mesa no esta registrada")  

def Cambiar_mozo():
    Mostrar_mozos()
    if not Lista_mozos:
        print("No hay mozos registrados")
        return

    while True:
        id_mozo = input("Ingrese el id del mozo a cambiar (4 dígitos): ")
        id_nuevo_mozo = input("Ingrese el id del nuevo mozo (4 dígitos): ")
        if len(id_mozo) == 4 and id_mozo.isdigit() and len(id_nuevo_mozo) == 4 and id_nuevo_mozo.isdigit():
            break
        else:
            print("Error, ambos IDs deben ser numéricos de 4 dígitos")

    while True:
        try:
            numero_mesa = int(input("Ingrese el numero de mesa a cambiar mozo (1 - 100): "))
            if 1 <= numero_mesa <= 100:
                break
            else:
                print("Error, el numero de mesa debe estar entre 1 y 100")
        except ValueError:
            print("Error en el numero de mesa")
            return

    # Buscar el nuevo mozo
    nuevo_mozo = None
    for mozo in Lista_mozos:
        if mozo["id_mozo"] == id_nuevo_mozo:
            if mozo["estado_mozo"] == "activo":
                nuevo_mozo = mozo
                break
            else:
                print("Error, el nuevo mozo no esta disponible")
                return
    if nuevo_mozo is None:
        print("Error, el ID del nuevo mozo no esta registrado")
        return

    # Buscar el mozo actual y quitar la mesa
    mozo_actual = None
    for mozo in Lista_mozos:
        if mozo["id_mozo"] == id_mozo:
            mozo_actual = mozo
            if numero_mesa in mozo["mesa_asignadas"]:
                mozo["mesa_asignadas"].remove(numero_mesa)
                if len(mozo["mesa_asignadas"]) < 4:
                    mozo["estado_mozo"] = "activo"
                break
            else:
                print("Error, la mesa no esta asignada al mozo actual")
                return
    if mozo_actual is None:
        print("Error, el mozo actual no se encuentra registrado")
        return

    # Asignar la mesa al nuevo mozo
    if len(nuevo_mozo["mesa_asignadas"]) < 4:
        nuevo_mozo["mesa_asignadas"].append(numero_mesa)
        print("-" * 80)
        print("Cambio de mozo realizado correctamente".center(80))
        print("-" * 80)
    else:
        print("Error, el nuevo mozo no puede atender más mesas")
     
# ----------------------------- Alexis Huaman------------------------------------------------------------
#---------------------------(Registro de pedidos)
def cartas():
        print("--" * 30)
        print("<< BIENVENIDO AL MENU >>".center(60))
        print("Seleccionar que desea: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("[0. Salir]")
        
def carta_platos():
    platos = {
        1: ["Lomo Saltado", 35.00],
        2: ["Ceviche", 35.00],
        3: ["Causa limeña", 25.00],
        4: ["Arroz con pollo", 20.00],
        5: ["Aji de gallina", 20.00],
        6: ["Pollo a la brasa", 24.00],
        7: ["Papa Rellena", 25.00],
        8: ["Chicharron de pescado", 30.00],
        9: ["Tallarines verdes", 25.00],
        10: ["Tallarines Rojos", 25.00]
        }
    print("--" * 30)
    print("<< MENU DE PLATILLOS DE FONDO >>".center(60))
    print("--" * 30)
    print("Platillos:", " "*28, "Precio:")
    for i, (nombre_precios) in enumerate(platos.values(), start=1):
        print(f"{i}. {nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return platos

def carta_postres():
    postres= {
        1: ["Mazamorra morada", 12.00],
        2: ["Arroz con leche", 12.00],
        3: ["Suspiro a la limeña", 10.00],
        4: ["Picarones", 15.00],
        5: ["Alfajores", 10.00],
        6: ["Torta de chocolates", 18.00],
        7: ["Turron", 15.00],
        8: ["King kong de manjar blanco",12.00]
    }
    
    print("--" * 30)
    print("<< MENU DE POSTRES >>".center(60))
    print("Postres:", " "*30, "Precios:")
    for num, nombre_precios in enumerate(postres.values(),start=1):
        print (f"{num}.{nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return postres

def carta_bebidas():
    
    bebidas = {
        1: ["Chicha morada", 18.00],
        2: ["Chicha de jora", 18.00],
        3: ["CocaCola", 10.00],
        4: ["InkaCola", 10.00],
        5: ["Jugo natural", 10.00],
        6: ["Cafe", 6.00],
        7: ["Pisco Sour", 20.00],
        8: ["Chilcano de pisco", 18.00]
    }
    
    print("--" * 30)
    print("<< MENU DE BEBIDAS >>".center(60))
    print("--" * 30)
    print("Bebidas:", " "*30, "Precio:")
    for num, nombre_precios in enumerate(bebidas.values(), start=1):
        print(f"{num}.{nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return bebidas

def guardar_cliente(numero_mesa, mozo_asignado, lista_platos, lista_postres, lista_bebidas, lista_h_pedido, lista_h_maxima, lista_h_entrega): 
    cliente = {
        "N_Mesa": numero_mesa,
        "N_Mozo" : mozo_asignado,
        "plato" : lista_platos.copy(),
        "postre" : lista_postres.copy(),
        "bebida" : lista_bebidas.copy(),
        "hora_pedido" : lista_h_pedido.copy(),
        "hora_maxima" : lista_h_maxima.copy(),
        "hora_entrega" : lista_h_entrega.copy()
    }
    lista_clientes.append(cliente)

def mostrar_cliente():
    if not lista_clientes:
        print("La lista esta vacia")
    else:
        print("El mozo asignado es: ",lista_clientes[0]["N_Mozo"])
        
        print(tabulate(lista_clientes,headers="keys",tablefmt="grid"))

def registro_pedido():
    while True:
        try:
            existe_mesa = False
            numero_mesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
            if 1<= numero_mesa <= 100:
                for  id  in Lista_mesas:
                    if id["numero_mesa"] == numero_mesa:
                        existe_mesa = True
                        break
            if existe_mesa:
                break
            else:
                print("Error, el numero de mesa no es correcto") 
        except ValueError:
            print("Valor incorrecto")
    
    while True:
        print("--" * 30)
        print("<< BIENVENIDO AL MENU >>".center(60))
        print("Seleccionar que desea: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("4. Registrar hora de pedido (Necesario)")
        print("5. Registrar hora de entrega")
        print("[0. Salir]")
        opcion = int(input ("Ingresar opcion: "))
        
        if opcion == 1:
            platos = carta_platos()
            while True:
                opcion = int(input("Elegir opcion de plato: "))
                if 1<= opcion <= 10:
                    plato = platos[opcion] # platos[opcion] = nombre, precio
                    lista_platos.append(plato)
                    break
                else:
                    print("No existe opcion.")
                    
        elif opcion == 2:
            postres = carta_postres()
            while True:
                opcion = int(input("Elegir opcion del postre: "))
                if 1<= opcion <= 8:
                    postre = postres[opcion] # 
                    lista_postres.append(postre)
                    break
                else:
                    print("No existe opcion.")
        elif opcion == 3:
            bebidas = carta_bebidas()
            while True:
                opcion = int(input("Elegir opcion de bebida: "))
                if 1<= opcion <= 10:
                    bebida = bebidas[opcion]
                    lista_bebidas.append(bebida)
                    break
                
        elif opcion == 4:
            fecha_pedido = datetime.now()
            hora_pedido = fecha_pedido.hour
            minutos_pedido = fecha_pedido.minute
            print("--" * 30)
            print("--" * 30)
            print("<< HORA DE PEDIDO >>".center(60))
            print(f"Hora de pedido:  {hora_pedido} horas con {minutos_pedido} minutos.")
            if minutos_pedido + 30 >= 60:
                minutos_maximo = (minutos_pedido + 30) - 60
                hora_maxima = hora_pedido + 1      
                if hora_maxima > 24:
                    hora_maxima = (hora_pedido + 1) - 24
            else:
                
                hora_maxima = hora_pedido
                minutos_maximo = minutos_pedido + 30
            print("<< HORA DE MAXIMA DE ENTREGA >>".center(60))
            print(f"Hora maxima de entrega: {hora_maxima} horas con {minutos_maximo} minutos.")
            print("--" * 30)
            print("--" * 30)
            lista_h_pedido.append((hora_pedido, minutos_pedido))
            lista_h_maxima.append((hora_maxima, minutos_maximo))
            break
        
        elif opcion == 5:
            try:
                print("-"* 30)
                print("Ingresar la hora de entrega de su pedido (en formato 24h): ")
                hora_entrega = int(input("Ingresar hora: "))
                minuto_entrega = int(input("Ingresar minuto: "))
                if hora_entrega >= 0 and hora_entrega <= 24 and minuto_entrega >= 0 and minuto_entrega < 60:
                    for cliente in lista_clientes:
                        if cliente["N_Mesa"] == numero_mesa:
                            if cliente["hora_pedido"]:
                                hora_pedido, minuto_pedido = cliente["hora_pedido"][-1]
                                tiempo_pedido = hora_pedido * 60 + minuto_pedido
                                tiempo_entrega = hora_entrega * 60 + minuto_entrega
                                if tiempo_entrega > tiempo_pedido and tiempo_entrega <= 1440:
                                    print("-" * 30)
                                    print("<< HORA DE ENTREGA REGISTRADO CORRECTAMENTE >>".center(80))
                                    print("-" * 30)
                                    cliente["hora_entrega"].append((hora_entrega, minuto_entrega))
                                else:
                                    print("-" * 30)
                                    print("La hora de entrega debe ser mayor a la hora del pedido")
                                    print("-" * 30)
                            else:
                                print("-" * 30)
                                print("No hay una hora de pedido registrada")
                                print("-" * 30)
                            break
                    else:
                        print("-" * 30)
                        print("No hay un cliente registrado para esta mes")
                        print("-" * 30)
                else:
                    print("-" * 30)
                    print("Error con la hora introducida")
                    print("-" * 30)
            except ValueError:
                print("-" * 30)
                print("Valor incorrecto")
                print("-" * 30)
        elif opcion == 0:
            print("-" * 30)
            print("Regresando...")
            break
        else:
            print("Opcion no existente")
    mozo_asignado = None
    for mozo in Lista_mozos:
        if numero_mesa in mozo["mesa_asignadas"]:
            mozo_asignado = mozo["nombre_mozo"]
            break
    else:
        print("No hay un mozo asignado a esta mesa.")
        
    if lista_platos or lista_postres or lista_bebidas or lista_h_pedido or lista_h_maxima or lista_h_entrega:
        guardar_cliente(numero_mesa, mozo_asignado, lista_platos, lista_postres, lista_bebidas, lista_h_pedido, lista_h_maxima, lista_h_entrega)
        
    lista_platos.clear()
    lista_postres.clear()
    lista_bebidas.clear()
    lista_h_pedido.clear()
    lista_h_maxima.clear()
    lista_h_entrega.clear()

    
#TODO ------------------------------------- Alexis Huaman-----------------------------------------------------
#---------------------------(ELIMINAR PEDIDOS)
def eliminar_pedido(): 
    while True:
        print("--" * 30)
        print("<< ELIMINAR PEDIDOS >>".center(60))
        print("--" * 30)
        existe_mesa = False
        existe_cliente = False
        mesa = int(input("Ingrese el numero de mesa del cliente (si no desea precione 0): "))
        if mesa == 0:
            break
        if 1 <= mesa <= 100: 
            existe_mesa = True
            for cliente in lista_clientes:
                if mesa == cliente['N_Mesa']:
                    existe_cliente = True
                    break 
        if not existe_mesa:
            print("Error, el numero de mesa no es correcto")
            continue
        if not existe_cliente:
            print("Error, no hay un cliente registrado")
            continue
        print("-"* 30)
        print("Que es lo que desea eliminar: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("[0. Regresar]")
        elim = int(input("Ingrese la opcion: "))
        if elim == 1:
            if cliente["plato"] != []:
                print("Platos:")
                for i, pedido in enumerate(cliente["plato"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero del plato a eliminar (Salir = 0): "))
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["plato"]):
                        cliente["plato"].pop(eliminar-1)
                        print("Plato eliminado correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de plato no es correcto")
            else:
                print("No hay platos registrados para eliminar")
        elif elim == 2:
            if cliente["postre"] != []:
                print("Postres:")
                for i, pedido in enumerate(cliente["postre"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero del postre a eliminar (Salir = 0): "))
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["postre"]):
                        cliente["postre"].pop(eliminar-1)
                        print("Postre eliminado correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de postre no es correcto")
            else:
                print("No hay postres registrados para eliminar")
        elif elim == 3:
            if cliente["bebida"] != []:
                print("Bebidas:")
                for i, pedido in enumerate(cliente["bebida"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero de la bebida a eliminar (Salir = 0): "))
                    print("Si no desea eliminar presione 0")
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["bebida"]):
                        cliente["bebida"].pop(eliminar-1)
                        print("Bebida eliminada correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de bebida no es correcto")
            else:
                print("No hay bebidas registradas para eliminar")
        elif elim == 0:
            break
        else:
            print("Opcion incorrecta")
            
# TODO ---------------------------------------- Lucero -------------------------------------------------------------

def mesas_pagadas(nmesa,pagoTotal):
    pagadas = {
        "N_Mesa": nmesa,
        "PagoTotal": pagoTotal
    }
    pagos_finales.append(pagadas)
        
def mostrar_pagos():
    if not pagos_finales:
        print("No hay registro de mesas pagadas")
    else:
        print("-"*80)
        print(tabulate(pagos_finales, headers="keys", tablefmt="grid"))
        print("-"*80) 
    
def pago_final():
    print("-" * 50)
    print("<< CALCULO >>".center(61))
    print("-" * 50)

    try:
        # Validación de número de mesa
        n_mesa = int(input("Digite el numero de mesa a pagar: "))
        if not (1 <= n_mesa <= 100):
            print("❌ Error: numero de mesa fuera del rango (1-100).")
            return

        # Verificación de existencia de la mesa
        existe_mesa = any(mesa["numero_mesa"] == n_mesa for mesa in Lista_mesas)
        if not existe_mesa:
            print("❌ Error: la mesa no está registrada.")
            return

        # Buscar cliente correspondiente y calcular consumo
        for cliente in lista_clientes:
            if cliente["N_Mesa"] == n_mesa:
                # Calcular consumo base
                # Inicializamos los pagos como 0
                pago_plato = 0
                pago_postre = 0
                pago_bebida = 0

                if "plato" in cliente and cliente["plato"]:  
                    for plato in cliente["plato"]:
                        pago_plato += int(plato[1]) 
               
                if "postre" in cliente and cliente["postre"]:  
                    for postre in cliente["postre"]:
                        pago_postre += int(postre[1])  
               
                if "bebida" in cliente and cliente["bebida"]: 
                    for bebida in cliente["bebida"]:
                        pago_bebida += int(bebida[1])  

                pago_total = pago_plato + pago_postre + pago_bebida

                # Calcular tiempo de espera
                pedido_min = cliente["hora_pedido"][0][0] * 60 + cliente["hora_pedido"][0][1]
                entrega_min = cliente["hora_entrega"][0][0] * 60 + cliente["hora_entrega"][0][1]

                # Aplicar descuento si corresponde
                if entrega_min > pedido_min + 30:
                    print("--" * 30)
                    print("‼ Tiempo de espera mayor a 30 minutos.")
                    print("---> Descuento automatico del 10% aplicado.")
                    print("--" * 30)
                    descuento = pago_total * 0.10
                    pago_total -= descuento

                # Preguntar por propina
                propina = input("¿Desea agregar propina del 10%? (si/no): ").lower()
                if propina == "si":
                    pago_total += pago_total * 0.10
                elif propina != "no":
                    print("⚠ Formato de respuesta incorrecto. Se omitio la propina.")

                # Guardar y mostrar resumen
                mesas_pagadas(n_mesa, round(pago_total, 2))
                print("=" * 60)
                print(f"{'Resumen de Pago':^60}")
                print("-" * 60)
                print(f"{'Mesa #:':<20} {n_mesa}")
                print(f"{'Total a pagar:':<20} {pago_total:.2f} soles")
                print("-" * 60)
                print(f"{'¡Gracias por su visita!':^60}")
                print("=" * 60)
                return

        # Si no se encontró cliente con esa mesa
        print("❌ Error: No se encontrO consumo registrado para esta mesa.")

    except ValueError:
        print("❌ Error: Debe ingresar un numero entero.")


# TODO ------------------------------------------- JOSEPH ------ -----------------------------------------------------


def mozo_mas_pedido():
    if not lista_clientes or not Lista_mozos:
        print("No hay mozos registrados o no hay pedidos registrados")
        return

    mozos_items = {}
    for mozo in Lista_mozos:
        mozos_items[mozo['nombre_mozo']] = 0
    
    for cliente in lista_clientes:
        mozo = cliente['N_Mozo']
        if mozo in mozos_items:
            mozos_items[mozo] += len(cliente['plato'])
            mozos_items[mozo] += len(cliente['postre'])
            mozos_items[mozo] += len(cliente['bebida'])
    
    if not mozos_items or sum(mozos_items.values()) == 0:
        print("No hay pedidos registrados")
        return

    mozo_top = ("", 0)
    for nombre, cantidad in mozos_items.items():
        if cantidad > mozo_top[1]:
            mozo_top = (nombre, cantidad)
    
    items_list = []
    for nombre, cantidad in mozos_items.items():
        items_list.append((cantidad, nombre))
    
    tabla_datos = []
    for posicion, (cantidad, nombre) in enumerate(items_list, start=1):
        tabla_datos.append([posicion, nombre, cantidad])
    
    print("\n" + "="*60)
    print("MOZO CON MAS PEDIDOS ATENDIDOS".center(60))
    print("="*60)
    print(tabulate(tabla_datos, headers=['Mozo', 'Total Pedidos'],tablefmt='grid'))
    print("="*60)
    print(f"¡El mozo mas eficiente es {mozo_top[0]} con {mozo_top[1]} pedidos atendidos!".center(60))
    print("="*60 + "\n")

def espera_promedio():
    if not lista_clientes:
        print("No hay pedidos registrados para calcular tiempos de espera")
        return
    
    total_pedidos = 0
    tiempo_total = 0 
    mostrar_prom = []
    
    for cliente in  lista_clientes:
        if not cliente['hora_pedido'] or not cliente['hora_entrega']:
            continue     
        hora_pedido, minuto_pedido = cliente['hora_pedido'][0]
        hora_entrega, minuto_entrega = cliente['hora_entrega'][0]
        
        tiempo_pedido = hora_pedido * 60 + minuto_pedido
        tiempo_entrega = hora_entrega * 60 + minuto_entrega

        tiempo_espera = tiempo_entrega - tiempo_pedido
            
        total_pedidos += 1
        tiempo_total += tiempo_espera
        
        mostrar_prom.append([
            cliente['N_Mesa'],
            f"{hora_pedido}:{minuto_pedido}",
            f"{hora_entrega}:{minuto_entrega}",
            f"{tiempo_espera}"])
        
    prom_espera = tiempo_total / total_pedidos

    if total_pedidos == 0:
        print("No hay pedidos completos con hora de entrega registrada")
        return
    
    print("\n" + "="*60)
    print("TIEMPO DE ESPERA POR PEDIDO".center(60))
    print("="*60)
    print(tabulate(mostrar_prom, 
                  headers=['Mesa', 'Hora Pedido', 'Hora Entrega', 'Tiempo Espera'],
                  tablefmt='grid'))
    print(f"Tiempo promedio de espera: {prom_espera:.1f} minutos")
    print("="*60 + "\n")


def pedidos_tardes():
    mostrar_tardes=[]
    pedidos_tardes = 0
    ped_puntiales = 0
    for cliente in  lista_clientes:
        if not cliente['hora_pedido'] or not cliente['hora_entrega']:
            return     
        hora_entrega, minuto_entrega = cliente['hora_entrega'][0]
        hora_maxima, minuto_maximo = cliente['hora_maxima'][0]
        
        tiempo_entrega = hora_entrega * 60 + minuto_entrega
        tiempo_maximo = hora_maxima * 60 + minuto_maximo
                
        tardio = "Sí" if tiempo_entrega > tiempo_maximo else "No"
        if tardio == "Sí":
            pedidos_tardes += 1
        else:
            ped_puntiales +=1
        mostrar_tardes.append([
            cliente['N_Mesa'],
            f"{hora_maxima}:{minuto_maximo}",
            f"{hora_entrega}:{minuto_entrega}",
            f"{tardio} min"])
    print(tabulate(mostrar_tardes, 
                  headers=['Mesa','Hora estimada', 'Hora Entrega', 'Tardio'],
                  tablefmt='grid'))

def mesa_mas_peds():
    imprimir=[]
    if not pagos_finales:
        print("No hay suficientes datos para generar este reporte")
        return
    mesa_mayor = 0
    consumo_mayor = 0
    
    for pago in pagos_finales:
        if pago["PagoTotal"] > consumo_mayor :
            consumo_mayor = pago["PagoTotal"]
            mesa_mayor = pago["N_Mesa"]
    imprimir.append([mesa_mayor,f"S/. {consumo_mayor}"])
    
    print("\n" + "="*60)
    print("MESA CON MAYOR CONSUMO (VENTAS TOTALES POR MESA)".center(60))
    print("="*60)
    print(tabulate(imprimir, headers=["Mesa", "Consumo Total"], tablefmt="grid"))
    print("\n" + "RESULTADO:".center(60))
    
    
def ingreso_x_zona():
    if not pagos_finales:
        print("No hay suficiente datos para generar el reporte")
        return
    ingresos_sala=0
    ingresos_terr=0
    mesas_sala=0
    mesas_terraza=0
    mesa_zona={}
    for mesa in Lista_mesas:
        mesa_zona[mesa["numero_mesa"]] = mesa["zona_mesa"]
    
    for pago in pagos_finales:
        mesa= pago["N_Mesa"]
        if mesa in mesa_zona:
            zona= mesa_zona[mesa]
            if zona == "sala":
                ingresos_sala+=pago["PagoTotal"]
                mesas_sala+=1
            elif zona == "terraza":
                mesas_terraza+=1
                ingresos_terr+=pago["PagoTotal"]
    total_ingreso=ingresos_terr+ingresos_sala
    total_mesas=mesas_sala+mesas_terraza
    
    porc_sala=(ingresos_sala/total_ingreso)*100
    porc_terraza=(ingresos_terr/total_ingreso)*100

    imprimir=[[f"Sala",f"S/.{ingresos_sala}",mesas_sala],[f"Terraza",f"S.{ingresos_terr}",mesas_terraza],["Total",f"S/.{total_ingreso}",total_mesas]]
    print("\n" + "═"*60)
    print(" INGRESOS POR ZONA (SALA VS. TERRAZA) ".center(60))
    print("═"*60)
    print(tabulate(imprimir,headers=["Zona", "Ingresos Totales", "Mesas Atendidas"],tablefmt="grid"))
    print("\n" + "ANÁLISIS DE DEMANDA:".center(50))
    print("="*60)
    print(f"- Sala: {porc_sala:.1f}% de los ingresos ({mesas_sala} mesas)")
    print(f"- Terraza: {porc_terraza:.1f}% de los ingresos ({mesas_terraza} mesas)")
    print("="*60)


def caratula():
    print("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@  ".center(80))
    print("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@  ".center(80))
    print("  @@   @@   @@    @@   @@   @@  ".center(80))
    print(" @@    @@   @@    @@   @@    @@ ".center(80))
    print("@@@   @@    @@    @@    @@   @@@".center(80))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@".center(80))
    print("@@   @@@    @@    @@    @@@   @@".center(80))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@".center(80))
    print(" @@@@@@@@@@@@@ @@  @@@@@@   @@@ ".center(80))
    print(" @@@@@@@@@@@@@@  @@@@@@@@@@  @@ ".center(80))
    print(" @@@@       @@@  @@@@@ @@@@  @@ ".center(80))
    print(" @@@@       @@@  @@@@@@@@@@  @@ ".center(80))
    print(" @@@@      @@@@    @@@@@@@   @@ ".center(80))
    print(" @@@@      @@@@@@@@@@@@@@@@@@@@ ".center(80))
    print(" @@@@       @@@@@@@@@@@@@@@@@@@ ".center(80))
    print(" @@@@       @@@              @@ ".center(80))
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ".center(80))
    print("================================".center(80))
    print("SISTEMA DE GESTIÓN DE PEDIDOS PARA RESTAURANTES".center(80))
    print("TRABAJO PARCIAL".center(80))
    print("================================".center(80))
    print("Curso: PROGRAMACION ORIENTADO A OBJETOS".center(80))
    print("Docente: Juan Alfonso Ramírez Espinoza".center(80))
    print("2025-1".center(80))
    print("--------------------------------".center(80))
    print("Integrantes:".center(80))
    print("Hidalgo Martel, Joseph Edward (U202421665)".center(80))
    print("Huamán Flores, Alexis Miguel (U20241G114)".center(80))
    print("Peña Roña, Antony Jomar (U202421102)".center(80))
    print("Villavicencio Davila, Ivette Lucero (U20241G010)".center(80))
    print("================================".center(80))
    print("================================".center(80))

def menu():
    print("--" * 30)
    print("<< MENU PRINCIPAL >>".center(60))
    print("--" * 30)
    print("[1] Registrar mesa y mozo    ") 
    print("[2] Solicitar mozo           ")
    print("[3] Tomar pedido             ")
    print("[4] Calcular pago            ")
    print("[5] Ver reportes             ")
    print("[6] Salir  ")
    print("--" * 30)
    print("<< ...SISTEMA RESTAURANTE -- BIENVENIDOS ...>>".center(60))
    print("--" * 30)
        
def main():
    caratula() 
    while True:
        menu()
        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if 1 <= opcion <= 7:
                    break
                else:
                    print("Opción invalida. Intente nuevamente.")
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero.")   
        if opcion == 1:
            while True:
                print("----------------------------------------")
                print("1. Registrar mesas")
                print("2. Registrar mozos")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if 1 <= subopcion <= 3:
                        if subopcion == 1:   
                            Registrar_mesas() # 1. Registrar mesas
                        elif subopcion == 2:
                            Registrar_mozos() # 2. Registrar mozos
                        elif subopcion == 3:
                            break
                        else:
                            print("Opcion invalida. Intente nuevamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
                
        elif opcion == 2:  # Asignar mozo a mesa
            while True:
                print("----------------------------------------")
                print("1. Asignar mozo a mesa")
                print("2. Cambiar mozo de la mesa actual")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if subopcion == 1:
                        Asignar_mozo()
                    elif subopcion == 2:
                        Cambiar_mozo()
                    elif subopcion == 3:
                        print("Saliendo del menú de mozos.")
                        break  # Salimos del bucle porque eligió salir
                    else:
                        print("Opción invalida. Intente nuevamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")

        elif opcion == 3: # Reaizar el pedido 
            while True:
                print("----------------------------------------")
                print("1. Añadir pedido y ver datos del pedido")
                print("2. Eliminar pedido")
                print("[0. Regresar]")
                try:
                    opcion = int(input ("Ingresar opcion: "))
                    if  opcion == 1:
                        registro_pedido()
                    elif opcion == 2:
                        eliminar_pedido()
                    elif opcion == 0:
                        break
                except ValueError:
                    print("Valor incorrecto")
                    
        elif opcion == 4:
              while True: 
                print("----------------------------------------")
                print("1. Pago final por mesa")
                print("2. Mostrar reporte de pago por mesa")
                print("3. Salir")
                try:
                    opcion=int(input("Digite la opcion: "))
                    if opcion== 1:
                        pago_final()
                    elif opcion==2:
                        mostrar_pagos()
                    elif opcion==3:
                        break
                except ValueError:
                    print("Error, digite un numero")
    
        elif opcion == 5: # Aqui se muestran los reportes de los mozos , mesas y los pedidos de los clientes
            while True:
                print("1. Mostrar mesas")
                print("2. Mostrar mozos")
                print("3. Mostrar pedidos clientes")
                print("4. Mostrar pagos realizados")
                print("5. Mostrar mozo con mas pedidos")
                print("6. Mostrar promedio tiempo espera")
                print("7. Pedidos tardios")
                print("8. Mostrar mesa mayor consumo")
                print("9. Mostrar ingresos por zona (sala/Terrasa)")
                print("0. salir")
                try:
                    subopcion = int(input("Seleccione una opcion ( 0 salir ): "))
                    if subopcion == 0:
                        break
                    
                    elif subopcion == 1:
                        Mostrar_mesas() # Mostrar mesas registradas
                    elif subopcion == 2:
                        Mostrar_mozos() # Mostrar mozos registrados
                    elif subopcion == 3:
                        mostrar_cliente() # Mostrar los pedidos de los clientes
                    elif subopcion == 4:
                        mostrar_pagos()
                        
                    elif subopcion == 5:
                        mozo_mas_pedido()
                    elif subopcion == 6:
                        espera_promedio()
                    elif subopcion == 7:
                        pedidos_tardes()
                    elif subopcion == 8:
                        mesa_mas_peds()
                    elif subopcion == 9:
                        ingreso_x_zona()
                    else:
                        print("La opcion es incorrecta")
                        
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
        
        elif opcion == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida. Por favor, intente nuevamente.")
main()