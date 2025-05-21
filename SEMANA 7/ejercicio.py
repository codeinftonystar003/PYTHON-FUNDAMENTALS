class perro:
    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad
        

perro1 = perro("toby",20)
print("El nombre del canino es : ",perro1.get_nombre())
print("La edad del perro es : ", perro1.get_edad())  
perro1.set_edad(3)
print("El nombre del canino es : ",perro1.get_nombre())
print("La edad del perro es : ", perro1.get_edad())  