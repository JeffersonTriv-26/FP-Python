# 28. Dado una hora en formato de 24 horas, mostrarla en formato de 12 horas AM/PM.
# Si la hora es invalida, mostrar mensaje de error.

import os
os.system("cls")

# Ingresar la hora y minutos
hora = int(input("Ingresa la hora (0-23): "))
minuto = int(input("Ingresa los minutos (0-59): "))

# Validar si la hora y minutos son correctos
if hora >= 0 and hora < 24 and minuto >= 0 and minuto < 60:
    
    # Si es medianoche (0 horas)
    if hora == 0:
        h12 = 12
        periodo = "AM"
    
    # Si es antes del medio dia
    elif hora < 12:
        h12 = hora
        periodo = "AM"
    
    # Si es medio dia (12 horas)
    elif hora == 12:
        h12 = 12
        periodo = "PM"
    
    # Si es despues del medio dia
    else:
        h12 = hora - 12
        periodo = "PM"
    
    # Mostrar la hora en formato 12h
    print(f"{h12}:{minuto:02d} {periodo}")

else:
    print("Hora invalida")
