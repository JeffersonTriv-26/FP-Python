# 25. Una empresa ha decidido otorgar una bonificación por fiestas patrias a sus empleados.
# Si el empleado tiene más de un hijo, recibirá una bonificación igual al 12.5% de su sueldo bruto
# más S/. 40 por cada hijo; en caso contrario, solo recibirá una bonificación del 10%.
# Elaborar el programa que muestre la bonificación y el sueldo neto a pagar.

import os
os.system("cls")

# Ingreso de sueldo bruto y cantidad de hijos
sueldo_bruto = int(input("Ingrese sueldo bruto: "))
hijos = int(input("Ingrese numero de hijos: "))

# Si tiene mas de 1 hijo, aplica bonificación de 12.5% + S/. 40 por cada hijo
if hijos > 1:
    bonificacion = sueldo_bruto * 125 // 1000 + (40 * hijos)
# Si no, solo recibe el 10% de bonificación
else:
    bonificacion = sueldo_bruto * 10 // 100

# Sumar la bonificación al sueldo bruto para obtener el sueldo neto
sueldo_neto = sueldo_bruto + bonificacion

# Mostrar resultados
print(f"Bonificacion: S/ {bonificacion}")
print(f"Sueldo neto: S/ {sueldo_neto}")
