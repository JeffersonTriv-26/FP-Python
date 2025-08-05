# 11. Desarrolle el programa que determine el signo de un número entre positivo, negativo y cero.

import os
os.system("cls")

numero = int(input("Numero: "))

if numero > 0:
    signo = "Positivo"
elif numero == 0:
    signo = "Cero"
else:
    signo = "Negativo"

print(f"El numero ingresado es: {signo}")
