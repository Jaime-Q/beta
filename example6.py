import os
from random import randint, uniform

def ged_dices():
    os.system('clear')
    
    player_name = input("Player name: ")

    dice1 = randint(1,6)
    dice2 = randint(1,6)

    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")

    if dice1 % 2 == 0 and dice2 % 2 == 0:
        print("::  🎉 YOU WIND 🎉  ::")
    else:
        print("::  😢 YOU LOSE 😢  ::")

ged_dices()