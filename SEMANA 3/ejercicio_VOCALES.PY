"""Hacer un programa en Python que permita el ingreso de 5 vocales, las vocales
pueden se mayúscula o minúsculas. Si la letra ingresada no es una vocal debe
dar un mensaje de error. Supongamos que la segunda vez no se ingresó una
vocal el mensaje debe decir: "El ingreso 2 no fue correcto", pero si se ingresó la
vocal "e" la segunda vez, el mensaje a mostrar debería ser: "El ingreso 2 fue la
letra e"""

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
print("Ingresar 5 Vocales")
print("-"*20)
for i in range(5):
    while True:
        vocal = input("Ingrese una vocal: ")
        if vocal.isalpha():
            break
        else:
            print("Error, ingrese una vocal.")

    if vocal in vocales:
        print(f"El ingreso {i+1} fue la letra {vocal}.")
    else:
        print(f"El ingreso {i+1} no fue correcto.")
