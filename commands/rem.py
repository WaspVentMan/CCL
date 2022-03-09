# Jacob A. G. Taylor, https://github.com/WaspVentMan, 2022

import os
from functions.colour import colour

def image_colour(data) -> str:
    colour_dict = {
        "0": "\033[30;", "1": "\033[90;", "2": "\033[37;", "3": "\033[97;", "4": "\033[33;", "5": "\033[93;",
        "6": "\033[31;", "7": "\033[91;", "8": "\033[35;", "9": "\033[95;", "a": "\033[34;", "b": "\033[34;",
        "c": "\033[36;", "d": "\033[96;", "e": "\033[32;", "f": "\033[92;", "\\": "\n"}

    if str(data) in colour_dict:
        return colour_dict[str(data)]
    else:
        return ""

def bg_colour(data) -> str:
    colour_dict = {
        "0": "40", "1": "100", "2": "47", "3": "107", 
        "4": "43", "5": "103", "6": "41", "7": "101",
        "8": "45", "9": "105", "a": "44", "b": "104",
        "c": "46", "d": "106", "e": "42", "f": "102"}

    return colour_dict[str(data)]

def remage_old(file):
    with open('images/' + str(file) + '.remage') as f: data = f.read()[5:]

    image_data = ""
    for x in range(len(data)):
        if image_colour(data[x]) in ["\n", ""]: image_data += image_colour(data[x])
        else:                                   image_data += image_colour(data[x]) + "40m██\033[0m"
    
    if image_data[len(image_data)-1] in ["\n", "\\", "n"]:
        image_data = image_data[:-1]
    print(image_data)

def remage2x(file):
    with open('images/' + str(file) + '.remage') as f: data = f.read()[5:]

    image_data = ""; x = 0
    while x < len(data):
        if image_colour(data[x]) in ["\n", ""]: image_data += image_colour(data[x]); x += 1
        else: image_data += image_colour(data[x]) + bg_colour(data[x+1]) +"m▀\033[0m"; x += 2
    
    if image_data[len(image_data)-1] in ["\n", "\\", "n"]:
        image_data = image_data[:-1]
    print(image_data)

def remage256(file):
    with open('images/' + str(file) + '.remage') as f: data = f.read()[5:]
    
    image_data = ""; x = 0
    while x+1 < len(data):
        try:
            if   str(data[x]) == ":" : x += 10; image_data += "\033[38;2;" + str(data[x+1]) + str(data[x+2]) + str(data[x+3]) + ";" + str(data[x+4]) + str(data[x+5]) + str(data[x+6]) + ";" + str(data[x+7]) + str(data[x+8]) + str(data[x+9]) + "m██\033[0m"
            elif str(data[x]) == "\\": x += 1;  image_data = image_data[:-10] + "\n"; image_data = image_data[:-1]
            else:                      x += 1
        except: pass

    if image_data[len(image_data)-1] in ["\n", "\\", "n"]: image_data = image_data[:-1]
    print(image_data)

def remage2x256(file):
    with open('images/' + str(file) + '.remage') as f:
        file_data = f.readlines()
        key = file_data[0][5:-1]
        key = key.replace("{", "").replace("}", "")
        vals = key.split(":")
        key_data = {}
        for val in vals:
            x = val.replace("'", "")
            key_data[x[6:]] = x[:6]
        data = file_data[1:]
        data = "".join(data)
    
    key = []
    hexy = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    num = {"!": 2, "#": 3, "$": 4, "%": 5, "&": 6, "(": 7, ")": 8, "*": 9}

    for item in key_data: key.append(item)

    count = 0
    
    image_data, x = "", 0
    while x < len(data):
        try:
            if data[x] in key or data[x] in hexy:
                if data[x] in key:
                    image_data += "\033[38;2;" + str(int("0x" + str(key_data[data[x]][:-4]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][2:-2]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][4:]), base=16)) + ";48;2;"
                    if data[x+1] in key or data[x+1] == "\\" or data[x+1] in hexy:
                        x += 1
                    else:
                        count += 1
                        if int(num[data[x+1]]) <= int(count):
                            count = -1
                            x += 2
                        else: pass
                else:
                    image_data += "\033[38;2;" + str(int("0x" + str(data[x] + data[x+1]), base=16)) + ";" + str(int("0x" + str(data[x+2] + data[x+3]), base=16)) + ";" + str(int("0x" + str(data[x+4] + data[x+5]), base=16)) + ";48;2;"
                    x += 6
                if data[x] in key:
                    image_data += str(int("0x" + str(key_data[data[x]][:-4]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][2:-2]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][4:]), base=16))
                    if data[x+1] in key or data[x+1] == "\\" or data[x+1] in hexy:
                        x += 1
                    else:
                        count += 1
                        if int(num[data[x+1]]) <= int(count):
                            count = -1
                            x += 2
                        else: pass
                else:
                    image_data += str(int("0x" + str(data[x] + data[x+1]), base=16)) + ";" + str(int("0x" + str(data[x+2] + data[x+3]), base=16)) + ";" + str(int("0x" + str(data[x+4] + data[x+5]), base=16))
                    x += 6
                image_data += "m▀\033[0m"
            elif data[x] == "\\": x += 1; print(image_data); image_data = ""
            else: x += 1
        except:
            x += 1

def remani2x256(file):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('images/' + str(file) + '.remage') as f:
        file_data = f.readlines()
        key = file_data[0][5:-1]
        key = key.replace("{", "").replace("}", "")
        vals = key.split(":")
        key_data = {}
        for val in vals:
            x = val.replace("'", "")
            key_data[x[6:]] = x[:6]
        data = file_data[1:]
        data = "".join(data)
    
    key = []
    hexy = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    num = {"!": 2, "#": 3, "$": 4, "%": 5, "&": 6, "(": 7, ")": 8, "*": 9}

    for item in key_data:
        key.append(item) 

    count = 0
    
    image_data = ""
    for f in range(20):
        x = 0
        while x < len(data):
            try:
                if data[x] in key or data[x] in hexy:
                    if data[x] in key:
                        image_data += "\033[38;2;" + str(int("0x" + str(key_data[data[x]][:-4]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][2:-2]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][4:]), base=16)) + ";48;2;"
                        if data[x+1] in key or data[x+1] == "\\" or data[x+1] in hexy:
                            x += 1
                        else:
                            count += 1
                            if int(num[data[x+1]]) <= int(count):
                                count = -1
                                x += 2
                            else: pass
                    else:
                        image_data += "\033[38;2;" + str(int("0x" + str(data[x] + data[x+1]), base=16)) + ";" + str(int("0x" + str(data[x+2] + data[x+3]), base=16)) + ";" + str(int("0x" + str(data[x+4] + data[x+5]), base=16)) + ";48;2;"
                        x += 6
                    if data[x] in key:
                        image_data += str(int("0x" + str(key_data[data[x]][:-4]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][2:-2]), base=16)) + ";" + str(int("0x" + str(key_data[data[x]][4:]), base=16))
                        if data[x+1] in key or data[x+1] == "\\" or data[x+1] in hexy:
                            x += 1
                        else:
                            count += 1
                            if int(num[data[x+1]]) <= int(count):
                                count = -1
                                x += 2
                            else: pass
                    else:
                        image_data += str(int("0x" + str(data[x] + data[x+1]), base=16)) + ";" + str(int("0x" + str(data[x+2] + data[x+3]), base=16)) + ";" + str(int("0x" + str(data[x+4] + data[x+5]), base=16))
                        x += 6
                    image_data += "m▀\033[0m"
                elif data[x] == "\\": x += 1;  image_data += "\n"
                elif data[x] == "@":
                    x += 1; print(image_data); image_data = ""
                    for b in range(250):
                        print("\033[A\033[A")
                else: x += 1
            except:
                x += 1

    os.system('cls' if os.name == 'nt' else 'clear')

def remage(file = "") -> None:
        """
        remage()
        
        Displays an image in the python termainal in the .remage format from the 'images' folder.\n
        The image must have a header depending on the formatting: 'R.OLD', '2xOLD', 'R.256', '2x256' or '256AN'.\n
        Leaving the field blank will list all files available to be used with Remage. (All files in the images folder.)
        """
        if file == "":
            print("")
            dir = os.listdir("images")
            for item in dir:
                with open('images/' + str(item)) as f: data = f.read()
                size = os.path.getsize('images/' + item)
                size_style = "B"
                if size >= 1024:
                    size = round(size/1024)
                    size_style = "KiB"
                    if size >= 1024:
                        size = round(size/1024)
                        size_style = "MiB"
                        if size >= 1024:
                            size = round(size/1024)
                            size_style = "GiB"

                print("Format: " + data[:5] + " | Size: " + str(size) + size_style + " "*(7-len(str(size))-len(size_style)) + " | Name: " + item[:-7])
            return

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