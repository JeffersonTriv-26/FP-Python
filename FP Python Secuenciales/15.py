# 15. Juan, Rosa y Daniel aportan cantidades de dinero para formar un capital. Juan y Rosa aportan en dólares y Daniel, en soles. Desarrolle el programa que determine el capital total en dólares y que porcentaje de dicho capital aporta cada uno. Dólar = S/. 3.00 nuevos soles.
import os
os.system("cls")

aporteJuan = float(input("Monto que aporta Juan (USD): "))
aporteRosa = float(input("Monto que aporta Rosa (USD): "))
aporteDanielSoles = float(input("Monto que aporta Daniel (Soles): "))

cambioDolar = 3.00

# convierto el aporte de Daniel a dólares dividiendo entre el tipo de cambio
aporteDanielDolares = aporteDanielSoles / cambioDolar

# sumo todos los aportes para obtener el capital total en dólares
capitalTotal = aporteJuan + aporteRosa + aporteDanielDolares

# calculo el porcentaje que aporta cada uno respecto al total
porcentajeJuan = (aporteJuan / capitalTotal) * 100
porcentajeRosa = (aporteRosa / capitalTotal) * 100
porcentajeDaniel = (aporteDanielDolares / capitalTotal) * 100

print(f"Capital total en dólares: {capitalTotal:.2f}")
print(f"Juan aporta: {porcentajeJuan:.2f}%")
print(f"Rosa aporta: {porcentajeRosa:.2f}%")
print(f"Daniel aporta: {porcentajeDaniel:.2f}%")
