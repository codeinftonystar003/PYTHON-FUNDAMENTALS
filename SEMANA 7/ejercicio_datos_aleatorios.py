from random import randint , choice

class CRegistro:
    def __init__(self, tipo, material, estado, tiempo):
        self.__tipo = tipo
        self.__material = material 
        self.__estado = estado 
        self.__tiempo = tiempo
        
    
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def get_material(self):
        return self.__material 
    def set_material(self, material):
        self.__material = material 
    
    def get_estado(self):
        return self.__estado
    def set_estado(self, estado):
        self.__estado  = estado
    
    def get_tiempo(self):
        return self.__tiempo
    def set_tiempo(self, tiempo):
        self.__tiempo = tiempo
    def __str__(self):
        return f"{self.__tipo}, {self.__material}, {self.__estado}, {self.__tiempo} años"


class CLista:
    def __init__(self,elementos):
        self.__listaRegistros = []
        self.__elementos = elementos
        
    
    def generarDatos(self,elementos):
        var_tipo = ["silla", "mesa", "escritorio", "estante"]
        var_material  = ["madera", "fierro", "melamina", "vidrio"]
        var_estado = ["bueno", "regular","malo", "pesimo"]
        for i in range(elementos):
            tipo = choice(var_tipo)
            material = choice(var_material)
            tiempo = randint(1,15)
            estado = choice(var_estado)
            registro = CRegistro(tipo, material, estado, tiempo)
            self.__listaRegistros.append(registro)
        
    
    def consultarDatos(self):
        if not self.__listaRegistros:
            print("No hay registro de muebles")
        else:
            print("--"*40)
            print("Registro de muebles".center(40))
            print("--"*40)
            print(f"{"TIPO":<12}{"MATERIAL":>14}{"ESTADO":>12}{"TIEMPO":>12}")
            print("--"*40)
            for reg in self.__listaRegistros:
                print(f"{reg.get_tipo():<12} {reg.get_material():>12} {reg.get_estado():>12} {reg.get_tiempo():>10}")
    
    def muebleUsado(self):
        contador = 0
        for reg in self.__listaRegistros:
           if  reg.get_tiempo() > 5:
               contador +=1
        print("--"*40)
        print("Muebles con mas de 5 años de uso: ", contador)
        for reg in self.__listaRegistros:
            if  reg.get_tiempo() > 5:
                print(f"{reg.get_tipo():<12} {reg.get_material():>12} {reg.get_estado():>12} {reg.get_tiempo():>10}")
        print("--"*40)
                
    def promedioMesas(self):
        uso = 0
        contador = 0
        for reg in self.__listaRegistros:
            if reg.get_tipo() == "mesas" and reg.get_material() == "fierro" and reg.get_estado == "regular":
                uso += reg.get_tiempo()
                contador+=1
        
        if uso > 0:
            promedio_uso = uso / contador
            print("--"*40)
            print("El promedio de uso para las mesas de fierro con estado regular es: ",promedio_uso)
            print("--"*40)
        else:
            print("--"*40)
            print("No hay mesas con esas caracteristicas [mesas + fierro + regular]")
            print("--"*40)
    
    def frecuenciaMaterial(self):
        madera = fierro = melamina = vidrio = 0
        for reg in self.__listaRegistros:
            if reg.get_material() == "madera":
                madera +=1
            if reg.get_material() == "fierro":
                fierro +=1
            if reg.get_material() == "melamina":
                melamina+=1
            if reg.get_material() == "vidrio":
                vidrio += 1
        
        print("=="*40)
        print("MATERIALES: ")
        print("Madera   -->", madera)
        print("fierro   -->",fierro)
        print("Melamina -->",melamina)
        print("Vidrio   -->", vidrio)
        print("El material que tiene mas frecuencia es: ")
        if madera >= fierro and madera >= melamina and madera >= vidrio:
            print("madera")
        if fierro >= madera and fierro >= melamina and fierro >= vidrio:
            print("fierro")
        if melamina >= madera and melamina >= fierro and melamina >= vidrio:
            print("melamina")
        if vidrio >= madera and vidrio >= fierro and vidrio >= melamina:
            print("Vidrio")
    
    def mesaAntigua(self):
        tiempo = 0
        lista_mayor_tiempo = []
        print("--"*40)
        for reg in self.__listaRegistros:
            if reg.get_material() == "madera" and reg.get_estado() == "bueno":
                tiempo = reg.get_tiempo()
                lista_mayor_tiempo.append(tiempo)
                break
        else:
            print("No existe una mesa con esas caracteristicas [mesa + madera + bueno]")
        if lista_mayor_tiempo != []:
            mayor = max(lista_mayor_tiempo)
            print("El mayor tiempo para de una mesa de madera en buen estado es: ",mayor)
            print("--"*40) 
    
    def ordenarMaterial(self):
        for i in range(len(self.__listaRegistros)-1):
            for j in range(len(self.__listaRegistros)-i-1):
                reg_actual = self.__listaRegistros[j]
                reg_siguiente = self.__listaRegistros[j+1]
                if reg_actual.get_material() > reg_siguiente.get_material():
                    self.__listaRegistros[j] = reg_siguiente
                    self.__listaRegistros[j + 1] =  reg_actual
                    
        print("--"*40)
        print(f"{"TIPO":<12}{"MATERIAL":>14}{"ESTADO":>12}{"TIEMPO":>12}")
        print("--"*40)
        for reg in self.__listaRegistros:
            print(f"{reg.get_tipo():<12} {reg.get_material():>12} {reg.get_estado():>12} {reg.get_tiempo():>10}")

def menu():
    print("MENU DE OPCIONES")
    print("=="*6)
    print("1. Ingresar cantidad de registros")
    print("2. Generar datos")
    print("3. Mostrar datos")
    print("4. Muebles usados")
    print("5. Promedio de mesas")
    print("6. Frecuencia de materiales")
    print("7. Mesa antigua")
    print("8. Listado ordenado por material")
    print("9. salir")

def main():
    while True:
        menu()
        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if 1<= opcion <= 9:
                    break
                else:
                    print("Opcion invalida , intente de nuevo")
            except ValueError:
                print("Error en los datos de ingreso...")

        if opcion == 9:
            break
        
        if opcion == 1:
            while True:
                elementos = int(input("Ingrese la cantidad de registros a realizar: "))
                if 1<= elementos <= 50:
                    break
                else:
                    print("El dato esta fuera del rango permitido")
            print(f"Se han generado {elementos} en el sistema")
            lista = CLista(elementos)
        elif opcion == 2:
            while True:
                respuesta = input("Desea generar los datos (si/no)").lower()
                if respuesta in ["si", "no"]:
                    break
                else:
                    print("El dato ingresado no es correcto a los valores permitidos")
            
            if respuesta == "si":
                print("----------------------------")
                lista.generarDatos(elementos)
                print("DATOS GENERADOS CON EXITO")
                print("----------------------------")
            else:
                print("La generacion de datos ha sido cancelada")
            
        elif opcion == 3:
            lista.consultarDatos()   
        elif opcion == 4:
            lista.muebleUsado()
        elif opcion == 5:
            lista.promedioMesas()
        elif opcion == 6:
            lista.frecuenciaMaterial()
        elif opcion == 7:
            lista.mesaAntigua()
        elif opcion == 8:
            lista.ordenarMaterial()    
            
# correr el programa
main()