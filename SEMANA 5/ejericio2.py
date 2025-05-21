
texto = input("Ingrese una cadena de texto:")
texto = texto.replace(" ", "")
diccionario = {}
for i in texto:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1
        
for i in diccionario:
    print(f"{i * diccionario[i]}: {diccionario[i]}")