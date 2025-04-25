""""
EScribir un programa en Python que reciba un angulo en radianes 
y lo convierta a grados sexagesimales. El angulo en grados debera 
ser mostrado en horas minutos y segundos. Por ejemplo si 
radianes = 3.141592  entonces la salida sera 180:0:0

"""
radianes = float(input("Ingrese angulo en radianes : "))
ansexag = radianes * 180 / 3.141592
grados = int(ansexag)   
aux1 = (ansexag - grados) * 60
minutos = int(aux1)
aux2 = (aux1 - minutos) * 60
segundos = int(aux2)
print(f"El angulo en grados sexagesimales es: {grados}:{minutos}:{segundos}")