# Jacob A. G. Taylor, https://github.com/WaspVentMan, 2022

from functions.colour import *
import os

def ace(input):
    try:
        os.system("echo " + input[4:] + " > ace.py && py ace.py")
    except:
        pass
    os.remove("ace.py")