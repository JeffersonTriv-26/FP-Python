# 11. Dado dos números enteros de 3 cifras, desarrolle el programa que muestre la cifra primera y tercera cifras intercambiadas entre ambos números. Ejemplo 123 y 456 → 624 y 351

n1 = input("Ingrese el primer número de 3 cifras: ")
n2 = input("Ingrese el segundo número de 3 cifras: ")

# Intercambiar la primera y tercera cifra directamente usando posiciones
nuevo1 = n2[0] + n1[1] + n1[2]
nuevo2 = n1[0] + n2[1] + n2[2]

print("Nuevos números:", nuevo1, "y", nuevo2)
