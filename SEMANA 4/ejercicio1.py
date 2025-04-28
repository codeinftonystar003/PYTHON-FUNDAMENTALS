alumnos = {}
cantidad = int(input("Ingrese la cantidad de alumnos: "))
for n in range(cantidad):
    nombre = input("Ingrese el nombre del alumno: ")
    while nombre in alumnos:
        print("Alumno ya existe")
        nombre = input("Ingrese el nombre del alumno: ")
    
    notas = []
    nota = float(input("Ingrese la nota del alumno (negativo para finalizar): "))
    while 0<= nota <= 20:
        notas.append(nota)
        nota = float(input("Ingrese la nota del alumno (negativo para finaliar): "))
    alumnos[nombre] = notas.copy()

for nombre, notas in alumnos.items():
    print("%s ha obtenido de promedio de %d " %(nombre, sum(notas)/len(notas)))
    