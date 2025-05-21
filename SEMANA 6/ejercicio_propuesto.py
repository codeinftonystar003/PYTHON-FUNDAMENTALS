"""Desarrollar una aplicación que pueda gestionar las personas
(registrar y reportar información sobre personas). Cada persona debe tener: 
•un nombre •una edad El sistema debe permitir generar dos reportes: uno con 
todas las personas y otra con personas filtrados por edad. Las personas están 
almacenados en una basePersonas (la basePersonas
tiene como atributo una lista de personas) Clase Persona (con los atributos 
descritos y el método verpersona [muestra los datos de una persona]
Clase basePersonas (listapersonas (lista que almacena objetos Persona) y los métodos: 
registrarPersona[agrega una persona a la basePersonas], visualizarPersonas 
[ver listado de personas]"""

class Personas:
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.__edad = edad 
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        set.__nombre = nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def basePersonas(self):
        lista_personas = []
        personas = [self.__nombre, self.__edad]
        lista_personas.append(personas)
        for persona in lista_personas:
            print(f"Nombre: {persona[0]} --> Edad: {persona[1]}")
            

persona1 = Personas("Luis", 26)
personna2 = Personas("Pedro",21)
persona1.basePersonas()


    
    

        