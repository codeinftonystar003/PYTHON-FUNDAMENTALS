
def Ingresar_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero de 3, 4 o 5 cifras: "))
            if 100 <= numero <= 99999:
                break
            else:
                print("El número debe tener entre 3 y 5 cifras. Intente nuevamente.")
        except ValueError:
            print("Valor inválido. Intente nuevamente.")
    return numero

def EsCapicua(numero):
    num_str = str(numero)
    if num_str == num_str[::-1]:
        print(f"El número {numero} es capicúa.")
    else:
        inverso = int(num_str[::-1])
        suma = numero + inverso
        print(f"El número {numero} no es capicúa. La suma de {numero} + {inverso} es: {suma}.")

def main():
    numero = Ingresar_numero()
    EsCapicua(numero)

main()