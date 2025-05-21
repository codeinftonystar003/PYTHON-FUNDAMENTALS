# Clase Producto solo para definir productos
class Producto:
    def __init__(self, nombre, id, precio, cantidad):
        self.nombre = nombre
        self.id = id 
        self.precio = precio
        self.cantidad = cantidad

def menu():
    print("-------------------")
    print("MENU INVENTARIO")
    print("-------------------")
    print("1. Agregar producto")
    print("2. Mostrar datos")
    print("3. Vender producto")
    print("4. Agregar stock")
    print("5. Consultar stock")
    print("6. Modificar datos")
    print("7. Eliminar producto")
    print("8. Salir")
    print("-------------------")


# Clase Inventario para gestionar los productos
class Inventario:
    def __init__(self):
        self.lista_productos = []  # Inicializa la lista de productos

    def agregar_producto(self, nombre, id, precio, cantidad):
        self.lista_productos.append(Producto(nombre, id, precio, cantidad))

    def mostrar_datos(self):
        print("-------------------")
        print("DATOS DEL PRODUCTO")
        print("-------------------")
        for producto in self.lista_productos:
            print(f"Nombre   : {producto.nombre}")
            print(f"ID       : {producto.id}")
            print(f"Precio   : ${producto.precio}")
            print(f"Cantidad : {producto.cantidad}")
            print("-------------------")

    def vender(self, id, cantidad):
        for producto in self.lista_productos:
            if producto.id == id:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    print(f"Se han vendido {cantidad} unidades de {producto.nombre}")
                else:
                    print("No hay suficiente stock")
                return
        print("Producto no encontrado")
        
    def agregar_producto(self, nombre, id, precio, cantidad):
        for producto in self.lista_productos:
            if producto.id == id:
                print("Producto ya existe en el inventario")
                return
        self.lista_productos.append(Producto(nombre, id, precio, cantidad))
        print(f"Se ha agregado el producto {nombre} al inventario con ID {id}")
   
    def agregar_stock(self, id, cantidad):
        for producto in self.lista_productos:
            if producto.id == id:
                producto.cantidad += cantidad
                print(f"Se ha agregado {cantidad} unidades al stock de {producto.nombre}")
                return
        print("No se encuentra el producto con el ID ingresado")
        # agreagar producto falta

    def consultar_stock(self, id):
        for producto in self.lista_productos:
            if producto.id == id:
                print(f"El stock de {producto.nombre} (ID {id}) es {producto.cantidad}")
                return
        print("No se encuentra el producto con el ID ingresado")

    def modificar_producto(self, id):
        encontrado = False  # Bandera para verificar si se encontró el producto

        for producto in self.lista_productos:
            if producto.id == id:
                encontrado = True  # Producto encontrado
                print("----------------------------------")
                print("   MODIFICAR DATOS DEL PRODUCTO   ")
                print("----------------------------------")
                print(f"Nombre actual   : {producto.nombre}")
                print(f"ID actual       : {producto.id}")
                print(f"Precio actual   : ${producto.precio}")
                print(f"Cantidad actual : {producto.cantidad}")
                print("----------------------------------")
                print("Seleccione el dato a modificar:")
                print("1. Modificar nombre")
                print("2. Modificar ID")
                print("3. Modificar precio")
                print("4. Modificar cantidad")
                print("----------------------------------")

                try:
                    opcion = int(input("Ingrese la opción que desea modificar: "))
                    if opcion == 1:
                        nuevo_nombre = input("Nuevo nombre: ")
                        if producto.nombre != nuevo_nombre:
                            producto.nombre = nuevo_nombre
                        else:
                            print("El nombre ya existe en el inventario.")
                            nuevo_nombre = input("Nuevo nombre: ")
                            producto.nombre = nuevo_nombre
                            
                    elif opcion == 2:
                        nuevo_id = int(input("Nuevo ID: "))
                        if producto.id != nuevo_id:
                            producto.id = nuevo_id
                        else:
                            print("El ID ya existe en el inventario.")
                            nuevo_id = int(input("Nuevo ID: "))
                            producto.id = nuevo_id
                    elif opcion == 3:
                        nuevo_precio = float(input("Nuevo precio: "))
                        producto.precio = nuevo_precio
                    elif opcion == 4:
                        nueva_cantidad = int(input("Nueva cantidad: "))
                        producto.cantidad = nueva_cantidad
                    else:
                        print("Opción no válida.")
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número para las opciones y valores numéricos.")

                # Mostrar datos actualizados
                print("----------------------------------")
                print("DATOS MODIFICADOS:")
                print(f"Nombre   : {producto.nombre}")
                print(f"ID       : {producto.id}")
                print(f"Precio   : ${producto.precio}")
                print(f"Cantidad : {producto.cantidad}")
                print("----------------------------------")
                print("Datos modificados correctamente.")

        if not encontrado:
            print("No se encuentra el producto con el ID ingresado.")


    def eliminar_producto(self, id):
        for producto in self.lista_productos:
            if producto.id == id:
                self.lista_productos.remove(producto)
                print("Producto eliminado correctamente")
                return
        print("No se encuentra el producto con el ID ingresado")
        
        
def main():
    inventario = Inventario()
    menu()
    opcion = 0
    
    while opcion !=8 :
        while True:
            try:
                opcion = input("Ingrese una opción: ").strip()  # Eliminar espacios al principio y al final
                if opcion == "":
                    print("Espacio vacío no es una opción válida.")
                    continue
                opcion = int(opcion)  # Convertir la opción a entero
                if 1 <= opcion <= 8:
                    break
                else:
                    print("Opción inválida. Ingrese un número entre 1 y 8.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")
                
        if opcion == 1:
            print()
            print(" SECCION PARA AGREGAR PRODUCTOS")
            print("---------------------------------")
            nombre = input("Ingrese el nombre del producto: ")
            id = int(input("Ingrese el ID del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario.agregar_producto(nombre, id, precio, cantidad)
        elif opcion == 2:
            print()
            inventario.mostrar_datos()
            
        elif opcion == 3:
            id = int(input("Ingrese el ID del producto a vender: "))
            cantidad = int(input("Ingrese la cantidad a vender: "))
            inventario.vender(id, cantidad)
        elif opcion == 4:
            id = int(input("Ingrese el ID del producto a agregar stock: "))
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            inventario.agregar_stock(id, cantidad)
        elif opcion == 5:
            id = int(input("Ingrese el ID del producto a consultar stock: "))
            inventario.consultar_stock(id)
        elif opcion == 6:
            id = int(input("Ingrese el ID del producto a modificar: "))
            inventario.modificar_producto(id)
        elif opcion == 7:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == 8:
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta, intente nuevamente.")

# Ejecutar el programa
main()
    
 