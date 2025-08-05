# 30. Una empresa cobra la cuota mensual con descuentos o recargos segun el dia de pago.
# Si paga en los primeros 10 dias, descuento.
# Si paga del dia 11 al 20, no hay descuento.
# Si paga despues del dia 20, hay recargo.

import os
os.system("cls")

# Ingresar monto de la cuota y dia de pago
cuota = int(input("Cuota mensual: "))
dia = int(input("Dia de pago: "))

# Si paga dentro de los primeros 10 dias, se aplica descuento
if dia >= 1 and dia <= 10:
    descuento = max(5, cuota * 0.02)  # El descuento es el mayor entre $5 y el 2% de la cuota
    total = cuota - descuento

# Si paga entre el dia 11 al 20, no hay descuento
elif dia >= 11 and dia <= 20:
    total = cuota

# Si paga despues del dia 20 hasta el 31, se aplica recargo
elif dia >= 21 and dia <= 31:
    recargo = max(10, cuota * 0.03)  # El recargo es el mayor entre $10 y el 3% de la cuota
    total = cuota + recargo

# Si el dia ingresado no es valido, mostramos error
else:
    total = None
    print("Dia de pago incorrecto")

# Mostrar el total a pagar solo si es valido
if total is not None:
    print(f"Total a pagar: ${total:.2f}")
