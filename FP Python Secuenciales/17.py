# 17. Una institución social recibe anualmente una donación que reparte de la siguiente forma: 25% para el centro de salud, 35% en el comedor infantil, 25% para la escuela infantil y el resto para el asilo de ancianos. Desarrolle el programa que muestre los montos asignados.
import os
os.system("cls")

montoDonacion = int(input("Digite el monto total de la donación (solo enteros): "))

# se calcula el 25% para el centro de salud
centroSalud = montoDonacion * 25 // 100

# se asigna el 35% al comedor infantil
comedorInfantil = montoDonacion * 35 // 100

# se destina el 25% a la escuela infantil
escuelaInfantil = montoDonacion * 25 // 100

# el resto es para el asilo de ancianos (lo que queda después de sumar los otros)
asiloAncianos = montoDonacion - (centroSalud + comedorInfantil + escuelaInfantil)

print(f"Centro de Salud: S/. {centroSalud}")
print(f"Comedor Infantil: S/. {comedorInfantil}")
print(f"Escuela Infantil: S/. {escuelaInfantil}")
print(f"Asilo de Ancianos: S/. {asiloAncianos}")
