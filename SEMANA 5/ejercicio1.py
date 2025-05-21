"""Escriba un programa en Python que permita insertar de forma 
ordenada ascendentemente números positivos en una lista. 
No debe usar ninguna función de ordenamiento. El fin del 
ingreso de datos será cuando se 
ingrese el 0. 
Ingrese numero: 5 
Lista: 5 
Ingrese numero: 23 
Lista: 5 23 
Ingrese numero: 18 
Lista: 5 18 23 
Ingrese numero: 2 
Lista: 2 5 18 23 
Ingrese numero: 0"""

lista = []
lista_ordenada  = []
while True:
    while True:
        try:
            n = int(input("Ingrese un numero: "))
            if n >= 0:
                break
            else:
                print("El numero debe de ser positivo")
        except ValueError:
            print("Error en el ingreso de datos")
    if n == 0:
        break
    
    lista.append(n)
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    
print(lista)
