# 20. Dada una cantidad de dinero en soles, desarrolle el programa que descomponga dicha cantidad en billetes de 200, 100, 50, 20, 10 y monedas de 5, 2, 1 nuevos soles.
import os
os.system("cls")

cantidadSoles = int(input("Ingrese el monto total en soles (solo enteros): "))

# calculo cuántos billetes de 200 se pueden entregar
b200 = cantidadSoles // 200
cantidadSoles = cantidadSoles % 200  # lo que sobra sigue para abajo

# cuántos billetes de 100
b100 = cantidadSoles // 100
cantidadSoles = cantidadSoles % 100

# billetes de 50
b50 = cantidadSoles // 50
cantidadSoles = cantidadSoles % 50

# billetes de 20
b20 = cantidadSoles // 20
cantidadSoles = cantidadSoles % 20

# billetes de 10
b10 = cantidadSoles // 10
cantidadSoles = cantidadSoles % 10

# monedas de 5
m5 = cantidadSoles // 5
cantidadSoles = cantidadSoles % 5

# monedas de 2
m2 = cantidadSoles // 2
cantidadSoles = cantidadSoles % 2

# lo que queda son monedas de 1
m1 = cantidadSoles

print("\nDesglose en billetes y monedas:")
print(f"Billetes de 200: {b200}")
print(f"Billetes de 100: {b100}")
print(f"Billetes de 50: {b50}")
print(f"Billetes de 20: {b20}")
print(f"Billetes de 10: {b10}")
print(f"Monedas de 5: {m5}")
print(f"Monedas de 2: {m2}")
print(f"Monedas de 1: {m1}")
