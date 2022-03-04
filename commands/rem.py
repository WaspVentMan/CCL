# Jacob A. G. Taylor, 2022

import os
from functions.colour import colour

def image_colour(data) -> str:
    if   str(data) == "0" : data = "\033[30;"
    elif str(data) == "1" : data = "\033[90;"
    elif str(data) == "2" : data = "\033[37;"
    elif str(data) == "3" : data = "\033[97;"
    elif str(data) == "4" : data = "\033[33;"
    elif str(data) == "5" : data = "\033[93;"
    elif str(data) == "6" : data = "\033[31;"
    elif str(data) == "7" : data = "\033[91;"
    elif str(data) == "8" : data = "\033[35;"
    elif str(data) == "9" : data = "\033[95;"
    elif str(data) == "a" : data = "\033[34;"
    elif str(data) == "b" : data = "\033[94;"
    elif str(data) == "c" : data = "\033[36;"
    elif str(data) == "d" : data = "\033[96;"
    elif str(data) == "e" : data = "\033[32;"
    elif str(data) == "f" : data = "\033[92;"
    elif str(data) == "\\": data = "\n"
    else:                   data = ""

    return data

def bg_colour(data) -> str:
    if   str(data) == "0": data = "40"
    elif str(data) == "1": data = "100"
    elif str(data) == "2": data = "47"
    elif str(data) == "3": data = "107"
    elif str(data) == "4": data = "43"
    elif str(data) == "5": data = "103"
    elif str(data) == "6": data = "41"
    elif str(data) == "7": data = "101"
    elif str(data) == "8": data = "45"
    elif str(data) == "9": data = "105"
    elif str(data) == "a": data = "44"
    elif str(data) == "b": data = "104"
    elif str(data) == "c": data = "46"
    elif str(data) == "d": data = "106"
    elif str(data) == "e": data = "42"
    elif str(data) == "f": data = "102"

    return data

def remage_old(file):
    with open('images/' + str(file) + '.remage') as f: data = f.read()[5:]

    image_data = ""
    for x in range(len(data)):
        if image_colour(data[x]) in ["\n", ""]: image_data += image_colour(data[x])
        else:                                   image_data += image_colour(data[x]) + "40m██\033[0m"
    
    if image_data[len(image_data)-1] in ["\n", "\\", "n"]:
        image_data = image_data[:-1]
    input(image_data)

def remage2x(file):
    with open('images/' + str(file) + '.remage') as f: data = f.read()[5:]

    image_data = ""; x = 0
    while x < len(data):
        if image_colour(data[x]) in ["\n", ""]: image_data += image_colour(data[x]); x += 1
        else: image_data += image_colour(data[x]) + bg_colour(data[x+1]) +"m▀\033[0m"; x += 2
    
    if image_data[len(image_data)-1] in ["\n", "\\", "n"]:
        image_data = image_data[:-1]
    input(image_data)

def remage256(file):
    with open('images/' + str(file) + '.remage') as f: data = f.read()[5:]
    
    image_data = ""; x = 0
    while x+1 < len(data):
        try:
            if   str(data[x]) == ":" : x += 10; image_data += "\033[38;2;" + str(data[x+1]) + str(data[x+2]) + str(data[x+3]) + ";" + str(data[x+4]) + str(data[x+5]) + str(data[x+6]) + ";" + str(data[x+7]) + str(data[x+8]) + str(data[x+9]) + "m██\033[0m"
            elif str(data[x]) == "\\": x += 1;  image_data = image_data[:-10] + "\n"; image_data = image_data[:-1]
            else:                      x += 1
        except:
            pass

    if image_data[len(image_data)-1] in ["\n", "\\", "n"]:
        image_data = image_data[:-1]
    input(image_data)

def remage2x256(file):
    with open('images/' + str(file) + '.remage') as f:
        file_data = f.readlines()
        key = file_data[0][5:-1]
        key = key.replace("{", "").replace("}", "")
        vals = key.split(", ")
        key_data = {}
        for val in vals:
            x = val.replace("'", "").split(": ")
            key_data[x[1]] = x[0]
        data = file_data[1:]
        data = "".join(data)
    
    key = []
    hexy = ["0", "1", "2", "3", "4", "5", "6", "7", "9", "a", "b", "c", "d", "e", "f"]

    for item in key_data:
        key.append(item) 
    
    image_data = ""
    x = 0
    while x < len(data):
        try:
            if data[x] == ":":
                x += 1
                if data[x] in key:
                    image_data += "\033[38;2;" + str(int("0x" + str(key_data[data[x]][:-4]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][2:-2]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][4:]), base=16)) + ";48;2;"
                    x += 1
                else:
                    image_data += "\033[38;2;" + str(int("0x" + str(data[x] + data[x+1]), base=16)) + ";" + str(int("0x" + str(data[x+2] + data[x+3]), base=16)) + ";" + str(int("0x" + str(data[x+4] + data[x+5]), base=16)) + ";48;2;"
                    x += 6
                x += 1
                if data[x] in key:
                    image_data += str(int("0x" + str(key_data[data[x]][:-4]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][2:-2]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][4:]), base=16))
                    x += 1
                else:
                    image_data += str(int("0x" + str(data[x] + data[x+1]), base=16)) + ";" + str(int("0x" + str(data[x+2] + data[x+3]), base=16)) + ";" + str(int("0x" + str(data[x+4] + data[x+5]), base=16))
                    x += 6
                image_data += "m▀\033[0m"
            elif data[x] == "\\": x += 1;  image_data += "\n"
            else: x += 1
        except:
            x += 1

    if image_data[len(image_data)-1] in ["\n", "\\", "n"]:
        image_data = image_data[:-1]
    input(image_data)

def remani2x256(file):
    with open('images/' + str(file) + '.remage') as f: data = f.read()[5:]

    os.system('cls' if os.name == 'nt' else 'clear')
    
    image_data = ""; x = 0
    for v in range(50):
        image_data = ""; x = 0
        while x < len(data):
            try:
                if data[x] == ":":
                    if data[x+1] == "W":
                        n = 1
                        image_data += "\033[38;2;255;255;255;48;2;"
                    elif data[x+1] == "B":
                        image_data += "\033[38;2;0;0;0;48;2;"
                        x += 1
                    else:
                        image_data += "\033[38;2;" + str(int(str(data[x+1] + data[x+2]), base=16)) + ";" + str(int("0x" + str(data[x+3] + data[x+4]), base=16)) + ";" + str(int("0x" + str(data[x+5] + data[x+6]), base=16)) + ";48;2;"
                        x += 6
                    if data[x+1] == "W":
                        image_data += "255;255;255"
                        x += 1
                    elif data[x+1] == "B":
                        image_data += "0;0;0"
                        x += 1
                    else:
                        image_data += str(int("0x" + str(data[x+1] + data[x+2]), base=16)) + ";" + str(int("0x" + str(data[x+3] + data[x+4]), base=16)) + ";" + str(int("0x" + str(data[x+5] + data[x+6]), base=16))
                        x += 6
                    image_data += "m▀\033[0m"
                elif data[x] == "\\": x += 1; image_data += "\n"
                elif data[x] == "@":
                    x += 1
                    if image_data[len(image_data)-1] in ["\n", "\\", "n"]:
                        image_data = image_data[:-1]
                    print(image_data, end="")
                    for v in range(126): print("\033[A\033[A")
                    image_data = ""
                else: x += 1
            except:
                pass

    os.system('cls' if os.name == 'nt' else 'clear')

def remage(file: str) -> None:

        """
        remage()
        
        Displays an image in the python termainal in the .remage format from the 'images' folder.\n
        The image must have a header depending on the formatting: 'R.OLD', '2xOLD', 'R.256' or '2x256'.
        """
        try:
            with open('images/' + str(file) + '.remage') as f: data = f.read()
        except:
            print(colour(1, 31, 40, "[ERROR]") + " Image " + colour(0, 30, 41, str(file) + ".remage") + " does not exist or is corrupted.")
            return
        if   data.startswith("R.OLD"): remage_old(file)
        elif data.startswith("2xOLD"): remage2x(file)
        elif data.startswith("R.256"): remage256(file)
        elif data.startswith("2x256"): remage2x256(file)
        elif data.startswith("256AN"): remani2x256(file)
        else:
            print(colour(1, 31, 40, "[ERROR]") + " Image " + str(file) + ".remage does not have a header or has an invalid header.")
            print(colour(1, 36, 40, "[DEBUG]") + " Please set the header to 'R.OLD', '2xOLD', 'R.256' or '2x256', depending on the format.")
        return