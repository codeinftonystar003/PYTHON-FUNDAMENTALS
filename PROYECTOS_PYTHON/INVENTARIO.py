class Producto:
    def __init__(self,id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.id} , Precio: {self.precio}, Cantidad: {self.cantidad})"


class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("El producto ya existe , actualizar cantidad")
            self.productos[producto.id].cantidad += producto.cantidad
        else:   
            self.productos[producto.id] = producto
            print("Producto agregado al inventario")
            
    def eliminar_producto(self, id): 
        if id in self.productos: 
            del self.productos[id]
            print(f"producto con ID {id} eliminado.")
        else:
            print(f"No se encontro el producto con ID {id}")
            
    def actualizar_producto(self, id, cantidad , precio):
        if id in self.productos:
            self.productos[id].cantidad = cantidad
            self.productos[id].precio = precio
            print(f"Cantidad actualizada para el producto con ID {id}")
        else:
            print(f"No se encontro el producto con ID {id}")
            
    def listar_productos(self):
        for producto in self.productos.values():
            print(producto)
        
inventario1 = Inventario()
Producto1 = Producto(id=1, nombre="Laptop", precio=1200, cantidad=5)
Producto2 = Producto(id=2, nombre="Mouse", precio=20, cantidad=10)
Producto3 = Producto(id=3, nombre="Teclado", precio=50, cantidad=2)
print(inventario1.productos)
inventario1.agregar_producto(Producto1)
inventario1.agregar_producto(Producto2)
inventario1.agregar_producto(Producto3)
inventario1.actualizar_producto(1, 30, 4500)
inventario1.listar_productos()