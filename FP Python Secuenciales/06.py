# 6. Desarrolle el programa que calcule el área total y el volumen de un cilindro. Considere las siguientes formulas: Área = 2πr(r+h) y Volumen = πr2h. Siendo r el radio y h la altura.
import os
import math

os.system("cls")

# Solicitar al usuario que ingrese el valor 
r = float(input("Digite el valor del radio (r) del cilindro: "))
h = float(input("Digite la altura (h) del cilindro: "))

areaCilindro = 2 * math.pi * r * (r + h)
volumenCilindro = math.pi * (r ** 2) * h

print(f"Área superficial total: {areaCilindro:.2f} unidades")
print(f"Volumen del cilindro: {volumenCilindro:.2f} unidades")

