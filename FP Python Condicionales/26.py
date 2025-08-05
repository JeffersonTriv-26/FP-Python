# 26. Una empresa ha decidido adquirir varias piezas de la misma clase a una fabrica de refacciones.
# Si el monto total de la compra excede de $5000, la empresa pedira prestado al banco el 30%;
# en caso contrario, el prestamo sera del 20%. La diferencia la cubrira con su propio dinero.
# El banco cobra un 10% de interes sobre el prestamo.

import os
os.system("cls")


monto = int(input("Ingrese el monto total de la compra: "))

# Determinar porcentaje de prestamo segun el monto
if monto > 5000:
    prestamo = monto * 30 // 100
else:
    prestamo = monto * 20 // 100

# Calcular interes del 10% sobre el prestamo
interes = prestamo * 10 // 100

# Lo que la empresa pagara de su propio dinero
propio = monto - prestamo


print(f"Pago con prestamo (incluye interes): $ {prestamo + interes}")
print(f"Pago con dinero propio: $ {propio}")
