class Producto :
    def __init__(self, id, nombre, categoria, marca, precio, cantidad, garantia):
        self.id = id
        self.nombre = nombre 
        self.categoria = categoria
        self.marca = marca 
        self.precio = precio 
        self.cantidad = cantidad
        self.garantia = garantia 

class Gestion_tecnologia:
    def __init__(self):
        self.lista_productos = []
        self.lista_productos_vendidos = []  
        
    def guardar_datos(self, id, nombre,categoria,marca,precio, cantidad, garantia):
        producto = Producto(id, nombre, categoria, marca, precio, cantidad, garantia)
        self.lista_productos.append(producto)
        
    def guardar_productos_vendidos(self,id, nombre, marca, precio, cantidad):
        producto = Producto(id, nombre, " ", marca, precio, cantidad,0)
        self.lista_productos_vendidos.append(producto)
        
    def mostrar_datos(self):
        if not self.lista_productos:
            print("No hay productos guardados.")
        print("====== DATOS DEL PRODUCTO ======")
        for producto in self.lista_productos:
            print("---"*50)
            print(f"{'ID':<4} {'NOMBRE':<20} {'CATEGORIA':<20} {'MARCA':<20} {'PRECIO':<10} {'CANTIDAD':<10} {'GARANTIA':<10}")
            print(f"{producto.id:<4} {producto.nombre:<20} {producto.categoria:<20} "
                    f"{producto.marca:<20} {producto.precio:>10.2f} {producto.cantidad:>10} {producto.garantia:>10}")
        print("---"*50)
    
    def vendidos (self):
        if not self.lista_productos:
            print("No hay productos vendidos")
        print("===== DATOS DEL PRODUCTO VENDIDO ======")
        for producto in self.lista_productos_vendidos:
            print("---"*50)
            print(f"{'ID':<4} {'NOMBRE':<20} {'CATEGORIA':<20} {'MARCA':<20} {'PRECIO':<10} {'CANTIDAD':<10}")
            print(f"{producto.id:<4} {producto.nombre:<20} {producto.categoria:<20} "
                 f"{producto.marca:<20} {producto.precio:>10.2f} {producto.cantidad:>10}")
        print("---"*50)
            
    def Registrar_Producto(self):
        while True:
            id = input("Ingrese el ID del producto: ")
            if len(id) == 4 and  id not in  [producto.id for producto in self.lista_productos]:
                break
            else:
                print("El ID debe tener 4 caracteres y no debe estar repetido.")
    
        nombre = input("Ingrese el nombre del producto: ").title()
        categoria = input("Ingrese la categoría del producto: ").title()
        marca = input("Ingrese la marca del producto: ").title()
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser mayor a 0.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        
        garantia = int(input("Ingrese la garantía del producto (en meses): "))
        
        self.guardar_datos(id, nombre, categoria, marca, precio, cantidad, garantia)
        print(f"\n------- Producto {nombre} guardado exitosamente.------------- \n")
        
    def Registrar_ventas(self):
        while True:
            id = input("ingrese el id del producto : ")
            if len(id) == 4:
                break
            else:
                print("el codigo debe ser de 4 digitos numericos")
                
        while True:
            try:
                cantidad = int(input("ingrese la cantidad de unidades del producto: "))
                if cantidad > 0:
                    break
                else:
                    print("la cantidad debe ser mayor a 0")
            except ValueError:
                print("datos incorrectos")

        for producto in self.lista_productos:
            if producto.id == id:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    print(f"\n Se han vendido {cantidad} unidades del producto {producto.nombre}.\n")
                    print("\n---------- Venta existosa----------------\n")
                    print("==============================================================")
                    print(F"\nVOLETA DE VENTA DEL PRODUCTO {producto.nombre}\n")
                    print(f"Nombre: {producto.nombre}")
                    print(f"Precio: ${producto.precio:.2f}")
                    print(f"Cantidad: {cantidad}")
                    print(f"Total a pagar : {producto.precio * cantidad:.2f} s/")
                    print("\n GRACIAS POR SU PREFERENCIA SOMOS ## TECNOLOGY ANTHONY ## \n")
                    print("==============================================================")
                
                    self.guardar_productos_vendidos(id, producto.nombre, producto.marca, producto.precio, cantidad)
                    break
    
                else:
                    print(f"\n------- No hay suficiente stock del producto {producto.nombre}.------------- \n")
                    break
            else:
                print(f"\n------- No se ha encontrado el producto con el ID {id}.------------- \n")
        
    def Consultar_stock(self):
        while True:
            id = input("Ingrese el ID del producto: ")
            if len(id) == 4:
                break
            else:
                print("El ID debe tener 4 caracteres.")

        # Buscar el producto por ID
        producto_encontrado = None
        for producto in self.lista_productos:
            if producto.id == id:
                producto_encontrado = producto
                break

        if producto_encontrado:
            # Obtener todas las marcas para el mismo producto (mismo nombre y categoría)
            # Codigo adicional para mostrar todas las marcas del producto
            """
            marcas = set()
            for producto in self.lista_productos:
                if producto.nombre == producto_encontrado.nombre and producto.categoria == producto_encontrado.categoria:
                    marcas.add(producto.marca)
            """
            print(f"\n------- Stock del producto {producto_encontrado.nombre} (ID {id}): {producto_encontrado.cantidad} unidades.------------- \n")
            print("      \nDatos generales del producto: ")
            print("===============================================")
            print(f"Nombre: {producto_encontrado.nombre}")
            print(f"Categoría: {producto_encontrado.categoria}")
            print(f"Marcas disponibles: {producto_encontrado.marca}")  # Mostrar todas las marcas
            print(f"Precio: ${producto_encontrado.precio:.2f}")
            print("===============================================")
        else:
            print(f"\n------- No se ha encontrado el producto con el ID {id}.------------- \n")
                
    def  Reporte_mas_vendidos(self):
        if not self.lista_productos_vendidos:
            print("No hay productos vendidos")
        else:
            productos_vendidos = sorted(self.lista_productos_vendidos, key=lambda x: x.cantidad, reverse=True)
            print("\n------- Reporte de productos más vendidos:------------- \n")
            for i, producto in enumerate(productos_vendidos[:10], start=1):
                print(f"{i}. Producto: {producto.nombre} (ID {producto.id}) - Cantidad vendida: {producto.cantidad} unidades")
                print("===============================================")
        
    def Alerta_stock_bajo(self):
        for producto in self.lista_productos:
            if producto.cantidad <= 5:
                print(f"\n------- Alerta! Stock bajo del producto {producto.nombre}"
                    f"(ID {producto.id}): QUEDAN : {producto.cantidad} unidades.------------- \n")
                break
            elif producto.cantidad >= 6:
                print(f"\n------- Producto {producto.nombre} (ID {producto.id}): Stock suficiente.------------- \n")
                break
            else:
                print(f"\n------- No se ha encontrado el producto con el ID {producto.id}.------------- \n")

    def verificar_garantia(self):
        grantia = 0
        while True:
            id = input("Ingrese el ID del producto: ")
            if len(id) == 4:
                break
            else:
                print("El ID debe tener 4 caracteres.")
        while True:
            try:
                grantia = int(input("Ingrese los meses transcurridos desde la fecha compra a la actual: "))
                if grantia > 0:
                    break
                else:
                    print("La garantía debe ser mayor a 0.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
                
        for producto in self.lista_productos:
            if producto.id == id:
                if producto.garantia > grantia:
                    print(f"\n------- Producto {producto.nombre} (ID {id}): Garantía vigente.------------- \n")
                else:
                    print(f"\n------- Producto {producto.nombre} (ID {id}): Garantía vencida.------------- \n")
                break
            print(f"\n------- No se ha encontrado el producto con el ID {id}.------------- \n")
    
    def Eliminar_Producto(self):
        while True:
            try:
                id = input("ingrese el ID del producto a eliminar:")
                if len(id) == 4:
                    break
                else:
                    print("El ID debe tener 4 caracteres.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        
        for producto in self.lista_productos:
            if producto.id == id:
                self.lista_productos.remove(producto)
                print(f"\n------- Producto {producto.nombre} (ID {id}) eliminado exitosamente.------------- \n")
                break
            else:
                print(f"\n------- No se ha encontrado el producto con el ID {id}.------------- \n")



def menu():
    print("\n------- Menu Principal:------------- \n")
    print("1. Registrar Producto")
    print("2. Registrar Venta")
    print("3. Consultar Stock")
    print("4. Reporte de Productos")
    print("5. Alerta Stock Bajo")
    print("6. Verificar Garantía")
    print("7. Eliminar Producto")
    print("8. Salir")
        
def main():
    gestion = Gestion_tecnologia()
    while True:
        menu()
        try:
            opcion = int(input("Ingrese su opción: "))
            if opcion == 1:
                gestion.Registrar_Producto()
            elif opcion == 2:
                gestion.Registrar_ventas()
            elif opcion == 3:
                gestion.Consultar_stock()
            elif opcion == 4:
                print("OPCION DE REPORTE\n")
                print("1. Reporte general")
                print("2. Productos vendidos")
                print("3. Reporte de productos más vendidos")
                suopcion = int(input("Ingrese su opción: "))
                if suopcion == 1:
                    gestion.mostrar_datos()
                elif suopcion == 2:
                    gestion.vendidos()
                elif suopcion == 3:
                    gestion.Reporte_mas_vendidos()
                else:
                    print("opcion no valida.")
                    
            elif opcion == 5:
                gestion.Alerta_stock_bajo()
            elif opcion == 6:
                gestion.verificar_garantia()
            elif opcion == 7: 
                gestion.Eliminar_Producto()
            elif opcion == 8:
                print("\n------- Gracias por utilizar nuestro sistema.------------- \n")
                break
            else:
                print("\n------- Opcion no válida. Intente nuevamente.------------- \n")
        except ValueError:
            print("datos incorrectos. Intente nuevamente.")
# ejecutar el programa
main()


