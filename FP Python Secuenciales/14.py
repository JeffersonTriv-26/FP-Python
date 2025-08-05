# 14. Calcule el promedio de los 3 números mayores de 5 números ingresados. Usando la clase Math.
import os
import math
os.system("cls")

num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))
num3 = float(input("Digite el tercer número: "))
num4 = float(input("Digite el cuarto número: "))
num5 = float(input("Digite el quinto número: "))

listaNumeros = [num1, num2, num3, num4, num5]

# ordeno la lista de mayor a menor para tomar los 3 primeros
listaNumeros.sort(reverse=True)

# sumo los 3 números más grandes usando math.fsum
sumaTop3 = math.fsum([listaNumeros[0], listaNumeros[1], listaNumeros[2]])

# calculo el promedio de esos 3 números
promedioTop3 = sumaTop3 / 3

print(f"\nEl promedio de los tres números mayores es: {promedioTop3:.2f}")
