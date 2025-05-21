#GESTION DE INVENTARIO DE UNA TIENDA

inventario = {
    "Manzanas":50,
    "Peras":30,
    "Plátanos":20,
    "Uvas":40,
    "Bananas":60,
    "Cerezas":10
}

#mostrar el inventario actual
def mostrar_inventario(inventario):
    print("Invenatario actual:")
    for producto , cntidad in inventario.items():
        print(f"{producto}: {cntidad} unidades")

def vender_producto(inventario):
    producto = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input(f"Ingrese la cantidad de {producto} desea vender: "))
    if producto in inventario:
        if inventario[producto] >=  cantidad:
            inventario[producto] -= cantidad
            print(f"Se han vendido {cantidad} unidades de {producto}")
        else:
            print(f"No hay suficientes unidades de {producto} en el inventario")
    else:
        print(f"{producto} no se encuentra en el inventario")
# agreagar nuevos productos 
def agregar_prtoductos(inventario):
    producto = input("Ingrese el nombre del producto a agregar: ")
    cantidad = int(input(f"Ingrese la cantidad de {producto} que desea agregar: "))
    if producto in inventario:
        inventario[producto] += cantidad
        print(f"Se han agregado {cantidad} unidades de {producto} al inventario")
    else:
        inventario[producto] = cantidad
        print(f"{producto} se ha agregado al inventario con {cantidad} unidades")

def buscar_producto(inventario):
    producto = input("Ingrese el nombre del producto a buscar: ")
    if producto in inventario:
        print(f"{producto} se encuentra en el inventario con {inventario[producto]} unidades")
    else:
        print(f"{producto} no se encuentra en el inventario")
        
#gestion de productos 

def gestion_tienda(inventario):
    while True:
        print("\nGestión del inventario")
        print("1. Mostrar inventario")
        print("2. Vender producto")
        print("3. Agregar productos")
        print("4. Buscar producto")
        print("5. Cerrar tienda")
        opcion = int(input("Elije una opción: "))
        if opcion == 1:
            mostrar_inventario(inventario)
        elif opcion == 2:
            vender_producto(inventario)
        elif opcion == 3:
            agregar_prtoductos(inventario)
        elif opcion == 4:
            buscar_producto(inventario)
        elif opcion == 5:
            print("cerrando tienda....by!!!")
            break
        else:
            print("Opción incorrecta, intente de nuevo")

gestion_tienda(inventario)