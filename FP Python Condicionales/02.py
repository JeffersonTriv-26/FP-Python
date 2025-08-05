# 2. Una tienda vende un producto a un precio unitario igual a S/. 20. Como oferta la tienda ofrece un porcentaje de descuento sobre el importe de la compra. Adicionalmente la tienda regala caramelos en base al número de unidades adquiridas del producto. Desarrolle el programa que determine el importe de la compra, el descuento, total a pagar y el número de caramelos del obsequio que se da al cliente por la compra realizada. Ver tablas siguientes:
import os
os.system("cls")

precioProducto = 20
cantidadComprada = int(input("Ingrese la cantidad de unidades compradas: "))

importeTotal = precioProducto * cantidadComprada

# el descuento depende del importe total de la compra
descuentoCompra = importeTotal * (0.12 if importeTotal <= 500 else 0.16 if importeTotal > 700 else 0.14)

# la cantidad de caramelos depende de las unidades compradas
cantidadCaramelos = 5 if cantidadComprada <= 50 else 15 if cantidadComprada > 100 else 10

totalPagar = importeTotal - descuentoCompra

print(f"Importe total de la compra: S/. {importeTotal}")
print(f"Descuento aplicado: S/. {descuentoCompra}")
print(f"Total a pagar: S/. {totalPagar}")
print(f"Obsequio de caramelos: {cantidadCaramelos} unidades")
