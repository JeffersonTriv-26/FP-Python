# 24. Una empresa paga a sus vendedores un sueldo igual al 10% del monto total vendido
# mas S/. 25 por cada S/. 500 de venta en exceso sobre S/. 5000.
# Desarrolle el programa que permita calcular el sueldo de un vendedor.

import os
os.system("cls")


monto_vendido = int(input("Ingresa el monto total vendido: "))

# Calculo el 10% del monto vendido
sueldo = monto_vendido * 10 / 100

# Si se supera los 5000, se añade 25 por cada 500 de exceso
if monto_vendido > 5000:
    exceso = (monto_vendido - 5000) // 500  # Cantidad de bloques de 500
    sueldo += exceso * 25  # Se suma 25 por cada bloque


print(f"Sueldo: S/ {sueldo:.2f}")
