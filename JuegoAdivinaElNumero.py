# Se importa los mudolos que vamos a utilizar
from Mensaje import Mensaje
from Aleatorio import Aleatorio, Rango

# parametro de la lista de rango para adivinar
rangoA = 1
rangoB = 21

# Asignamos el mensaje de bienvenida y color del mensaje a mostrar
mensaje_bienvenido = f'''\n¡Bienvenido a Adivina el Número!
En este juego, deberás de adivinar el número en el que estoy pensando.
El número está entre {rangoA} al {rangoB-1}. 
¡Gana quien adivine en el menor número de intentos! \n'''
color_mensaje_bienvenido = 34

# mostramos por pantalla el mensaje de bienvenida
print(Mensaje(color_mensaje_bienvenido,mensaje_bienvenido))

# numero aleatorio generado
numero_aleatorio=str(Aleatorio(rangoA,rangoB))

# lista para adivinar
numeros_lista=Rango().numeros(rangoA,rangoB)
print(f"{numeros_lista} \n")

while True:
    numero_adivinado = input(Mensaje(32,"Adivina el número: "))
    if int(numero_adivinado) > len(numeros_lista) or int(numero_adivinado) == 0:
        print(Mensaje(31,"Numero fuera del rango !!"))
    else:
        if numero_aleatorio == numero_adivinado:
            print(Mensaje(35,"Felicidanes adivinaste el numero"))
            break
        else:
            numeros_lista=Rango().reemplazar_x(numeros_lista,numero_adivinado)
            print(f"{numeros_lista} \n")