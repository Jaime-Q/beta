'''
Script description:
Crea un script Python que lance dos dados N veces y visualice por pantalla los resultados.

La cantidad o numero de veces debe ser ingresada por el usuario.
Debe lanzarce dos dados.
Usar funcion.
'''

import os 
from random import randint

lan = int(input('¿Cuantas veces deseas lanzar los dados?: '))

i = 1
while i <= lan :
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    print(f"Lanzamiento {i}: ")
    print(f"Dices 1: {d1}")
    print(f"Dices 2: {d2}")
    print("\n")
    
    i+=1