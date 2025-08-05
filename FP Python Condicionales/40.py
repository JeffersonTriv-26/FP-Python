# 40. En un instituto los cursos de matemática, física y química se evalúan en base a tres prácticas calificadas, examen parcial y final. Cada práctica tiene un peso dado. Desarrolle el programa que determine el promedio final del curso y su condición de aprobado / desaprobado dado que la nota mínima es de 13.
import os
os.system("cls")

asignatura = input("Escribe el nombre del curso (matematica, fisica, quimica): ").lower()

# Ingreso de notas como enteros
nota1 = int(input("Nota de práctica 1: "))
nota2 = int(input("Nota de práctica 2: "))
nota3 = int(input("Nota de práctica 3: "))
parcial = int(input("Nota de examen parcial: "))
final = int(input("Nota de examen final: "))

# Cálculo del promedio final según el curso
if asignatura == "matematica":
    promedio = nota1 * 0.10 + nota2 * 0.20 + nota3 * 0.10 + parcial * 0.30 + final * 0.30
elif asignatura == "fisica":
    promedio = (nota1 + nota2 + nota3 + parcial + final) / 5
elif asignatura == "quimica":
    promedio = nota1 * 0.10 + nota2 * 0.30 + nota3 * 0.10 + parcial * 0.25 + final * 0.25
else:
    promedio = 0

# Verificamos si aprueba
if promedio >= 13:
    estado = "Aprobado"
else:
    estado = "Desaprobado"

# Mostramos el resultado con dos decimales
print(f"Promedio final del curso: {promedio:.2f} - {estado}")
