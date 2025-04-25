"""
Elabore un programa en Python que teniendo como dato una hora 
expresada en horas, minutos y segundos (h, m, s) nos calcule y 
muestre la nueva hora luego de un segundo. Por ejemplo, si h fuese 
11, m fuese 59 y s fuese 59 entonces la nueva hora sería 12:0:0
"""

horas = int(input("Ingrese la hora (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))
segundos = int(input("Ingrese los segundos (0-59): "))

total = horas * 3600 + minutos * 60 + segundos + 1
horas = ( total // 3600 ) % 24 
aux = total % 3600
minutos = aux // 60 
segundos = aux % 60
print(f"La nueva hora es: {horas}:{minutos}:{segundos}")