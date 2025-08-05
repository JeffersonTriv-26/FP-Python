import os
os.system("cls")

donacion = int(input("Ingrese la donacion anual: "))

if donacion >= 10000:
    salud = donacion * 30 // 100  # 30% al centro de salud
    comedor = donacion * 50 // 100  # 50% al comedor
else:
    salud = donacion * 25 // 100  # 25% al centro de salud
    comedor = donacion * 60 // 100  # 60% al comedor

bolsa = donacion - (salud + comedor)  # Lo que queda va a la bolsa

print(f"Donacion total: ${donacion}")
print(f"Centro de salud: ${salud}")
print(f"Comedor de ninos: ${comedor}")
print(f"Inversion en bolsa: ${bolsa}")
