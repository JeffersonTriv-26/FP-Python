# 33. Una empresa evalúa a sus empleados bajo dos criterios: puntualidad y rendimiento.
# Según esos puntajes, calcula una bonificación anual.
# Desarrolle el programa que calcule los puntajes y la bonificación correspondiente.

import os
os.system("cls")

# Pedimos minutos de tardanza y número de observaciones
tardanza = int(input("Ingrese minutos de tardanza: "))
observaciones = int(input("Ingrese número de observaciones: "))

# Asignamos puntaje por puntualidad según la cantidad de tardanza
if tardanza == 0:
    punt_puntualidad = 10
elif 1 <= tardanza <= 2:
    punt_puntualidad = 8
elif 3 <= tardanza <= 5:
    punt_puntualidad = 6
elif 6 <= tardanza <= 9:
    punt_puntualidad = 4
else:
    punt_puntualidad = 0

# Asignamos puntaje por rendimiento según las observaciones
if observaciones == 0:
    punt_rendimiento = 10
elif observaciones == 1:
    punt_rendimiento = 8
elif observaciones == 2:
    punt_rendimiento = 5
elif observaciones == 3:
    punt_rendimiento = 1
else:
    punt_rendimiento = 0

# Sumamos los puntajes para obtener el total
punt_total = punt_puntualidad + punt_rendimiento

# Calculamos la bonificación según el puntaje total
if punt_total < 11:
    bonificacion = punt_total * 2.5
elif 11 <= punt_total <= 13:
    bonificacion = punt_total * 5.0
elif 14 <= punt_total <= 16:
    bonificacion = punt_total * 7.5
elif 17 <= punt_total <= 19:
    bonificacion = punt_total * 10.0
else:
    bonificacion = punt_total * 12.5

# Mostramos los resultados finales
print(f"Puntaje total: {punt_total}")
print(f"Bonificación: S/. {bonificacion:.2f}")
