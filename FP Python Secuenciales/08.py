# 8. Desarrolle el programa que determine de un cilindro el área base = π r2, área lateral = 2 π r h, área total = 2 x área base x área lateral. Siendo r el radio y h la altura.
import os
import math
os.system("cls")

r = float(input("Digite el valor del radio (r): "))
h = float(input("Digite la altura (h): "))

baseArea = math.pi * (r ** 2)
lateralArea = 2 * math.pi * r * h
totalArea = (2 * baseArea) + lateralArea

print(f"Área de la base: {baseArea:.2f}")
print(f"Área lateral: {lateralArea:.2f}")
print(f"Área total del cilindro: {totalArea:.2f}")
