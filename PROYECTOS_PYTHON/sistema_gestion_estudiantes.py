class Alumno:
    def __init__(self, codigo, nombre, edad, sexo, promedio, carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.promedio = promedio
        self.carrera = carrera

class GestionAlumnos:
    def __init__(self):
        self.lista_alumnos = []

    def guardar_datos(self, codigo, nombre, edad, sexo, promedio, carrera):
        self.lista_alumnos.append(Alumno(codigo, nombre, edad, sexo, promedio, carrera))
        print(f"\nAlumno {nombre} registrado exitosamente.\n")

    def mostrar_datos(self):
        if not self.lista_alumnos:
            print("\nNo hay alumnos registrados.\n")
            return
        for alumno in self.lista_alumnos:
            print("===== DATOS DE ALUMNO =====")
            print(f"Codigo  : {alumno.codigo}")
            print(f"Nombre  : {alumno.nombre}")
            print(f"Edad    : {alumno.edad} años")
            print(f"Sexo    : {alumno.sexo}")
            print(f"Promedio: {alumno.promedio}")
            print(f"Carrera : {alumno.carrera}")
            print("===========================\n")

    def registrar_alumno(self):
        while True:
            codigo = input("Ingrese el código del alumno (9 caracteres): ")
            if len(codigo) == 9:
                break
            print("El código debe tener 9 caracteres.")

        nombre = input("Ingrese el nombre del alumno: ").title()

        while True:
            try:
                edad = int(input("Ingrese la edad del alumno (entre 18 y 35): "))
                if 18 <= edad <= 35:
                    break
                print("La edad debe estar entre 18 y 35 años.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        sexo = input("Ingrese el sexo del alumno (M/F/O): ").upper()

        while True:
            try:
                promedio = float(input("Ingrese el promedio del alumno (entre 0 y 20): "))
                if 0 <= promedio <= 20:
                    break
                print("El promedio debe estar entre 0 y 20.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        carrera = input("Ingrese la carrera del alumno: ").title()

        self.guardar_datos(codigo, nombre, edad, sexo, promedio, carrera)

    def buscar_alumno(self):
        codigo = input("Ingrese el código del alumno a buscar: ")
        encontrado = False
        for alumno in self.lista_alumnos:
            if alumno.codigo == codigo:
                print("\n===== DATOS DE ALUMNO =====")
                print(f"Codigo  : {alumno.codigo}")
                print(f"Nombre  : {alumno.nombre}")
                print(f"Edad    : {alumno.edad} años")
                print(f"Sexo    : {alumno.sexo}")
                print(f"Promedio: {alumno.promedio}")
                print(f"Carrera : {alumno.carrera}")
                print("===========================\n")
                encontrado = True
                break
        if not encontrado:
            print(f"Alumno con código {codigo} no encontrado.")

    def modificar_datos_alumno(self):
        codigo = input("Ingrese el código del alumno a modificar: ")
        for alumno in self.lista_alumnos:
            if alumno.codigo == codigo:
                print("1. Nombre\n2. Edad\n3. Sexo\n4. Promedio\n5. Carrera")
                opcion = input("Seleccione qué desea modificar: ")

                if opcion == "1":
                    alumno.nombre = input("Ingrese el nuevo nombre: ").title()
                elif opcion == "2":
                    while True:
                        try:
                            edad = int(input("Ingrese la nueva edad: "))
                            if 18 <= edad <= 35:
                                alumno.edad = edad
                                break
                            print("La edad debe estar entre 18 y 35 años.")
                        except ValueError:
                            print("Dato incorrecto. Intente nuevamente.")
                elif opcion == "3":
                    alumno.sexo = input("Ingrese el nuevo sexo (M/F/O): ").upper()
                elif opcion == "4":
                    while True:
                        try:
                            promedio = float(input("Ingrese el nuevo promedio: "))
                            if 0 <= promedio <= 20:
                                alumno.promedio = promedio
                                break
                            print("El promedio debe estar entre 0 y 20.")
                        except ValueError:
                            print("Dato incorrecto. Intente nuevamente.")
                elif opcion == "5":
                    alumno.carrera = input("Ingrese la nueva carrera: ").title()
                else:
                    print("Opción inválida.")

                print("Datos modificados exitosamente.\n")
                return
        print(f"Alumno con código {codigo} no encontrado.")

    def eliminar_alumno(self):
        codigo = input("Ingrese el código del alumno a eliminar: ")
        for alumno in self.lista_alumnos:
            if alumno.codigo == codigo:
                self.lista_alumnos.remove(alumno)
                print(f"Alumno con código {codigo} eliminado exitosamente.\n")
                return
        print(f"Alumno con código {codigo} no encontrado.")

    def salir_programa(self):
        print("Gracias por utilizar el programa. Hasta luego!")
        exit()

def menu():
    print("====== MENU DE OPCIONES ======")
    print("1. Registrar Alumno")
    print("2. Buscar Alumno")
    print("3. Mostrar Alumnos Matriculados")
    print("4. Modificar datos del alumno")
    print("5. Eliminar Alumno")
    print("6. Salir del programa")

def main():
    gestion = GestionAlumnos()
    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                gestion.registrar_alumno()
            elif opcion == 2:
                gestion.buscar_alumno()
            elif opcion == 3:
                gestion.mostrar_datos()
            elif opcion == 4:
                gestion.modificar_datos_alumno()
            elif opcion == 5:
                gestion.eliminar_alumno()
            elif opcion == 6:
                gestion.salir_programa()
            else:
                print("Opción incorrecta. Intente nuevamente.")
        except ValueError:
            print("Ingrese solo números.")

# Ejecutar el programa
main()
