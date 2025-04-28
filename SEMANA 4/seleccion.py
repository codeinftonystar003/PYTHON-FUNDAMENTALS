while True:
    try:
        n = int(input("Ingrese un numero :"))
        if 1<= n <= 11:
            break
        else:
            print("Error el dato debe ser positivo")
    except ValueError:
        print("Error en los datos de iingreso")
limite = 1
for i in range(1, n+1):
    print("   "*(n - i), end="")
    for j in range(1,i*2):
        print(j , end = "  ")
    print()

for i in range(n-1, 0, -1):
    print("   "*(n-i), end= "")
    for j in range(1, i*2):
        print(j, end = "  ")
    print()