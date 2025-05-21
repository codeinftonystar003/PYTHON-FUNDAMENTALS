class CuentaBancaria:
    def __init__(self, nombre,saldo, tasainteres):
        self.__nombre = nombre
        self.__saldo = saldo
        self.__tasainteres = tasainteres
        
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
        
    def get_tasainteres(self):
        return self.__tasainteres 

    def set_tasainteres (self, tasainteres):
        self.__tasainteres = tasainteres
        
    
    def aplicainteres(self):
        self.__saldo = self.__saldo + (self.__saldo * self.__tasainteres)/100

cuenta = CuentaBancaria("Juan de Arona",1000,3)
cuenta.aplicainteres()
print("El saldo es: ", cuenta.get_saldo())
cuenta.set_tasainteres(2)
cuenta.aplicainteres()
print("El saldo es: ", cuenta.get_saldo())


