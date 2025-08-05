# 12. Desarrolle el programa que lea un número entero en el intervalo de 1 a 7 correspondiente a un día de la semana, y determine el nombre del día. Considere 1 - lunes, 2 – martes, …

import os
os.system("cls")

numero = int(input("Numero: "))

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

if numero >= 1 and numero <= 7:
    dia_nombre = dias[numero - 1]
else:
    dia_nombre = "Error"

print(f"El dia correspondiente es: {dia_nombre}")
