# 15. Una compania paga a sus vendedores un salario compuesto por un sueldo base de S/. 250 mas una comision, la cual depende del total de ventas realizadas. Ademas, si el sueldo bruto supera los S/. 3500, se aplica un descuento del 15%, en caso contrario, el descuento es del 8%. Elaborar el programa que calcule y muestre el sueldo bruto, la comision, el descuento y el sueldo neto.

import os
os.system("cls")

ventas = int(input("Ingrese el total de ventas: S/ "))

sueldo_base = 250

# Calculo de la comision segun el monto vendido
if ventas <= 5000:
    comision = ventas * 0.05
elif ventas <= 10000:
    comision = ventas * 0.08
elif ventas <= 20000:
    comision = ventas * 0.10
else:
    comision = ventas * 0.15

# Suma del sueldo base y la comision
sueldo_bruto = sueldo_base + comision

# Aplicar descuento segun el sueldo bruto
if sueldo_bruto > 3500:
    descuento = sueldo_bruto * 0.15
else:
    descuento = sueldo_bruto * 0.08

# Calculo del sueldo neto
sueldo_neto = sueldo_bruto - descuento

# Mostrar resultados finales
print(f"Sueldo Bruto: S/. {sueldo_bruto:.2f}")
print(f"Comision Ganada: S/. {comision:.2f}")
print(f"Descuento Aplicado: S/. {descuento:.2f}")
print(f"Sueldo Neto a Recibir: S/. {sueldo_neto:.2f}")
