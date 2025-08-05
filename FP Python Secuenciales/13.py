# 13. Desarrolle el programa que permita calcular la hipotenusa de un triángulo. Usando la clase Math.
import os
import math
os.system("cls")

ladoA = float(input("Digite el primer cateto: "))
ladoB = float(input("Digite el segundo cateto: "))

# aplicando pitágoras: hipotenusa = raíz de (ladoA2 + ladoB2)
hipo = math.sqrt(ladoA**2 + ladoB**2)

print(f"El valor de la hipotenusa es: {hipo:.2f}")
