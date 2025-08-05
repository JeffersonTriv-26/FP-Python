# 1. Una tienda vende un producto a precios unitarios que dependen de la cantidad de unidades adquiridas. Adicionalmente, si el cliente adquiere más de 50 unidades la tienda le descuenta el 15% del importe de la compra; en caso contrario, sólo le descuenta el 5%. Desarrolle el programa que determine el importe de la compra, el descuento y el total a pagar por la compra de cierta cantidad de unidades del producto.
import os
os.system("cls")

horas = float(input("Horas de ausencia del operario: "))
defectuosos = int(input("Cantidad de tornillos defectuosos: "))
buenos = int(input("Cantidad de tornillos buenos: "))

# Evaluación de condiciones
if horas <= 1.5 and defectuosos < 300 and buenos > 10000:
    grado = 20
elif horas <= 1.5 and defectuosos < 300:
    grado = 12
elif horas <= 1.5 and buenos > 10000:
    grado = 13
elif defectuosos < 300 and buenos > 10000:
    grado = 15
elif horas <= 1.5:
    grado = 7
elif defectuosos < 300:
    grado = 8
elif buenos > 10000:
    grado = 9
else:
    grado = 5

print(f"Grado de eficiencia del operario: {grado:.2f}")
