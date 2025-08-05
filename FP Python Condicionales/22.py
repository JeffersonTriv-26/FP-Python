# 22. Una empresa desea adquirir cierta cantidad de unidades de dos productos A y B a un proveedor cuyos precios son los siguientes:
# Producto A = S/. 25 x unidad y 15 % de descuento para más de 50 unidades adquiridas.
# Producto B = S/. 30 x unidad y 10 % de descuento para más de 60 unidades adquiridas.
# Desarrolle el programa que muestre el importe bruto, descuento y total a pagar por la compra de ciertas unidades de ambos productos.

import os
os.system("cls")

# Preguntar la cantidad de productos A y B al usuario
productoA = int(input("Ingresa cantidad de prodcuto A : "))
productoB = int(input("Ingresa cantidad de prodcuto B : "))

# Precio fijo por unidad de cada producto
costoA = 25
costoB = 30

# Calculo del importe total por cada producto sin descuentos
importeA = productoA * costoA
importeB = productoB * costoB

# Sumo los importes de A y B para obtener el importe bruto total
t_importe = importeA + importeB

# Si compra más de 50 unidades del producto A, aplica 15% de descuento
descA = importeA * 0.15 if productoA > 50 else 0

# Si compra más de 60 unidades del producto B, aplica 10% de descuento
descB = importeB * 0.10 if productoB > 60 else 0

# Sumo ambos descuentos
t_descuento = descA + descB

# Calculo el total a pagar restando el descuento al importe bruto
t_pagar = t_importe - t_descuento

# Muestro todos los resultados
print("DETALLE DE COMPRA")
print(f"Importe de producto A : S/ {importeA}")
print(f"Importe de producto B : S/ {importeB}")
print(f"Importe total : S/ {t_importe}")
print(f"Descuento aplicado : S/ {t_descuento}")
print(f"Total a pagar : S/ {t_pagar}")
