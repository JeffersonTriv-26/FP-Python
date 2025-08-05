# 39. Desarrolle el programa para obtener el grado de eficiencia de un operario de torno para obtener el grado de eficiencia de un operario de torno de una fábrica productora de tornillos de acuerdo a las siguientes condiciones: No más de 1.5 horas de ausencia al trabajo. Menos de 300 tornillos defectuosos producidos. Más de 10000 tornillos no defectuosos producidos. Los grados de eficiencia para cada trabajador son asignados de la siguiente manera: Si no cumple ninguna condición, grado 5. Si sólo cumple la primera, grado 7. Si sólo cumple la segunda, grado 8. Si sólo cumple la tercera, grado 9. Si cumple la primera y segunda condición, grado 12. Si cumple la primera y tercera condición, grado 13. Si cumple la segunda y tercera condición, grado 15. Si cumple las tres condiciones, grado 20.
import os
os.system("cls")

ausencia = float(input("Ingrese horas de ausencia: "))
defectuosos = int(input("Ingrese tornillos defectuosos: "))
no_defectuosos = int(input("Ingrese tornillos no defectuosos: "))

cond1 = ausencia <= 1.5
cond2 = defectuosos < 300
cond3 = no_defectuosos > 10000

if cond1 and cond2 and cond3:
    grado = 20
elif cond1 and cond2:
    grado = 12
elif cond1 and cond3:
    grado = 13
elif cond2 and cond3:
    grado = 15
elif cond1:
    grado = 7
elif cond2:
    grado = 8
elif cond3:
    grado = 9
else:
    grado = 5

print(f"Grado de eficiencia: {grado}")
