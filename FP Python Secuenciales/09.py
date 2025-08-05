# 9. Desarrolle el programa que lea un número entero y determine la suma de sus cifras. Asumir que el número es positivo y de 4 cifras.
import os
os.system("cls")

numeroIngresado = int(input("Digite un número positivo de 4 dígitos: "))

digitoMil = numeroIngresado // 1000
digitoCen = (numeroIngresado // 100) % 10
digitoDec = (numeroIngresado // 10) % 10
digitoUni = numeroIngresado % 10

sumaTotalCifras = digitoMil + digitoCen + digitoDec + digitoUni

print(f"\nLa suma total de las cifras es: {sumaTotalCifras}")
