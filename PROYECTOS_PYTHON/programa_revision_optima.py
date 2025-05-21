class Alumno:
    def __init__(self, nombre, edad, sexo, promedio, carrera, codigo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.promedio = promedio
        self.carrera = carrera
        self.codigo = codigo
        self.lista_alumnos = []
    
    def guardar_datos(self,codigo, nombre, edad, sexo, promedio, carrera):
        self.lista_alumnos.append(Alumno(nombre, edad, sexo, promedio, carrera, codigo))

    def mostrar_datos(self):
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
            try:
                codigo = input("Ingrese el código del alumno (9 caracteres): ")
                if len(codigo) == 9:
                    break
                else:
                    print("El código debe tener 9 caracteres.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
                
                    
        while True:
            nombre = input("Ingrese el nombre del alumno: ").title()
            if len(nombre) > 0:
                break
            else: 
                print("El nombre no puede estar vacío.")
        
        while True:
            try:
                edad = int(input("Ingrese la edad del alumno (entre 18 y 35): "))
                if 18 <= edad <= 35:
                    break
                else:
                    print("La edad debe estar entre 18 y 35 años.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        
        sexo = input("Ingrese el sexo del alumno (M/F): ").upper()
        
        while True:
            try:
                promedio = float(input("Ingrese el promedio del alumno (entre 0 y 20): "))
                if 0 <= promedio <= 20:
                    break
                else:
                    print("El promedio debe estar entre 0 y 20.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        
        while True:
            carrera = input("Ingrese la carrera del alumno: ").title()
            if len(carrera) > 0:
                break
            else:
                print("La carrera no puede estar vacía.")
        
        self.guardar_datos(codigo, nombre, edad, sexo, promedio, carrera)
        print(f"Alumno: {self.nombre} registrado exitosamente.")
    
    def buscar_alumnos(self):
        codigo = input("Ingrese el código del alumno a buscar: ")
        for alumno in self.lista_alumnos:
            if alumno.codigo == codigo:
                print("\n--------------------------------------------------")
                print("===== DATOS DE ALUMNO =====")
                print(f"codigo  : {alumno.codigo}")
                print(f"Nombre  : {alumno.nombre}")
                print(f"Edad    : {alumno.edad} años")
                print(f"Sexo    : {alumno.sexo}")
                print(f"Promedio: {alumno.promedio}")
                print(f"Carrera : {alumno.carrera}")
                print("--------------------------------------------------\n")
                
            print(f"Alumno con codigo {self.codigo} no encontrado.")
    
    
    def Modificar_datos_alumno( self ):
        codigo = input("Ingrese el código del alumno a modificar: ")
        for alumno in self.lista_alumnos:
            if alumno.codigo == codigo:
                print("\n--------------------------------------------------")
                print("===== DATOS DE ALUMNO =====")
                print(f"codigo  : {alumno.codigo}")
                print(f"Nombre  : {alumno.nombre}")
                print(f"Edad    : {alumno.edad} años")
                print(f"Sexo    : {alumno.sexo}")
                print(f"Promedio: {alumno.promedio}")
                print(f"Carrera : {alumno.carrera}\n")
                print("----------------------------------------------------\n")
                print("Seleccciona el tipo de dato a modificar")
                print("1. Codigo\n2. Nombre\n3. Edad\n4. Sexo\n5. Promedio\n6. Carrera")
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    print("**** MODIFICAR CODIGO DE ALUMNO ***** ")
                    nuevo_codigo = input("Ingrese el nuevo código: ")
                    if len(nuevo_codigo) == 9 and self.codigo != nuevo_codigo:
                        alumno.codigo = nuevo_codigo
                    else:
                        print("El código debe tener 9 caracteres y no debe coincidir con el actual.")
                elif opcion == 2:
                    print("**** MODIFICAR NOMBRE DE ALUMNO ***** ")
                    nuevo_nombre = input("Ingrese el nuevo nombre: ").title()
                    if len(nuevo_nombre) > 0 and self.nombre!= nuevo_nombre:
                        alumno.nombre = nuevo_nombre
                    else:
                        print("El nombre no puede estar vacío y no debe coincidir con el actual.")
                elif opcion == 3:
                    print("**** MODIFICAR EDAD DE ALUMNO ***** ")
                    nueva_edad = int(input("Ingrese la nueva edad: "))
                    if 18 <= nueva_edad <= 35 and self.edad!= nueva_edad:
                        alumno.edad = nueva_edad
                    else:
                        print("La edad debe estar entre 18 y 35 años y no debe coincidir con el actual.")
                elif opcion == 4:
                    print("**** MODIFICAR SEXO DE ALUMNO ***** ")
                    nuevo_sexo = input("Ingrese el nuevo sexo (M/F): ").upper()
                    if nuevo_sexo in ["M", "F" , "O"] and self.sexo!= nuevo_sexo:
                        alumno.sexo = nuevo_sexo
                    else:
                        print("El sexo debe ser M/F/O y no debe coincidir con el actual.")
                elif opcion == 5:
                    print("**** MODIFICAR PROMEDIO DE ALUMNO ***** ")
                    nuevo_promedio = float(input("Ingrese el nuevo promedio: "))
                    if 0 <= nuevo_promedio <= 20 and self.promedio!= nuevo_promedio:
                        alumno.promedio = nuevo_promedio
                    else:
                        print("El promedio debe estar entre 0 y 20 y no debe coincidir con el actual.")
                elif opcion == 6:
                    print("**** MODIFICAR CARRERA DE ALUMNO ***** ")
                    nueva_carrera = input("Ingrese la nueva carrera: ").title()
                    if len(nueva_carrera) > 0 and self.carrera!= nueva_carrera:
                        alumno.carrera = nueva_carrera
                    else:
                        print("La carrera no puede estar vacía y no debe coincidir con el actual.")
                else:
                        print("Opcion invalida. Intente nuevamente.")
            else:
                print(f"Alumno con codigo {self.codigo} no encontrado")
                
        print("\n------- Datos modificados exitosamente.--------\n")
    
    def Eliminar_alumno(self):
        codigo = input("Ingrese el código del alumno a eliminar: ")
        for alumno in self.lista_alumnos:
            if alumno.codigo == codigo:
                self.lista_alumnos.remove(alumno)
                print(f"\nAlumno con codigo {alumno.codigo} eliminado exitosamente.\n")
        else:
            print(f"Alumno con codigo {self.codigo} no encontrado.")
        
    def salir_programa(self):
        print("Gracias por utilizar el programa. Hasta luego!")
        exit()
    
def menu():
    print("====== MENU DE OPCIONES ==========")
    print("1. Registrar Alumno")
    print("2. Buscar Alumno")
    print("3. Mostrar Alumnos Matriculados")
    print("4. Modificar datos del alumno")
    print("5. Eliminar Alumno")
    print("6. salir del programa")
    

def main():
    menu()
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 6:
        if opcion == 1:
            alumnos = Alumno("" ,"" ,"" ,"", "" ,"")
            alumnos.registrar_alumno()
        elif opcion == 2:
            alumnos.buscar_alumnos()
        elif opcion == 3:
            alumnos.mostrar_datos()
        elif opcion == 4:
            alumnos.Modificar_datos_alumno()
        elif opcion == 5:
            alumnos.Eliminar_alumno()
        elif opcion == 6:
            alumnos.salir_programa()
        else:
            print("Opcion incorrecta. Intente nuevamente.")
        menu()
        opcion = int(input("Ingrese una opcion: "))
# ejecutar el programa
main()



