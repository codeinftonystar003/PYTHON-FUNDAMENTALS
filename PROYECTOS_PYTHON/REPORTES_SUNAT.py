from random import randint, choice


def genera_y_muestra_arreglo():
    lista_persona = []
    lista_antiguedad = []
    lista_departamento = []
    lista_capital = []

    while True:
        try:
            num_personas = int(input("ingrese el numero de personas a consultar : "))
            if 1 <= num_personas <= 50:
                break
            else:
                print("número de personas fuera de rango")
        except ValueError:
            print("datos incorrectos..")

    for i in range(num_personas):
        lista_persona.append(choice(['N', 'J']))
        lista_antiguedad.append(randint(1, 99))
        lista_departamento.append(choice(['L', 'C', 'O']))
        lista_capital.append(randint(200, 1000))
    return lista_persona, lista_antiguedad, lista_departamento, lista_capital, num_personas


def muestra_datos(lista_persona, lista_antiguedad, lista_departamento, lista_capital, num_personas):
    print("DATOS GENERADOS".center(50, '-'))  # Encabezado centrado con guiones
    print(f"{'PERSONA':<10}{'ANTIGÜEDAD':<15}{'DEPARTAMENTO':<15}{'CAPITAL':<10}")  # Encabezados de columnas
    print("-" * 50)  # Separador

    for i in range(num_personas):
        print(f"{lista_persona[i]:<10}{lista_antiguedad[i]:<15}{lista_departamento[i]:<15}{lista_capital[i]:<10}")

def calcula_maximo_minimo ( lista_antiguedad):
    minima_antiguedad = min(lista_antiguedad)
    maxima_amtiguedad = max(lista_antiguedad)
    print("-"*50)
    print(f"la máxima antiguedad es de : {maxima_amtiguedad} años")
    print(f"la mínima antiguedad es de  : {minima_antiguedad} años")

def porcentaje_natural_juridica(lista_persona,num_personas):
    cont_natural = 0
    cont_juridico = 0
    for i in range(num_personas):
        if lista_persona[i] == 'N':
            cont_natural +=1
        else:
            cont_juridico+=1
    porcentaje_natural = (cont_natural/num_personas) * 100
    porcentaje_juridico = (cont_juridico/num_personas) * 100
    print()
    print("-"*50)
    print(f"El porcentaje de personas naturales es de : {porcentaje_natural} % ")
    print(f"El porcentaje de personas juridicas es de : {porcentaje_juridico} % ")

def promedio_x_departamento(lista_departamento, lista_capital, num_personas):
    capital_acumulado1 = capital_acumulado2 = capital_acumulado3 = 0
    lima = callao = provincia = 0

    for i in range(num_personas):
        if lista_departamento[i] == 'L':
            lima += 1
            capital_acumulado1 += lista_capital[i]
        elif lista_departamento[i] == 'C':
            callao += 1
            capital_acumulado2 += lista_capital[i]
        elif lista_departamento[i] == 'O':
            provincia += 1
            capital_acumulado3 += lista_capital[i]

    print()
    print("-" * 50)
    print("PROMEDIO DE CAPITAL POR DEPARTAMENTO".center(50))
    if lima > 0:
        promedio_lima = capital_acumulado1 / lima
        print(f"LIMA      : {promedio_lima:.2f} soles")
    if callao > 0:
        promedio_callao = capital_acumulado2 / callao
        print(f"CALLAO    : {promedio_callao:.2f} soles ")
    if provincia > 0:
        promedio_provincia = capital_acumulado3 / provincia
        print(f"PROVINCIA : {promedio_provincia:.2f} soles ")

def datos_ordenados(lista_persona, lista_antiguedad,lista_departamento,lista_capital,num_personas):
    for i in range (num_personas-1):
        for j in range( i+1, num_personas):
            if lista_antiguedad[i] > lista_antiguedad[j]:
                aux = lista_antiguedad[i]
                lista_antiguedad[i] = lista_antiguedad[j]
                lista_antiguedad[j] = aux
                aux = lista_persona[i]
                lista_persona[i] = lista_persona[j]
                lista_persona[j] = aux
                aux = lista_departamento[i]
                lista_departamento[i] = lista_departamento[j]
                lista_departamento[j] = aux
                aux = lista_capital[i]
                lista_capital[i] = lista_capital[j]
                lista_capital[j]=aux
    print()
    print("DATOS ORDENADOS POR CAPITAL".center(50, '-'))  # Encabezado centrado con guiones
    print(f"{'PERSONA':<10}{'ANTIGÜEDAD':<15}{'DEPARTAMENTO':<15}{'CAPITAL':<10}")  # Encabezados de columnas
    print("-" * 50)  # Separador

    for i in range(num_personas):
        print(f"{lista_persona[i]:<10}{lista_antiguedad[i]:<15}{lista_departamento[i]:<15}{lista_capital[i]:<10}")


def main():
    lista_persona, lista_antiguedad, lista_departamento, lista_capital, num_personas = genera_y_muestra_arreglo()
    muestra_datos(lista_persona, lista_antiguedad, lista_departamento, lista_capital, num_personas)
    calcula_maximo_minimo(lista_antiguedad)
    porcentaje_natural_juridica(lista_persona, num_personas)
    promedio_x_departamento(lista_departamento,lista_capital,num_personas)
    datos_ordenados(lista_persona,lista_antiguedad, lista_departamento, lista_capital ,num_personas)

# ejecutar el programa
main()