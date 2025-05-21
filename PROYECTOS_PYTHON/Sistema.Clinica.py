from tabulate import tabulate
from datetime import datetime

class Paciente:
    def __init__(self, nombre, dni, fecha_nac, telefono):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nac = fecha_nac
        self.telefono = telefono
        
class Reporte_medico:
    def __init__(self):
        self.listado_citas = []
        self.lista_pacientes = []

    def guardar_pacientes(self, nombre, dni, fecha_nac, telefono):
        paciente = {'Nombre': nombre, 'DNI': dni, 'FECHA NACIMIENTO': fecha_nac, 'TELEFONO': telefono}
        self.lista_pacientes.append(paciente)

    def guardar_citas(self, dni, telefono, motivo, fecha_cita):
        cita = {'DNI': dni, 'TELEFONO': telefono, 'MOTIVO': motivo, 'FECHA CITA': fecha_cita}
        self.listado_citas.append(cita)

    def mostrar_pacientes(self):
        if not self.lista_pacientes:
            print("No hay pacientes registrados.")
        else:
            print("\n--- LISTADO DE PACIENTES ---")
            print(tabulate(self.lista_pacientes, headers="keys", tablefmt="grid"))

    def mostrar_citas(self):
        if not self.listado_citas:
            print("No hay citas registradas.")
        else:
            print("\n--- LISTADO DE CITAS ---")
            print(tabulate(self.listado_citas, headers="keys", tablefmt="grid"))

    def validar_fecha(self, fecha_str):
        try:
            datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
        
    def comparar_fecha_actual (self,fecha_str):
        try:
            fecha_ingresada = datetime.strptime(fecha_str, "%d/%m/%Y").date()
            fecha_actual = datetime.today().date()

            if fecha_ingresada < fecha_actual:
                print("Error: No se permiten fechas anteriores a hoy.")
                return False
            return True
        except ValueError:
            print("Error: Formato de fecha inválido. Use 'DD/MM/YYYY'.")
            return False
        
    def Registrar_paciente(self):
        nombre = input("Ingrese el nombre y apellidos del paciente: ").title()
        while True:
            try:
                dni = input("Ingrese el DNI del paciente: ")
                if len(dni) == 8 and dni.isdigit() and dni not in [paciente['DNI'] for paciente in self.lista_pacientes]:
                    break
                else:
                    print("El DNI debe ser un número de 8 dígitos y no debe estar repetido.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        while True:
            fecha_nac = input("Ingrese la fecha de nacimiento del paciente (dd/mm/aaaa): ")
            if self.validar_fecha(fecha_nac):
                break
            else:
                print("Fecha inválida. Ingrese una fecha válida en formato dd/mm/aaaa.")

        while True:
            try:
                telefono = input("Ingrese el teléfono del paciente: ")
                if len(telefono) == 9 and telefono.isdigit():
                    break
                else:
                    print("El teléfono debe tener 9 caracteres.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        self.guardar_pacientes(nombre, dni, fecha_nac, telefono)
        print("----------------------------------------")
        print("Paciente registrado correctamente.")

    def Registrar_Cita(self):
        while True:
            try:
                dni = input("Ingrese el DNI del paciente: ")
                if dni in [paciente['DNI'] for paciente in self.lista_pacientes]:
                    break
                else:
                    print("No se encuentra el paciente con ese DNI.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        motivo = input("Ingrese el motivo de la cita: ").title()

        while True:
            fecha_cita = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
            if self.validar_fecha(fecha_cita) and self.comparar_fecha_actual(fecha_cita):
                break
            else:
                print("La fecha de la cita debe ser posterior a hoy y la fecha ingresada.")

        while True:
            try:
                telefono = input("Ingrese el teléfono del paciente: ")
                if len(telefono) == 9 and telefono.isdigit():
                    break
                else:
                    print("El teléfono debe tener 9 caracteres.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        self.guardar_citas(dni, telefono, motivo, fecha_cita)
        print("----------------------------------------")
        print(" ### Cita registrada correctamente ###")
        print("----------------------------------------")

    def farmacia(self):
        medicamentos = [
            ("Paracetamol", 2.50),
            ("Ibuprofeno", 3.00),
            ("Naproxeno", 4.50),
            ("Ketorolaco", 5.00),
            ("Diclofenaco", 3.50),
            ("Amoxicilina", 12.00),
            ("Azitromicina", 15.00),
            ("Cefalexina", 10.50),
            ("Ciprofloxacino", 13.00),
            ("Metronidazol", 7.00),
            ("Loratadina", 6.50),
            ("Cetirizina", 8.00),
            ("Clorfenamina", 2.00),
            ("Desloratadina", 9.50),
            ("Ambroxol", 5.50),
            ("Losartán", 10.00),
            ("Enalapril", 8.50),
            ("Amlodipino", 7.50),
            ("Atenolol", 6.00),
            ("Furosemida", 4.00),
            ("Metformina", 9.00),
            ("Insulina", 45.00),
            ("Glibenclamida", 5.00),
            ("Omeprazol", 3.50),
            ("Ranitidina", 4.50),
            ("Bismuto", 6.50),
            ("Salbutamol", 15.00),
            ("Diazepam", 10.00),
            ("Dexametasona", 7.00),
            ("Aspirina", 2.50)
        ]
        headers = ["Medicamento", "Precio (S/.)"]
        print(tabulate(medicamentos, headers=headers, tablefmt="grid"))
        
        cliente = input("Ingrese el nombre del cliente: ").capitalize()
        dni_cliente = input("Ingrese el DNI del cliente: ")
        total_a_pagar = 0
        lista_compras = []
        
        while True:
            nombre = input("Ingrese el nombre del medicamento: ").capitalize()
            encontrado = False
            for med, precio in medicamentos:
                if med == nombre:
                    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
                    subtotal = precio * cantidad
                    total_a_pagar += subtotal
                    lista_compras.append((nombre, cantidad, precio, subtotal))
                    print(f"Subtotal por {cantidad} {nombre}: S/. {subtotal:.2f}")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Medicamento no encontrado.")
            
            opcion = input("¿Desea seguir comprando? (s/n): ").strip().lower()
            if opcion != "s":
                break
        
        print("------------------------------------------------")
        print("### BOLETA DE VENTA - FARMACIA VIDA Y SALUD ###")
        print("------------------------------------------------")
        print(f"Nombre Cliente: {cliente}")
        print(f"DNI Cliente: {dni_cliente}")
        print("------------------------------------------------")
        print(tabulate(lista_compras, headers=["Medicamento", "Cantidad", "Precio Unitario", "Subtotal"], tablefmt="grid"))
        print(f"TOTAL A PAGAR: S/. {total_a_pagar:.2f}")
        print("------------------------------------------------")

    def Calcular_Costo_cita(self):
        while True:
            try:
                dni = input("Ingrese el DNI del paciente: ")
                if dni in [paciente['DNI'] for paciente in self.lista_pacientes]:
                    break
                else:
                    print("No se encuentra el paciente con ese DNI.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        while True:
            try:
                costo = float(input("Ingrese el costo de la consulta: "))
                if costo > 0:
                    break
                else:
                    print("El costo debe ser mayor a 0.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        while True:
            try:
                descuento = float(input("Ingrese el descuento aplicado (entre 0 y 100): "))
                if 0 <= descuento <= 100:
                    break
                else:
                    print("El descuento debe estar entre 0 y 100.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
        while True:
            try:
                fecha_cita = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
                    
                if self.validar_fecha(fecha_cita) and fecha_cita in [cita['FECHA CITA'] for cita in self.listado_citas]:
                    break
                else:
                    print("No se encuentra la cita con esa fecha.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")
                
        gasto_medicamentales = float(input("Ingrese el gasto de medicamentos: "))
        if gasto_medicamentales > 0:
            costo_total = costo - (costo * descuento / 100) + gasto_medicamentales
            print(f"El costo total de la consulta con descuento aplicado es: ${costo_total:.2f}")
        else:
            print("El gasto de medicamentos debe ser mayor a 0.")
        print("\n-------------------------------------------")
        print("--- REGISTRO DE CITA ---")
        print(f"DNI Paciente: {dni}")
        print("---------------------------------------------")
        print(f"Costo de la consulta: ${costo:.2f}")
        print(f"Descuento aplicado: {descuento}%")
        print(f"Gasto de medicamentos: ${gasto_medicamentales:.2f}")
        print(f"Costo  Total : ${costo_total:.2f}")
        print("---CITA CANCELADA ---")
        print("---------------------------------------------")
         
    def Consultar_Historial_Medico(self):
        while True:
            try:
                dni = input("Ingrese el DNI del paciente: ")
                if dni in [paciente['DNI'] for paciente in self.lista_pacientes]:
                    break
                else:
                    print("No se encuentra el paciente con ese DNI.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        citas_paciente = [cita for cita in self.listado_citas if cita['DNI'] == dni]

        if not citas_paciente:
            print("\nNo hay citas registradas para este paciente.")
        else:
            print("\n--- HISTORIAL MÉDICO ---")
            print(tabulate(citas_paciente, headers="keys", tablefmt="grid"))
        
    def Reportes_Medicos(self):
        print("\n--- REPORTE GENERAL DE CITAS ---")
        print("---> opciones: ")
        print("1. Por paciente")
        print("2. Reporte General")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            while True:
                dias = int(input("Ingrese el número de días a validar la cita: "))
                if dias > 0:
                    break
                else:
                    print("El número de días debe ser mayor a 0.")
            if 1 < dias <= 30:
                self.Consultar_Historial_Medico()
            else:
                print("Usted no tiene citas registradas en los últimos", dias, "días.")
        elif opcion == 2:
            self.mostrar_citas()

    def Eliminar_paciente(self):
        while True:
            try:
                dni = input("Ingrese el DNI del paciente a eliminar: ")
                for paciente in self.lista_pacientes:
                    if paciente['DNI'] == dni:
                        self.lista_pacientes.remove(paciente)
                        print(f"Paciente con DNI {dni} eliminado exitosamente.")
                        return
                print("No se encuentra el paciente con ese DNI.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

    def salir(self):
        print(" \n###---GRACIAS POR UTILIZAR NUESTRO SISTEMA---###\n")
        exit()

def Menu_Principal():
    print("\n===== MENU PRINCIPAL======")
    print("---------------------------")
    print(" BIENVENIDOS A VIDA_CLINIC ")
    print("---------------------------")
    print("1. Registrar Paciente")
    print("2. Registrar Cita Medica")
    print("3. Consultar Historial Medico")
    print("4. Generar Reporte Medico")
    print("5. Reporte de Pacientes")
    print("6. Reporte de citas")
    print("7. Eliminar Pacientes")
    print("8. Farmacia Vida y Salud")
    print("9. Calcular Costo Cita")
    print("10. Salir")

def main():
    medico = Reporte_medico()
    while True:
        Menu_Principal()
        while True:
            opcion = input("Ingrese una opción: ").strip()  # Elimina espacios antes y después
            if not opcion:  # Verifica si la entrada está vacía
                print("La opción no puede estar vacía. Intente nuevamente.")
                continue
            if opcion.isdigit():  # Verifica si es un número
                opcion = int(opcion)
                break  # Sale del bucle si es válido
            else:
                print("Debe ingresar un número válido. Intente nuevamente.")
        if opcion == 1:
            medico.Registrar_paciente()
        elif opcion == 2:
            medico.Registrar_Cita()
        elif opcion == 3:
            medico.Consultar_Historial_Medico()
        elif opcion == 4:
            medico.Reportes_Medicos()
        elif opcion == 5:
            medico.mostrar_pacientes()
        elif opcion == 6:
            medico.mostrar_citas()
        elif opcion == 7:
            medico.Eliminar_paciente()
        elif opcion == 8:
            medico.farmacia()
        elif opcion == 9:
            medico.Calcular_Costo_cita()
        elif opcion == 10:
            medico.salir()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
    
# cosas a mejorar 
# 2 agregar algunos datos al paciente como dirección, email, etc.
# 6 agregar un minibot para detectar enfermedades 
# 7 agregar un sistema de seguridad para guardar los datos en un archivo
# 8 agregar una base de datos en archivo excel para manejar registros ya exustentes en el programa



# agregar cita pagada a historial medico
# seguimos con la validacion de fecha que no sea menor a la actual
# agregar opcion a registrar cita sobre medicos y horarios disponibles