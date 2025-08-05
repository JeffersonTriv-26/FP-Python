# 14. Un supermercado ofrece una promocion donde el cliente raspa una tarjeta con un numero oculto. Si el numero es par y no menor que 100, recibe un descuento del 15%. En cualquier otro caso, el descuento sera del 5%. Elaborar el programa que muestre el numero de la tarjeta, el importe de la compra y el descuento aplicado.

import os
os.system("cls")

monto_compra = int(input("Ingrese el importe de la compra: "))
numero_tarjeta = int(input("Ingrese el numero de la tarjeta: "))

if numero_tarjeta % 2 == 0 and numero_tarjeta >= 100:
    descuento = monto_compra * 0.15
else:
    descuento = monto_compra * 0.05

total_pagar = monto_compra - descuento

print("\nRESUMEN DE LA COMPRA")
print(f"Numero de tarjeta: {numero_tarjeta}")
print(f"Importe inicial: S/. {monto_compra:.2f}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Total a cancelar: S/. {total_pagar:.2f}")
