# 12. Desarrolle el programa que permita calcular el resultado de la ecuación de segundo grado de la forma ax2 + bx +c. Usando la clase Math.
import os
import math

os.system("cls")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# calculo del discriminante (lo que está dentro de la raíz cuadrada)
d = b * b - 4 * a * c

# saco la raíz cuadrada del discriminante
r = math.sqrt(d)

# fórmula general: (-b + raíz) / (2a)
x1 = (-b + r) / (2 * a)

# fórmula general: (-b - raíz) / (2a)
x2 = (-b - r) / (2 * a)

print("La primera solución es:", x1)
print("La segunda solución es:", x2)
