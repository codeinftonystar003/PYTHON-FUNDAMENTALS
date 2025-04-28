import random
matriz = []
for f in range(10):
    lista = []
    for c in range(15):
        lista.append(random.randint(1,3))
    matriz.append(lista)
    
for f in range(10):
    for c in range(15):
        print(matriz[f][c], " ", end = "") 
    print()

frecuencia = []
for cultivo in range(1,4):
    contador = 0
    for f in range(10):
        for c in range(15):
            if matriz[f][c] == cultivo:
                contador += 1
    frecuencia.append(contador)

maximo = max(frecuencia)
minimos = min(frecuencia)
print(frecuencia)
print("El cultivo que mas se repite : ")
for i in range(3):
    if frecuencia[i] == maximo:
        print(i+1)
    
print("El cultivo que menos se repite")
for i in range(3): 
    if frecuencia[i] == minimos:
        print(i+1)
print("--"*10)
print("GUARIDA DE TOPO")
print("--"*10)

for f in range(1,9):
    for c in range(1,14):
        if matriz[f][c-1] == 2 and matriz[f][c+1]==2 and matriz[f-1][c]== 3 and matriz[f+1][c]==1:
            print("Fila : ", f , "Columna : ",c)