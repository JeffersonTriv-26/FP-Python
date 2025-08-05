# 27. Una empresa paga a sus vendedores un sueldo que es la suma de un basico de S/. 600 mas una comision del 15% sobre las ventas.
# Si el sueldo bruto supera S/. 1800 se descuenta el 10%, en caso contrario el 5%. 
# Tambien se obsequian 3 polos si vende mas de S/. 1000, sino solo 1.

import os
os.system("cls")

# Ingresar el monto total de ventas
ventas = int(input("Ingrese el monto vendido: "))

# Calculo del sueldo bruto (basico + comision)
bruto = 600 + ventas * 15 // 100

# Determinar el descuento segun el sueldo bruto
if bruto > 1800:
    descuento = bruto * 10 // 100
else:
    descuento = bruto * 5 // 100

# Sueldo neto despues de aplicar el descuento
neto = bruto - descuento

# Calcular polos de regalo segun ventas
polos = 3 if ventas > 1000 else 1

# Mostrar resultados
print(f"Sueldo bruto: S/. {bruto}")
print(f"Descuento: S/. {descuento}")
print(f"Sueldo neto: S/. {neto}")
print(f"Polos de regalo: {polos}")
