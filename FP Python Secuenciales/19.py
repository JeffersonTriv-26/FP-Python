# 19. Una empresa paga a sus vendedores un sueldo básico mensual de S/. 500. El sueldo bruto es igual al sueldo básico más una comisión, que es igual al 9% del monto total vendido. Por ley, todo vendedor se somete a un descuento del 11%. Desarrolle el programa que calcule la comisión, el sueldo bruto, el descuento y el sueldo neto de un vendedor de la empresa.
import os
os.system("cls")

ventasTotales = int(input("Digite el monto total de las ventas (sin decimales): "))

sueldoFijo = 500

# la comisión es el 9% de las ventas
comisionVendedor = ventasTotales * 9 // 100

# sueldo bruto es el sueldo fijo más la comisión
sueldoBruto = sueldoFijo + comisionVendedor

# descuento del 11% sobre el sueldo bruto
descuentoLey = sueldoBruto * 11 // 100

# sueldo neto es el sueldo bruto menos el descuento
sueldoFinal = sueldoBruto - descuentoLey

print(f"Comisión: S/. {comisionVendedor}")
print(f"Sueldo Bruto: S/. {sueldoBruto}")
print(f"Descuento de Ley: S/. {descuentoLey}")
print(f"Sueldo Neto: S/. {sueldoFinal}")
