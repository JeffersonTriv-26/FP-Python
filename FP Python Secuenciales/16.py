# 16. El cálculo del pago mensual de un empleado de una empresa se efectúa de la siguiente manera: el sueldo básico se calcula sobre la base del número total de horas trabajadas basado en una tarifa horaria, al sueldo básico, se le aplica una bonificación del 20% obteniéndose el sueldo bruto; al sueldo bruto, se le aplica un descuento del 10% obteniéndose el sueldo neto. Desarrolle el programa que muestre el sueldo básico, bruto y neto de un trabajador.
import os
os.system("cls")

horasTrabajadas = float(input("Digite cuántas horas trabajó: "))
pagoPorHora = float(input("Digite la tarifa por hora: "))

# sueldo básico = horas trabajadas x tarifa por hora
basico = horasTrabajadas * pagoPorHora

# sueldo bruto = sueldo básico + 20% (es decir, multiplicado por 1.20)
bruto = basico * 1.20

# sueldo neto = sueldo bruto - 10% (es decir, multiplicado por 0.90)
neto = bruto * 0.90

print(f"Sueldo básico: S/. {basico:.2f}")
print(f"Sueldo bruto: S/. {bruto:.2f}")
print(f"Sueldo neto: S/. {neto:.2f}")
