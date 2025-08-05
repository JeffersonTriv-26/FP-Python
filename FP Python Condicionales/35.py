# 35. Una compañía asigna un código de tres dígitos a cada trabajador.
# Según la divisibilidad del código, se define su categoría:
# - Si es divisible por 2, 3 y 5: Administrativo
# - Si es divisible por 3 y 5, pero no por 2: Directivo
# - Si es divisible solo por 2: Vendedor
# - Si no es divisible por 2, 3 ni 5: Seguridad

import os
os.system("cls")

codigo_empleado = int(input("Ingrese el código de 3 dígitos del trabajador: "))

# Evaluamos las condiciones para clasificar al trabajador
if codigo_empleado % 2 == 0 and codigo_empleado % 3 == 0 and codigo_empleado % 5 == 0:
    categoria = "Administrativo"
elif codigo_empleado % 3 == 0 and codigo_empleado % 5 == 0 and codigo_empleado % 2 != 0:
    categoria = "Directivo"
elif codigo_empleado % 2 == 0 and codigo_empleado % 3 != 0 and codigo_empleado % 5 != 0:
    categoria = "Vendedor"
else:
    categoria = "Seguridad"

print(f"Categoría del trabajador: {categoria}")
