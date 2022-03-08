# Jacob A. G. Taylor, https://github.com/WaspVentMan, 2022

import os
from functions.colour import *
from functions.CMD_Input import CMD_Input
from functions.date_time import date_time

os.system('cls' if os.name == 'nt' else 'clear')

print(colour(1, 36, 40, "[DEBUG]") + " Running C.C.L. BETA 2")
print(colour(1, 36, 40, "[DEBUG]") + " \"help\" for commands.")
print(colour(1, 36, 40, "[DEBUG]") + " \"exit\" to exit.")
print(colour(1, 36, 40, "[DEBUG]") + " Created by Jacob A. G. Taylor, 2022")

exit = False
while exit != True:
    exit = CMD_Input(input("\n>>> "))