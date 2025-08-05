import os
os.system("cls")

a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))

# Verifico si los números están de menor a mayor
if a < b and b < c:
    orden = "ascendente"

# Verifico si están de mayor a menor
elif a > b and b > c:
    orden = "descendente"

# Si no es ninguno de los anteriores, está desordenado
else:
    orden = "desorden"

print(f"Numeros ingresados: {a}, {b}, {c}")
print(f"Orden: {orden}")
