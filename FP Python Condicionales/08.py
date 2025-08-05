# 8. Un estudiante recibe una propina mensual S/. 20. El estudiante rinde mensualmente tres examenes. Su papa ha decidido incentivarlo dandole una propina adicional de S/. 5 por cada examen aprobado. Desarrolle el programa que determine el monto total de la propina.
import os
os.system("cls")

ex1 = int(input("Ingrese nota del examen 1: "))
ex2 = int(input("Ingrese nota del examen 2: "))
ex3 = int(input("Ingrese nota del examen 3: "))

propina = 20  # Propina base

# Si aprueba cada examen (mayor a 10), se le suma 5
if ex1 > 10:
    propina = propina + 5
if ex2 > 10:
    propina = propina + 5
if ex3 > 10:
    propina = propina + 5

# Mostrar resultado al final
print(f"El total de la propina es: S/. {propina}")
