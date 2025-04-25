"""Hacer un programa en Python que permita el ingreso de 5 vocales, las vocales
pueden se mayúscula o minúsculas. Si la letra ingresada no es una vocal debe
dar un mensaje de error. Supongamos que la segunda vez no se ingresó una
vocal el mensaje debe decir: "El ingreso 2 no fue correcto", pero si se ingresó la
vocal "e" la segunda vez, el mensaje a mostrar debería ser: "El ingreso 2 fue la
letra e"""

lista_vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print("Usted debe ingresar 5 vocales")
print("-"*30)
for i in range(5):
    while True:
        try:
            vocales = input("Ingrese una vocal: ")
            if vocales.isalpha():
                break
            else:
                print("El ingreso no fue correcto")
                
        except ValueError:
            print("Error en los datos de ingreso")
        
    if vocales in lista_vocales:
        print(f"El ingreso {i+1} fue la letra {vocales}")
    else:
        print(f"El ingreso {i+1} no fue correcto")