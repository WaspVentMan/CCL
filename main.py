# Jacob A. G. Taylor, 2022

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
    print(colour(1, 36, 40, "\n[DEBUG]") + " It is currently: " + date_time()[0] + ", " + date_time()[1] + ", " + str(date_time()[2]) + date_time()[3] + " " + date_time()[4] + " " + str(date_time()[5]))
    exit = CMD_Input(input("\n>>> "))