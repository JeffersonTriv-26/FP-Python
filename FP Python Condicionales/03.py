# 3. Los angulos se clasifican de la siguiente manera: nulo (0°), Agudo (0°< x < 90°), Recto (90°), Obtuso (90° < x <180°), Llano (180°), Concavo (180°< x < 360°), Completo (360°). Desarrolle el programa que determine la clasificacion de un angulo dado en grados.
import os
os.system("cls")

grado = float(input("Ingrese el valor del angulo en grados: "))

# Variable para almacenar la clasificacion del angulo
tipoAngulo = ""

if grado == 0:
    tipoAngulo = "Angulo Nulo"
elif 0 < grado < 90:
    tipoAngulo = "Angulo Agudo"
elif grado == 90:
    tipoAngulo = "Angulo Recto"
elif 90 < grado < 180:
    tipoAngulo = "Angulo Obtuso"
elif grado == 180:
    tipoAngulo = "Angulo Llano"
elif 180 < grado < 360:
    tipoAngulo = "Angulo Concavo"
elif grado == 360:
    tipoAngulo = "Angulo Completo"
else:
    tipoAngulo = "Angulo fuera de clasificacion"

# Mostrar resultado
print(f"Clasificacion: {tipoAngulo}")
