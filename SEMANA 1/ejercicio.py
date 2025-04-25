# Inventario de productos
from tabulate import tabulate

lista_productos = []
def guardar_productos(id , nombre ,precio, cantidad):
    producto = {
        'id': id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    lista_productos.append(producto)
    return lista_productos
def mostrar_productos(lista_productos):
    if not lista_productos:
        print("No hay productos registrados.")
    else:
        for productos in lista_productos:
            print(tabulate(lista_productos, headers="keys", tablefmt="grid"))
def agregar_productos():
    id_producto = input("Ingrese el ID del producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    cantidad_producto = int(input("Ingrese la cantidad del producto: "))
    guardar_productos(id_producto, nombre_producto, precio_producto, cantidad_producto)
    print("Producto agregado exitosamente.")

def menu():
    print("MENU PRINCIPAL")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            agregar_productos()
        elif opcion == "2":
            mostrar_productos(lista_productos)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
if __name__ == "__main__":
    main()