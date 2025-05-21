def menu_principal():
    print("MENU EMPRESARIAL")
    print("1. Registrar")
    print("2. Reportes")
    print("3. Salir")

def menu_registrar():
    print("REGISTRO EMPRESARIAL")
    print("1. Registrar empresa")
    print("2. Registrar rubro")
    print("3. Volver al menú principal")

def menu_reportes():
    print("REPORTES EMPRESARIAL")
    print("1. Reporte de empresas por distrito")
    print("2. Pequeñas empresas evaluadas en los últimos meses")
    print("3. Reporte de empresas ordenado ASC por distrito")

def fecha_valida():
    try:
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))

        if mes < 1 or mes > 12:
            return False

        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_max = 31
        elif mes in [4, 6, 9, 11]:
            dias_max = 30
        elif mes == 2:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                dias_max = 29
            else:
                dias_max = 28
        else:
            return False

        if dia < 1 or dia > dias_max:
            return False
        return True
    except ValueError:
        return False

class Empresa:
    def __init__(self):
        self.lista_ruc = []
        self.lista_distrito = []
        self.lista_tipo = []
        self.lista_evaluacion = []

    def registrar_empresa(self):
        while True:
            try:
                ruc = input("Ingrese el RUC de la empresa (11 dígitos): ")
                if len(ruc) == 11 and ruc.isdigit():
                    self.lista_ruc.append(ruc)
                    break
                else:
                    print("El RUC debe tener 11 dígitos numéricos.")
            except ValueError:
                print("Dato incorrecto. Intente nuevamente.")

        while True:
            print("DISTRITOS EMPRESA")
            print("1. San Isidro  (I)")
            print("2. San Borja   (S)")
            print("3. Jesús María (J)")
            print("4. Breña       (B)")
            print("5. Cercado de Lima (L)")
            distrito = input("Ingrese el distrito de la empresa: ").upper()
            if distrito in ['I', 'S', 'J', 'B', 'L']:
                self.lista_distrito.append(distrito)
                break
            else:
                print("Distrito inválido.")

        while True:
            print("TIPOS DE EMPRESA:")
            print("1. Empresa Pequeña (P)")
            print("2. Empresa Mediana (M)")
            print("3. Empresa Grande (G)")
            tipo = input("Ingrese el tipo de la empresa: ").upper()
            if tipo in ['P', 'M', 'G']:
                self.lista_tipo.append(tipo)
                break
            else:
                print("Tipo de empresa inválido.")

        while True:
            print("Ingrese la fecha de evaluación:")
            if fecha_valida():
                dia = int(input("Día: "))
                mes = int(input("Mes: "))
                anio = int(input("Año: "))
                self.lista_evaluacion.append(f"{dia}/{mes}/{anio}")
                break
            else:
                print("Fecha inválida. Intente nuevamente.")

        print("Empresa registrada correctamente.")

    def reporte_empresas_distrito(self):
        distritos = {'I': "San Isidro", 'S': "San Borja", 'J': "Jesús María", 'B': "Breña", 'L': "Cercado de Lima"}
        conteo = {key: 0 for key in distritos.keys()}

        for distrito in self.lista_distrito:
            if distrito in conteo:
                conteo[distrito] += 1

        print("-------------------------------------------")
        print("REPORTE DE EMPRESAS POR DISTRITO")
        print("-------------------------------------------")
        print(" | Distrito         | Cant. Empresas      |")
        print("-------------------------------------------")
        for key, nombre in distritos.items():
            print(f" | {nombre:<16} | {conteo[key]:<18} |")
        print("-------------------------------------------")

    def pequeñas_empresas(self):
        print("Pequeñas empresas evaluadas en los últimos meses (Noviembre y Diciembre):")
        for i in range(len(self.lista_tipo)):
            mes = int(self.lista_evaluacion[i].split('/')[1])
            if self.lista_tipo[i] == 'P' and mes in [11, 12]:
                print(f"RUC: {self.lista_ruc[i]}, Distrito: {self.lista_distrito[i]}, Fecha: {self.lista_evaluacion[i]}")

    def ordenar_empresas(self):
        for i in range(len(self.lista_distrito) - 1):
            for j in range(i + 1, len(self.lista_distrito)):
                if self.lista_distrito[i] > self.lista_distrito[j]:
                    # Intercambiar distrito
                    aux = self.lista_distrito[i]
                    self.lista_distrito[i] = self.lista_distrito[j]
                    self.lista_distrito[j] = aux
                    # Intercambiar RUC
                    aux = self.lista_ruc[i]
                    self.lista_ruc[i] = self.lista_ruc[j]
                    self.lista_ruc[j] = aux
                    # Intercambiar tipo
                    aux = self.lista_tipo[i]
                    self.lista_tipo[i] = self.lista_tipo[j]
                    self.lista_tipo[j] = aux
                    # Intercambiar evaluación
                    aux = self.lista_evaluacion[i]
                    self.lista_evaluacion[i] = self.lista_evaluacion[j]
                    self.lista_evaluacion[j] = aux

        print("-------------------------------------------")
        print("REPORTE ORDENADO POR DISTRITO")
        print("-------------------------------------------")
        print(" | RUC          | Distrito    | Tipo   | Fecha         |")
        print("-------------------------------------------")
        for i in range(len(self.lista_distrito)):
            print(f" | {self.lista_ruc[i]:<12} | {self.lista_distrito[i]:<12} | {self.lista_tipo[i]:<6} | {self.lista_evaluacion[i]:<12} |")
        print("-------------------------------------------")


class Rubro:
    def __init__(self):
        self.lista_rubros = []

    def registrar_rubro(self):
        while True:
            codigo = input("Ingrese el código del rubro (4 caracteres): ")
            if len(codigo) == 4:
                break
            else:
                print("El código debe tener 4 caracteres.")

        descripcion = input("Ingrese la descripción del rubro: ")

        while True:
            print("CATEGORÍAS DE RUBRO:")
            print("1. Productos (P)")
            print("2. Servicios (S)")
            print("3. Actividades (A)")
            print("4. Tecnología (T)")
            categoria = input("Ingrese la categoría del rubro: ").upper()
            if categoria in ['P', 'S', 'A', 'T']:
                break
            else:
                print("Categoría de rubro inválida.")

        self.lista_rubros.append((codigo, descripcion, categoria))
        print("Rubro registrado correctamente.")


def main():
    empresa = Empresa()
    rubro = Rubro()

    while True:
        menu_principal()
        opcion = input("Ingrese su opción: ")
        if opcion == '1':
            menu_registrar()
            subopcion = input("Ingrese su subopción: ")
            if subopcion == '1':
                empresa.registrar_empresa()
            elif subopcion == '2':
                rubro.registrar_rubro()
            elif subopcion == '3':
                continue
            else:
                print("Opción inválida.")

        elif opcion == '2':
            menu_reportes()
            subopcion = input("Ingrese su subopción: ")
            if subopcion == '1':
                empresa.reporte_empresas_distrito()
            elif subopcion == '2':
                empresa.pequeñas_empresas()
            elif subopcion == '3':
                empresa.ordenar_empresas()
            else:
                print("Opción inválida.")

        elif opcion == '3':
            print("Gracias por usar el sistema empresarial. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
