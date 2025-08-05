import os
os.system("cls")

varones = float(input("Ingrese la cantidad de Varones:"))
mujeres = float(input("Ingrese la cantidad de Mujeres:"))

Total = varones + mujeres

PVarones = varones / Total * 100
PMujeres = mujeres / Total * 100

print(f"el porcentaje de Varones es: {PVarones:.2f} %")
print(f"el porcentaje de Mujeres es: {PMujeres:.2f} %")
