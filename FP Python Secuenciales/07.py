# 7. Desarrolle el programa que determine el área y el perímetro de un rectángulo sabiendo que el área = b x h, perímetro = 2x (b+h).
import os
os.system("cls")

valorBase = float(input("Ingrese la medida de la base: "))
valorAltura = float(input("Ingrese la medida de la altura: "))

resultadoArea = valorBase * valorAltura
resultadoPerimetro = 2 * (valorBase + valorAltura)

print(f"El área del rectángulo es: {resultadoArea:.2f}")
print(f"El perímetro del rectángulo es: {resultadoPerimetro:.2f}")
