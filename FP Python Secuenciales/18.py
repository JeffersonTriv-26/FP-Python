# 18. En una tienda han puesto en oferta la venta de todos sus artículos por cambio de estación ofreciendo un 15% + 15% de descuento. El primer 15% se aplica al importe de la compra, mientras que el segundo 15% se aplica al importe que resulta de restar el importe de la compra menos el primer descuento. Dada la cantidad de unidades adquiridas de un mismo tipo de artículo por parte de un cliente y el precio unitario del artículo. Desarrolle el programa que determine el importe de la compra, el descuento y el importe a pagar.
import os
os.system("cls")

cantidad = int(input("Digite cuántos artículos compró: "))
precio = int(input("Digite el precio unitario (sin decimales): "))

# calculo el importe total de la compra
importeTotal = cantidad * precio

# aplico el primer descuento del 15% sobre el importe total
descuento1 = importeTotal * 15 // 100

# resto el primer descuento para calcular sobre el saldo
saldoIntermedio = importeTotal - descuento1

# aplico el segundo descuento del 15% sobre el saldo intermedio
descuento2 = saldoIntermedio * 15 // 100

# sumo ambos descuentos
descuentoTotal = descuento1 + descuento2

# el importe final es el total menos los descuentos
importePagar = importeTotal - descuentoTotal

print(f"Importe de la compra: S/. {importeTotal}")
print(f"Descuento total aplicado: S/. {descuentoTotal}")
print(f"Total a pagar: S/. {importePagar}")
