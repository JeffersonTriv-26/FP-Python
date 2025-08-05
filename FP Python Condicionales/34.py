# 34. El índice de masa corporal (IMC) permite medir el grado de sobrepeso u obesidad de una persona.
# Se calcula como: IMC = peso / estatura^2. Desarrolle el programa que calcule el IMC de una persona.

import os
os.system("cls")

# Pedimos al usuario su peso (en kilogramos) y estatura (en metros)
peso = int(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Calculamos el IMC usando la fórmula peso / estatura^2
imc = peso / (estatura ** 2)

# Evaluamos el grado según el valor del IMC
if imc < 20:
    grado = "Delgado"
elif 20 <= imc <= 25:
    grado = "Normal"
elif 25 < imc <= 27:
    grado = "Sobrepeso"
else:
    grado = "Obesidad"

# Mostramos el resultado del IMC y el grado correspondiente
print(f"IMC: {imc:.2f} - {grado}")
