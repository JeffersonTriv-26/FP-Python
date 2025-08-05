# 36. En una tienda regalan lapiceros de las marcas Lucas, Faber y Pilot según la cantidad de cuadernos comprados:
# - Menos de 12 cuadernos: no hay regalo.
# - Entre 12 y 23 cuadernos: 1 lapicero Lucas por cada 4 cuadernos.
# - Entre 24 y 35 cuadernos: 2 lapiceros Faber por cada 4 cuadernos.
# - 36 o más cuadernos: 2 lapiceros Pilot por cada 4 cuadernos + 1 Faber por cada 6 + 1 Lucas por cada 12.

import os
os.system("cls")

cantidad_cuadernos = int(input("Número de cuadernos comprados: "))

# Inicializamos la cantidad de lapiceros para cada marca
regalo_lucas = 0
regalo_faber = 0
regalo_pilot = 0

if cantidad_cuadernos < 12:
    # No se regalan lapiceros
    regalo_lucas = 0
    regalo_faber = 0
    regalo_pilot = 0
elif cantidad_cuadernos < 24:
    # Regalan 1 lapicero Lucas por cada 4 cuadernos
    regalo_lucas = cantidad_cuadernos // 4
elif cantidad_cuadernos < 36:
    # Regalan 2 lapiceros Faber por cada 4 cuadernos
    regalo_faber = (cantidad_cuadernos // 4) * 2
else:
    # Regalos mixtos para 36 o más cuadernos
    regalo_pilot = (cantidad_cuadernos // 4) * 2
    regalo_faber = cantidad_cuadernos // 6
    regalo_lucas = cantidad_cuadernos // 12

total_lapiceros = regalo_lucas + regalo_faber + regalo_pilot

print(f"Lapiceros Lucas: {regalo_lucas}")
print(f"Lapiceros Faber: {regalo_faber}")
print(f"Lapiceros Pilot: {regalo_pilot}")
print(f"Total de lapiceros regalados: {total_lapiceros}")
