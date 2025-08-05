import os
os.system("cls")

valorMetros = int(input("Ingrese la cantidad en Metros: "))

valorCentimetros = valorMetros * 100
valorPulgadas = valorCentimetros / 2.54
valorPies = valorPulgadas / 12
valorYardas = valorPies / 3

print(f"El equivalente en Centímetros es: {valorCentimetros:.2f} cm")
print(f"Equivalencia en Pulgadas: {valorPulgadas:.2f} in")
print(f"Conversión a Pies: {valorPies:.2f} ft")
print(f"Medida en Yardas: {valorYardas:.2f} yd")

