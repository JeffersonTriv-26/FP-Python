# 32. En una universidad, los alumnos están categorizados en cuatro categorías, según tabla 01.
# Semestralmente la universidad efectúa rebajas en las pensiones de sus estudiantes a partir del segundo ciclo
# sobre la base del promedio ponderado del ciclo anterior en porcentajes dados en la tabla 02.
# Desarrolle el programa que determine la pensión actual, el descuento y la nueva pensión del estudiante.

import os
os.system("cls")

# Se ingresa la categoría del estudiante y con .upper() convertimos a mayúscula,
# para que si escribe "a", "A", "b", "B", etc., siempre sea tratado como mayúscula.
categoria = input("Ingrese la categoría del estudiante (A, B, C, D): ").upper()

promedio = float(input("Ingrese promedio ponderado: "))

# Según la categoría asignamos la pensión
if categoria == "A":
    pension = 550
elif categoria == "B":
    pension = 500
elif categoria == "C":
    pension = 450
elif categoria == "D":
    pension = 400
else:
    pension = 0  # Si la categoría no es válida, se pone en 0

# Según el promedio, calculamos el descuento correspondiente
if promedio < 14:
    descuento = 0
elif 14 <= promedio <= 15.99:
    descuento = pension * 0.10
elif 16 <= promedio <= 17.99:
    descuento = pension * 0.12
else:
    descuento = pension * 0.15

# Calculamos la nueva pensión
nueva_pension = pension - descuento

print(f"Pensión original: S/. {pension:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Nueva pensión: S/. {nueva_pension:.2f}")
