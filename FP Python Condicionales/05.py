# 5. Desarrolle el programa que, dado un numero de 4 cifras, forme el mayor numero posible de dos cifras usando la mayor y menor cifra del numero ingresado.
import os
os.system("cls")

num = int(input("Ingrese un numero de 4 cifras: "))

# Extraemos los 4 digitos del numero ingresado
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

# Determinamos el mayor y el menor digito
mayor = max(d1, d2, d3, d4)
menor = min(d1, d2, d3, d4)

# Formamos dos numeros de dos cifras con mayor y menor en diferentes posiciones
opcion1 = mayor * 10 + menor
opcion2 = menor * 10 + mayor

# El resultado sera el mayor de las dos opciones
mayorDosCifras = max(opcion1, opcion2)

# Mostramos el resultado al final
print(f"El mayor numero de dos cifras que se puede formar es: {mayorDosCifras}")
