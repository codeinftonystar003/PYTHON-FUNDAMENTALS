from tabulate import tabulate
class Cliente:
    def __init__(self, dni, nombre,direccion,telefono,correo,indicacion):
        self.dni = dni
        self.nombre= nombre
        self.direccion = direccion 
        self.telefono = telefono 
        self.correo = correo 
        self.indicacion = indicacion
        self.lista_clientes = []
    def BaseClientes(self,dni,nombre,direccion,telefono,correo,indicacion):
        cliente = {
            "dni": dni,
            "Nombre":nombre,
            "Dirección":direccion,
            "Telefono": telefono,
            "Correo": correo,
            "Inidicacion": indicacion
        }
        self.lista_clientes.append(cliente)
    
    def ver_cliente(self):
        if not self.lista_clientes:
            print("No hay registros de clientes en la base de datos")

        else:
            print(tabulate(self.lista_clientes, headers = "keys", tablefmt = "grid"))
    
    def registrar_cliente(self):
        while True:
            try:
                dni = input("Ingrese su numero de DNI: ")
                if len(dni) == 8 and dni.isdigit():
                    break
                else:
                    print("El numero de dni es incorrecto...")
            except ValueError:
                print("Error en los datos de ingreso...")
                
        while True:
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese un Apellido: ")
            for n in nombre + apellido:
                if n.isdigit():
                    print("El nombre no debe tener numeros")
                    break
            else:
                break
        nombre = nombre + " " + apellido
        direccion = input("Ingrese su dirección: ")
        
        while True:
            try:
                telefono = input("Ingrese su numero de telefono : ")
                if len(telefono) == 9 and telefono.isdigit():
                    break
                else:
                    print("El numero de telefono es incorrecto")
            except ValueError:
                print("Error en los datos de ingreso...")
    
        indicacion = int(input("Ingrese su indicacion: 1-True 0- false "))
        if indicacion == 1:
            indicacion = True
        elif indicacion == 0:
            indicacion = False
        
        correo = f"{nombre[0].lower()}{apellido.lower()}@empesac.com"
        
        self.BaseClientes(dni,nombre,direccion,telefono,correo,indicacion)
        print("CLIENTE REGITRADO CON EXITO".center(50,"-"))
    
    def BuscarCliente(self):
        while True:
            dni_buscar = input("Ingrese el dni del cliente a buscar: ")
            if len(dni_buscar) == 8 and dni_buscar.isdigit():
                break
            else:
                print("El dni no es correcto")
        
        for cliente in self.lista_clientes:
            if cliente["dni"] == dni_buscar:
                print("Cliente_encontrado".center(50))
                print("-"*50)
                print(tabulate([cliente], headers="keys", tablefmt="grid"))
                break
        else:
            print("El cliente no fue encontrado....")

    def ActualizarCliente(self):
        while True:
            dni_cliente = input("Ingrese el dni del cliente a actualizar: ")
            if len(dni_cliente) == 8 and dni_cliente.isdigit():
                encontrado = False
                for cliente in self.lista_clientes:
                    if cliente["dni"] == dni_cliente:
                        encontrado = True
                        break
                
                if not encontrado:
                    print("El cliente no esta registrado")
                else:
                    break
            else:
                print("el dni del usuario ingresado no es correcto ....")
        
    
            
    
        print("MENU DE ACTUALIZACION")
        print("-"*24)
        print("1. Actualizar Nonbre")
        print("2. Actualizar DNI")
        print("3. Actualizar telefono")
        while True:
            try:
                opcion = int(input("Ingrese una opcion : "))
                if 1 <= opcion <= 3:
                    break
                else:
                    print("Opcion fuera de rango...")
            except ValueError:
                print("Ingrese un número válido")
        
        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            for cliente in self.lista_clientes:
                if cliente["dni"] == dni_cliente:
                    cliente["Nombre"] = nuevo_nombre
                
            print("NOMBRE DEL CLIENTE ACTUALZADO CON EXITO")
            print("-"*50)
        elif opcion == 2:
            while True:
                try:
                    nuevo_dni = input("Ingrese el nuevo numero de DNI: ")
                    if len(nuevo_dni) == 8 and nuevo_dni.isdigit():
                        break
                    else:
                        print("El dni es incorrecto") 
                except ValueError:
                    print("Error en los datos de ingreso")
            
            for cliente in self.lista_clientes:
                if cliente["dni"] == dni_cliente:
                    cliente["dni"] = nuevo_dni
            
            print("DNI DEL CLIENTE ACTUZALIZADO CON EXITO")
            print("-"*50)
        
        elif opcion ==3:
            while True:
                nuevo_telefono = input("Ingrese su nuevo numero de telefono: ")
                if len(nuevo_telefono) == 9 and nuevo_telefono.isdigit():
                    break
                else:
                    print("El numero de telefono es incorrecto")
                    
            for cliente in self.lista_clientes:
                if cliente["dni"] == dni_cliente:
                    cliente["Telefono"] = nuevo_telefono
        
    def eliminarCliente(self):
        while True:
            try:
                dni_cliente = input("ingrese el dni del cliente a eliminar : ")
                if len(dni_cliente) == 8 and dni_cliente.isdigit():
                    break
                else:
                    print("el DNI del cliente es incorrecto")
            except ValueError:
                print("Error en los datos de ingreso ")
        
        for cliente in self.lista_clientes:
            if cliente["dni"] == dni_cliente:
                self.lista_clientes.remove(cliente)
                break
        
        print("CLIENTE ELIMINADO CORRECTAMENETE")
        print("-"*50)                   
            
        
    def menu(self):
        print("(1) Añadir cliente") 
        print("(2) Buscar cliente") 
        print("(3) Actualizar cliente") 
        print("(4) Eliminar cliente") 
        print("(5) Listar todos los clientes") 
        print("(6) Terminar. ") 

def main():
    cliente = Cliente("", "", "", "", "", False)
    while True:
        cliente.menu()
        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if 1 <= opcion <= 6:
                    break
                else:
                    print("Opcion fuera de rango, intente nuevamente")
            except ValueError:
                print("Error en los datos de ingreso")
        
        if opcion == 1:
            cliente.registrar_cliente()
        elif opcion == 2:
            cliente.BuscarCliente()
        elif opcion == 3:
            cliente.ActualizarCliente()
        elif opcion == 4:
            cliente.eliminarCliente()
        elif opcion == 5:
            cliente.ver_cliente()
        elif opcion == 6:
            print("Saliendo del sistema ......... ")
            break

# correr el programa
main()