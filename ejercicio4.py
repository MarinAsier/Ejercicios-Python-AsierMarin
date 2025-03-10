# coding=utf-8
__Author__="Asier Marin Saez"

"""Escriba un programa que simule el juego **Piedra, papel, tijera** para dos jugadores. Las reglas del juego son las siguientes: 
    Simultáneamente, los dos jugadores muestran una mano en tres posibles posiciones:
    - **Piedra:** se muestra el puño cerrado.
    - **Papel:** se muestra la palma de la mano.
    - **Tijera:** se muestra la palma de la mano con los dedos separados en dos grupos.
    - El jugador que ha sacado **Piedra** gana al jugador que ha sacado *Tijera*.
    - El jugador que ha sacado **Tijera** gana al jugador que ha sacado *Papel*.
    - El jugador que ha sacado **Papel** gana al jugador que ha sacado *Piedra*."""


import random

# Función que determina quien gana Piedra, papel o tijera
# 0: Empate.
# 1: Gana Jugador 1.
# 2: Gana Jugador 2.

def quienGana(jugada1, jugada2) :
    if jugada1 == jugada2 :
        return 0
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "tijera" and jugada2 == "papel") or \
         (jugada1 == "papel" and jugada2 == "piedra") :
        return 1
    # --> Complete su código <--
    else :
        return 2

# Programa principal
def main():
    print("PIEDRA, PAPEL, ... ¡TIJERA!")

    nombre1 = input("Introduzca el nombre del Jugador 1: ")
    nombre2 = input("Introduzca el nombre del Jugador 2: ")
    numeroTirada = int(input("Introduzca el número de tiradas: "))

    ganadas1=0
    ganadas2=0

    while numeroTirada > 0 :
        print("Tirada nº " + str(numeroTirada) + ":")
        j1 = random.choice(["piedra", "papel", "tijera"])
        j2 = random.choice(["piedra", "papel", "tijera"]) # Implemente tirada aleatoria para el jugador 2.
        
        print(nombre1 + " ha sacado " + j1 + ".")
        print(nombre2 + " ha sacado " + j2 + ".")
        
        ganador=quienGana(j1,j2)
        
        if ganador == 0 :
            print("Han empatado.")
        elif ganador == 1 :
            print("Gana "+nombre1)
            ganadas1=ganadas1+1
        elif ganador == 2 :
            print("Gana "+nombre2)
            ganadas2=ganadas2+1
        else :
            print("Error.")
        
        numeroTirada -= 1

    # Resultado final de todas las tiradas
    print("\nRESULTADO FINAL:")
    if ganadas1 == ganadas2 :
        print("HAN EMPATADO")
   # --> Complete código <--
    elif ganadas1 > ganadas2:
        print("GANA " + nombre1 + " con " + str(ganadas1) + " Victorias")
    else :
        print("GANA " + nombre2 + " con " + str(ganadas2) + " Victorias")


if __name__== "__main__" :
   main()
