import os
os.system("cls")

mes = int(input("Ingresa un número de mes (1 al 12): "))
anio = int(input("Ingresa el año: "))

# Verificamos si el mes es válido
if mes < 1 or mes > 12:
    print("El número de mes no es correcto")
else:
    # Comprobamos cuántos días tiene el mes
    if mes == 2:
        # Verificamos si el año es bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias = 29
        else:
            dias = 28
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias = 31
    else:
        dias = 30

    # Mostramos el nombre del mes
    if mes == 1:
        nombre = "Enero"
    elif mes == 2:
        nombre = "Febrero"
    elif mes == 3:
        nombre = "Marzo"
    elif mes == 4:
        nombre = "Abril"
    elif mes == 5:
        nombre = "Mayo"
    elif mes == 6:
        nombre = "Junio"
    elif mes == 7:
        nombre = "Julio"
    elif mes == 8:
        nombre = "Agosto"
    elif mes == 9:
        nombre = "Septiembre"
    elif mes == 10:
        nombre = "Octubre"
    elif mes == 11:
        nombre = "Noviembre"
    else:
        nombre = "Diciembre"

    print("El mes de", nombre, "tiene", dias, "días.")
