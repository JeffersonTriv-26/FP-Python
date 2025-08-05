import os
os.system("cls")

tramoKilometros = float(input("Digite la distancia del primer tramo (en kilómetros): "))
tramoPies = float(input("Ahora ingrese la distancia del segundo tramo (en pies): "))
tramoMillas = float(input("Finalmente, indique la distancia del tercer tramo (en millas): "))

# Conversión de unidades
primerTramoMetros = tramoKilometros * 1000
segundoTramoMetros = tramoPies / 3.2808
tercerTramoMetros = tramoMillas * 1609

# Suma de las distancias en metros
distanciaTotalMetros = primerTramoMetros + segundoTramoMetros + tercerTramoMetros

# Conversión total a yardas
distanciaTotalYardas = distanciaTotalMetros / 0.9144

print(f"\n>>> La distancia total que ha recorrido es de: {distanciaTotalMetros:.2f} metros")
print(f">>> Equivalente a: {distanciaTotalYardas:.2f} yardas")
