# 4. El promedio final de un curso se obtiene en base al promedio simple de tres practicas calificadas. Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos puntos la nota de la tercera practica calificada, si es que esta no es menor que 10. Desarrolle el programa que determine el promedio final de un alumno conociendo sus tres notas.

import os
os.system("cls")

n1 = int(input("Ingrese la primera nota: "))
n2 = int(input("Ingrese la segunda nota: "))
n3 = int(input("Ingrese la tercera nota: "))

# Calculamos el promedio simple antes de modificar la tercera nota
promedioSimple = (n1 + n2 + n3) / 3

# Si la tercera nota es 10 o mas, se le suma 2 puntos
if n3 >= 10:
    n3 = n3 + 2

# Calculamos el promedio final luego del posible aumento
promedioFinal = (n1 + n2 + n3) / 3

# Mostramos los resultados al final
print(f"Primera nota: {n1}")
print(f"Segunda nota: {n2}")
print(f"Tercera nota (posible aumento): {n3}")
print(f"Promedio simple: {promedioSimple:.2f}")
print(f"Promedio final: {promedioFinal:.2f}")
