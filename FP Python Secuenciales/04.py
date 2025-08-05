import os
os.system("cls")

cantidadPies = float(input("Indique la cantidad de pies (ft): "))
cantidadPulgadas = float(input("Ingrese la cantidad de pulgadas (in): "))

# Factores de conversión
factorPieAMetros = 0.3048
factorPulgadaAMetros = 0.0254

# Cálculo de estatura total en metros
totalEnMetros = (cantidadPies * factorPieAMetros) + (cantidadPulgadas * factorPulgadaAMetros)

print(f"\n>> La estatura total en el sistema métrico es: {totalEnMetros:.3f} metros")
