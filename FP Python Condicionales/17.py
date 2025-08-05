# 17. Una tienda ha puesto en oferta la venta, por docenas, de cierto tipo de producto ofreciendo un descuento del 15% por la compra de no menos de 6 docenas y 10% en caso contrario. Adicionalmente, la empresa un obsequio de 2 lapiceros por cada 3 docenas por la compra de no menos de 30 docenas en caso contrario no efectúa ningún obsequio.

import os
os.system("cls")

docenas = int(input("Ingrese la cantidad de docenas: "))
precio_docena = float(input("Ingrese el precio por docena: "))

importe_compra = docenas * precio_docena  # Calculo del importe total

# Si compra 6 o más docenas, descuento del 15%, caso contrario 10%
if docenas >= 6:
    descuento = importe_compra * 0.15
else:
    descuento = importe_compra * 0.10

total_pagar = importe_compra - descuento  # Total a pagar luego del descuento

# Si compra 30 o más docenas, recibe 2 lapiceros por cada 3 docenas
if docenas >= 30:
    lapiceros = (docenas // 3) * 2
else:
    lapiceros = 0

print(f"Importe de la compra: S/. {importe_compra:.2f}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_pagar:.2f}")
print(f"Lapiceros de obsequio: {lapiceros}")
