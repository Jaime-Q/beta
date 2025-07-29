import os
import random


def solicitar_jugadores():
    while True:
        try:
            jugadores = int(input("Cantidad de jugadores🧍 => 2 a 4 <=): "))
            if 2 <= jugadores <= 4:
                return jugadores
            else:
                print("Debes ingresar entre => 2 y 4 <= jugadores🧍.")
        except ValueError:
            print(" ❌Fallo. Ingresa un número entero.❌ ")

def seleccionar_nivel():
    niveles = {
        1: 20,
        2: 30,
        3: 50,
        4: 100
    }
    while True:
        try:
            print("\n Seleccionar nivel:")
            print("1. Nivel básico (20 posiciones)")
            print("2. Nivel intermedio (30 posiciones)")
            print("3. Nivel avanzado (50 posiciones)")
            print("4. Nivel experto (100 posiciones)")
            nivel = int(input("Nivel elegido: "))
            if nivel in niveles:
                return niveles[nivel]
            else:
                print(" ✅Selección inválida.✅ ")
        except ValueError:
            print(" ❌Fallo. Ingresa un número entero.❌ ")

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def carrera_numerica():
    jugadores = solicitar_jugadores()
    meta = seleccionar_nivel()
    posiciones = [0] * jugadores
    pares_consecutivos = [0] * jugadores
    turno = 0

    print(f"\n 🏁¡Inicia la Carrera Numérica hasta la meta de {meta} posiciones!🏁 \n")

    while True:
        jugador_actual = turno % jugadores
        dado1, dado2 = lanzar_dados()
        suma = dado1 + dado2
        print(f"Jugador🧍 {jugador_actual + 1} lanza: 🎲 {dado1} y 🎲 {dado2} → mueve {suma} posiciones")

        if dado1 == dado2:
            pares_consecutivos[jugador_actual] += 1
            print(f"¡Par #{pares_consecutivos[jugador_actual]} consecutivo!")
            if pares_consecutivos[jugador_actual] == 3:
                print(f"\n🏆 ¡Jugador🧍 {jugador_actual + 1} gana automáticamente con 3 pares consecutivos!👑👑")
                break
        else:
            pares_consecutivos[jugador_actual] = 0

        posiciones[jugador_actual] += suma

        if posiciones[jugador_actual] >= meta:
            print(f"\n¡Jugador🧍 {jugador_actual + 1} ha alcanzado la meta y gana la carrera!👑👑")
            break

        turno += 1
        input("Presiona Enter para continuar al siguiente turno...\n")

if __name__ == "__main__":
    carrera_numerica()
