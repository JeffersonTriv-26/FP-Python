# 16. Una constructora vende casas con las siguientes opciones: si el ingreso mensual del comprador es menor a S/. 1250, la inicial sera del 15% del precio de la casa y el resto se pagara en 120 meses. Si el ingreso es S/. 1250 o mas, la inicial sera del 30% y el saldo se divide en 75 cuotas. Elaborar el programa que calcule la cuota inicial y la mensualidad.

import os
os.system("cls")

ingreso = float(input("Ingrese su ingreso mensual: S/ "))
precio_casa = float(input("Ingrese el precio de la casa: S/ "))

if ingreso < 1250:
    inicial = precio_casa * 0.15
    cuotas = 120
else:
    inicial = precio_casa * 0.30
    cuotas = 75

saldo_restante = precio_casa - inicial
cuota_mensual = saldo_restante / cuotas

print(f"Cuota Inicial: S/. {inicial:.2f}")
print(f"Cuota Mensual: S/. {cuota_mensual:.2f}")
print(f"Total de Cuotas: {cuotas}")
