import os
os.system("cls")

num = int(input("Numero de 4 cifras: "))

# Extraigo la primera cifra (estado civil)
estado = num // 1000

# Extraigo las dos cifras del medio (edad)
edad = (num % 1000) // 10

# Extraigo la ultima cifra (sexo)
sexo = num % 10

# Determino estado civil segun el numero
if estado == 1:
    estado = "soltero"
elif estado == 2:
    estado = "casado"
elif estado == 3:
    estado = "divorciado"
elif estado == 4:
    estado = "viudo"
else:
    estado = "desconocido"

# Determino sexo segun el numero
if sexo == 1:
    sexo = "masculino"
elif sexo == 2:
    sexo = "femenino"
else:
    sexo = "desconocido"

print(f"Estado civil: {estado}")
print(f"Edad: {edad}")
print(f"Sexo: {sexo}")
