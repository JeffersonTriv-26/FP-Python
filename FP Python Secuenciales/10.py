# 10. Dado un número natural de cuatro cifras, desarrolle el programa que permite obtener el número al revés. Ejemplo 1234 → 4321.
numero = input("Ingrese un número de 4 cifras: ")

# Sacamos cada dígito por su posición
dig1 = numero[3] #los numeros indican la posición de los números
dig2 = numero[2]
dig3 = numero[1]
dig4 = numero[0]

# Unimos los dígitos al revés
numero_invertido = dig1 + dig2 + dig3 + dig4

print("Número invertido:", numero_invertido)
