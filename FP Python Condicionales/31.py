# 31. Calcular el sueldo de un trabajador segun categoria y horas trabajadas.
# Se aplica descuento del 20% si supera S/. 2500, sino 15%.

import os
os.system("cls")

categoria = input("Categoria (A, B, C, D): ").upper()
horas = int(input("Horas trabajadas: "))

# Asignar tarifa segun categoria
if categoria == "A":
    tarifa = 21
elif categoria == "B":
    tarifa = 19
elif categoria == "C":
    tarifa = 17
elif categoria == "D":
    tarifa = 15
else:
    tarifa = 0  # Categoria no valida, tarifa 0 (no valida pero continuamos)

# Calcular sueldo bruto multiplicando horas por tarifa
sueldo_bruto = horas * tarifa

# Aplicar descuento segun sueldo bruto
if sueldo_bruto > 2500:
    descuento = sueldo_bruto * 0.20
else:
    descuento = sueldo_bruto * 0.15

# Calcular sueldo neto restando el descuento
sueldo_neto = sueldo_bruto - descuento

print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
