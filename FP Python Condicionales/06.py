# 6. Desarrolle el programa que determine la edad menor y mayor de tres edades ingresadas.
import os
os.system("cls")

edad1 = int(input("Ingrese la primera edad: "))
edad2 = int(input("Ingrese la segunda edad: "))
edad3 = int(input("Ingrese la tercera edad: "))

# Determinar la edad mayor
mayor = edad1
if edad2 > mayor:
    mayor = edad2
if edad3 > mayor:
    mayor = edad3

# Determinar la edad menor
menor = edad1
if edad2 < menor:
    menor = edad2
if edad3 < menor:
    menor = edad3

# Mostrar los resultados al final
print(f"La edad menor es: {menor}")
print(f"La edad mayor es: {mayor}")
