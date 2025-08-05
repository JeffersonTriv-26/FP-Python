# 23. Un padre ha decido dar una propina a su hijo en base a las notas en Matematicas y Fisica.
# Si la nota de Matematicas es mayor a 17, le dara S/. 3, en caso contrario le dara S/. 1 por cada punto.
# Si la nota de Fisica es mayor a 15, le dara S/. 2, en caso contrario S/. 0.50.
# Ademas, si el promedio de las dos notas es mayor a 16, le regalara un reloj.

import os
os.system("cls")

# Ingreso de notas
matematica = int(input("Ingresa nota de Matematica: "))
fisica = int(input("Ingresa nota de Fisica: "))

# Propina por Matematica
if matematica > 17:
    propina_matematica = 3
else:
    propina_matematica = matematica * 1

# Propina por Fisica
if fisica > 15:
    propina_fisica = 2
else:
    propina_fisica = fisica * 0.5

# Sumo ambas propinas
total_propina = propina_matematica + propina_fisica

# Calculo el promedio de las dos notas
promedio = (matematica + fisica) / 2

# Determino si le regalan reloj
reloj = "SI" if promedio > 16 else "NO"

# Muestro resultados
print(f"Propina total: S/ {total_propina}")
print(f"Reloj: {reloj}")
