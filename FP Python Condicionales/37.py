# 37. En una elección democrática a la presidencia de un club femenino participan Pamela, Carol y Fanny. Para ganar la elección se requiere obtener la mitad de los votos emitidos más uno. En caso de no haber ganador, pasan a una segunda vuelta los candidatos que alcanzaron los dos primeros puestos; se anula la elección si hay empate entre los tres o si hay empate por el segundo puesto. Desarrolle el programa que muestre en que puesto quedaron los candidatos.
import os
os.system("cls")

ana = int(input("Votos para Ana: "))
brenda = int(input("Votos para Brenda: "))
diana = int(input("Votos para Diana: "))

total_votos = ana + brenda + diana
mitad_mas_uno = total_votos / 2 + 1

if ana >= mitad_mas_uno:
    print("Ana gana directamente en primera vuelta.")
elif brenda >= mitad_mas_uno:
    print("Brenda gana directamente en primera vuelta.")
elif diana >= mitad_mas_uno:
    print("Diana gana directamente en primera vuelta.")
else:
    if ana == brenda == diana:
        print("Empate total entre las tres. Elección anulada.")
    elif ana == brenda and ana > diana:
        print("Segunda vuelta entre Ana y Brenda.")
    elif ana == diana and ana > brenda:
        print("Segunda vuelta entre Ana y Diana.")
    elif brenda == diana and brenda > ana:
        print("Segunda vuelta entre Brenda y Diana.")
    elif ana > brenda and brenda == diana:
        print("Empate en segundo puesto. Elección anulada.")
    elif brenda > ana and ana == diana:
        print("Empate en segundo puesto. Elección anulada.")
    elif diana > ana and ana == brenda:
        print("Empate en segundo puesto. Elección anulada.")
    elif ana > brenda and brenda > diana:
        print("Segunda vuelta entre Ana y Brenda.")
    elif ana > diana and diana > brenda:
        print("Segunda vuelta entre Ana y Diana.")
    elif brenda > ana and ana > diana:
        print("Segunda vuelta entre Brenda y Ana.")
    elif brenda > diana and diana > ana:
        print("Segunda vuelta entre Brenda y Diana.")
    elif diana > ana and ana > brenda:
        print("Segunda vuelta entre Diana y Ana.")
    else:
        print("Segunda vuelta entre Diana y Brenda.")
