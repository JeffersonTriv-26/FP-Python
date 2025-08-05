# 10. Un curso se evalua sobre la base de 5 notas de las cuales se elimina las notas de mayor y menor puntaje. Desarrolle el programa que muestre las notas eliminadas y el promedio aprobatorio.

import os
os.system("cls")

n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))
n4 = float(input("Ingrese la nota 4: "))
n5 = float(input("Ingrese la nota 5: "))

# Lista con las notas
notas = [n1, n2, n3, n4, n5]

# Encontrar mayor y menor nota
mayor = max(notas)
menor = min(notas)

# Eliminar mayor y menor de la lista
notas.remove(mayor)
notas.remove(menor)

# Calcular promedio de las 3 notas restantes
promedio = (notas[0] + notas[1] + notas[2]) / 3

# Mostrar resultados
print(f"Nota eliminada (mayor): {mayor}")
print(f"Nota eliminada (menor): {menor}")
print(f"Promedio final: {promedio:.2f}")

if promedio >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
