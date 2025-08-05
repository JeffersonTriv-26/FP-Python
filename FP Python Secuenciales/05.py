import os
os.system("cls")

capacidadGB = float(input("Digite la capacidad del disco duro en Gigabytes (GB): "))

# Conversión a unidades menores
capacidadMB = capacidadGB * 1024
capacidadKB = capacidadMB * 1024
capacidadBytes = capacidadKB * 1024

print(f"\nCapacidad en Megabytes: {capacidadMB:.2f} MB")
print(f"Equivalente en Kilobytes: {capacidadKB:.2f} KB")
print(f"Total en Bytes: {capacidadBytes:.2f} B")
