cadena = input("Ingrese una cadena de texto : ")
palabras = cadena.split()
recuento = dict()

print("Palabras: ", palabras)

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Recuento: ", recuento)