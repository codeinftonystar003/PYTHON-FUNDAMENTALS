class Ticket:
    def __init__(self, precio, hora):
        self.__precio = precio
        self.__hora = hora
        
    def get_hora(self):
        return self.__hora
    
    def get_hora(self,hora):
        self.__hora = hora
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio
        
    def __str__(self):
        return f"Ticket{self.__precio,self.__hora}"
    
    def NocheHora(self):
        hora = int(self.__hora[:2])
        if 18<= hora <= 23:
            return True
        else:
            return False
        
    def totalDescuento(self,n):
        if 5<= n <= 9:
            pago = self.__precio - (self.__precio * 0.10)
        elif n>= 0:
            pago = self.__precio -(self.__precio * 0.20)
        print(f"El pago total por {n} ticket es de {self.__precio*n - pago}")
ticket1 = Ticket(10,"18:45")
print(ticket1)
print(ticket1.NocheHora())
ticket1.totalDescuento(8)

        