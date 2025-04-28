# Jugadores 

seleccion_titular = {
    1 : "Pedro Gallese",
    22: "Alexander Callens",
    4 : "Anderson Santamaría ", 
    6 : "Marcos Lopez", 
    17: "Luis Advincula" ,
    10: "Christian Cueva ", 
    13: "Renato Tapia" ,
    23: "Pedro Aquino ",  
    9 : "Gianluca Lapadula", 
    20: "Edison Flores " ,
    18: "Andre Carrillo"    
    }

suplentes= {
    5 : "Carlos Zambrano",
    8 : "Sergio Peña",
    24: " Alex Valera",
    30: " Raúl Ruidíaz",
    16: "Christofer Gonzales",
    26: "Yordy Reyna",
    }

# Imprimir el diccionario de la seleccion titular
print("------------------- Seleccion titular------------------")
print(seleccion_titular)
# sustituir a Anderson Santamaria por Carlos Zambrano 
seleccion_titular [4] = suplentes[5]  # --> reemplzamos el contenido de la clave
del seleccion_titular[4] # --> borramos la clave anterior para que no se reemplace en la misma clave 
# Sustituir al resto de jugadores 
seleccion_titular[10] = suplentes[8]
seleccion_titular[23] = suplentes[24]  
seleccion_titular[9] = suplentes[30]  
seleccion_titular[20] = suplentes[16]  
seleccion_titular[18] = suplentes[26]  



print("-------------------Cambio de Suplentes-------------------")
print(seleccion_titular)

print("-"*30)
print("------Ordenado por numeros------")
ordenar_numero = sorted(seleccion_titular.items())
for clave, valor in ordenar_numero:
    print(f"{clave}: {valor}")

print("-"*30)
ordenar_nombres = sorted(seleccion_titular.items(), key = lambda x: x[1].strip())

print("------Ordenado por Nombres------")
for clave, valor  in ordenar_nombres:
    print(clave ,"-->", valor)

