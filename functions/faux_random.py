# Jacob A. G. Taylor, https://github.com/WaspVentMan, 2022

import os

def random_single():
    select = 0
    os.system("echo > r")
    fileStatsObj = os.stat("r")
    os.remove("r")
    select = int(str(fileStatsObj[1])[15:16]) + 6
    select = int(str((fileStatsObj[1]))[select:select+1]) + 6
    return int(str((fileStatsObj[1]))[select:select+1])

def randint(low: int, high: int):
    """
    Randint()

    Randomly generates numbers in certain perameters, pretty simple.
    
    (Still WIP)
    """
    random = ""
    if low > high:
        return "error"

    for x in range(len(str(high))):
        random += str(random_single())

    while int(random) > high - low:
        random = int(random) / 5
        
    return int(random)
