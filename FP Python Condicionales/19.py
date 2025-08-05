import os
os.system("cls")

sexo = input("Escriba su sexo (masculino/femenino): ").lower()
edad = int(input("Escriba su edad: "))

if sexo == "femenino":
    if edad < 23:
        categoria = "FA"  # Femenino y menor de 23
    else:
        categoria = "FB"  # Femenino y 23 o más

elif sexo == "masculino":
    if edad < 25:
        categoria = "MA"  # Masculino y menor de 25
    else:
        categoria = "MB"  # Masculino y 25 o más

else:
    categoria = "Error"  # Sexo no valido

print(f"Sexo: {sexo}")
print(f"Edad: {edad}")
print(f"Categoria: {categoria}")
