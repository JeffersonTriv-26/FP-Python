# 29. Una empresa paga a sus empleados por horas trabajadas.
# Hasta 48 horas paga tarifa normal, las extras con 20% adicional.
# Si el sueldo bruto es mayor a 1500, aplica descuento de 11%.

import os
os.system("cls")

horas = int(input("Horas trabajadas: "))
tarifa = int(input("Pago por hora: "))

# Si trabaja hasta 48 horas, sueldo normal
if horas <= 48:
    sueldo_bruto = horas * tarifa
# Si trabaja más de 48 horas, calcular horas extra con recargo
else:
    sueldo_bruto = 48 * tarifa + (horas - 48) * tarifa * 1.2

# Si el sueldo supera 1500, se aplica descuento del 11%
if sueldo_bruto > 1500:
    descuento = sueldo_bruto * 0.11
else:
    descuento = 0

# Calcular el sueldo neto
sueldo_neto = sueldo_bruto - descuento


print(f"Horas trabajadas: {horas}")
print(f"Pago por hora: S/. {tarifa}")
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
