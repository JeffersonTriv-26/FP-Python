# 7. Desarrolle el programa que lea tres numeros enteros y determine el numero intermedio. No use operadores logicos en la solucion.
import os
os.system("cls")

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

# Comparaciones para encontrar el numero intermedio
if n1 > n2:
    if n1 < n3:
        intermedio = n1
    elif n2 > n3:
        intermedio = n2
    else:
        intermedio = n3
else:
    if n1 > n3:
        intermedio = n1
    elif n2 < n3:
        intermedio = n2
    else:
        intermedio = n3

# Mostrar resultado al final
print(f"El numero intermedio es: {intermedio}")
