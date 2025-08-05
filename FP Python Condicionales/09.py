# 9. Una tienda ofrece un porcentaje de descuento sobre el importe de la compra de los cuatro tipos de productos cuyos codigos, precios unitarios y descuentos se muestran en las siguientes tablas. Desarrolle el programa que determine el importe de la compra, el descuento y el total a pagar por la compra de cierta cantidad de unidades de un mismo tipo de producto.

codigo = int(input("Codigo del producto: "))
cantidad = int(input("Cantidad: "))

# Asignar precio segun codigo
if codigo == 101:
    precio = 17
elif codigo == 102:
    precio = 25
elif codigo == 103:
    precio = 16
elif codigo == 104:
    precio = 27

importe = cantidad * precio

# Calculo de descuento segun el codigo y cantidad
if codigo == 101 and cantidad <= 10:
    descuento = importe * 0.05
elif codigo == 102 and cantidad >= 11 and cantidad <= 20:
    descuento = importe * 0.08
elif codigo == 103 and cantidad >= 21 and cantidad <= 30:
    descuento = importe * 0.10
elif codigo == 104 and cantidad >= 31:
    descuento = importe * 0.13
else:
    descuento = 0

total = importe - descuento

# Resultados finales
print(f"Codigo: {codigo}")
print(f"Cantidad: {cantidad}")
print(f"Importe: S/. {importe:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total:.2f}")
