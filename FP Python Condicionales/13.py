# 13. Desarrolle el programa que lea un número entero positivo de tres cifras y determine si las cifras son o no consecutivas (en orden ascendente o descendente). En caso contrario mostrar mensaje.

import os
os.system("cls")

numero = int(input("Ingrese numero positivo de 3 digitos: "))

c1 = numero // 100
c2 = (numero // 10) % 10
c3 = numero % 10

if c2 == c1 + 1 and c3 == c2 + 1:
    mensaje = "Las cifras son consecutivas en orden ascendente"
elif c2 == c1 - 1 and c3 == c2 - 1:
    mensaje = "Las cifras son consecutivas en orden descendente"
else:
    mensaje = "Las cifras no son consecutivas"

print(mensaje)
