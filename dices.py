'''
Dev: Jaime Quenan
Description: 
Get player name
Generate two random number into 2 dices
Dice 1: 1-6
Dice 2: 1-6
Print dices values
'''
import os
from random import randint, uniform

###########Functions################
def ged_dices():
    os.system('clear')
    print("::: WELCOM TO MY PARCHIS :::")
    #print("Player name: ")
    player_name = input("Player name: ")

    dice1 = randint(1,6)
    dice2 = randint(1,6)

    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")

ged_dices()