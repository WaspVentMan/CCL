# Jacob A. G. Taylor, https://github.com/WaspVentMan, 2022

import os
from PIL import Image

from functions.maths import *

def R256_Convert(name):
    red_image = Image.open(name + ".png")
    red_image_rgb = red_image.convert("RGBA")
    size = red_image.size

    data = "R.256\n"

    for y in range(size[1]):
        for x in range(size[0]):
            r = str(red_image_rgb.getpixel((x,y))[0])
            g = str(red_image_rgb.getpixel((x,y))[1])
            b = str(red_image_rgb.getpixel((x,y))[2])
            a = str(red_image_rgb.getpixel((x,y))[3])
            if a != "255":
                r = "255"
                g = "255"
                b = "255"
            while len(r) < 3: r = "0" + r
            while len(g) < 3: g = "0" + g
            while len(b) < 3: b = "0" + b
            data += ":" + r + g + b
        data += "\\\n"
    a = open("images/" + name + ".remage", "w")
    a.write(data)
    return data

def x2256_Convert(name):
    try:
        red_image = Image.open(name + ".png")
    except:
        red_image = Image.open(name + ".jpg")
    
    red_image_rgb = red_image.convert("RGBA"); size = red_image.size; used_values = {}; x = size[0];  y = size[1]; x = x/238; y = y/126; data = ""; temp = {}; t = 0; to_delete = []

    if x > 1 or y > 1:
        if x > y: x = round(red_image_rgb.width/x); y = round(red_image_rgb.height/x)
        else:     x = round(red_image_rgb.width/y); y = round(red_image_rgb.height/y)
        red_image_rgb = red_image_rgb.resize((x,y)); size = red_image_rgb.size

    for y in range(floor(size[1]/2)):
        for x in range(size[0]):
            r = str(hex(red_image_rgb.getpixel((x,(y*2)))[0]))
            g = str(hex(red_image_rgb.getpixel((x,(y*2)))[1]))
            b = str(hex(red_image_rgb.getpixel((x,(y*2)))[2]))
            a = str(hex(red_image_rgb.getpixel((x,(y*2)))[3]))
            if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:    used_values[r[2:] + g[2:] + b[2:]] += 1
            except: used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
            r=str(hex(red_image_rgb.getpixel((x,(y*2)+1))[0]))
            g=str(hex(red_image_rgb.getpixel((x,(y*2)+1))[1]))
            b=str(hex(red_image_rgb.getpixel((x,(y*2)+1))[2]))
            a=str(hex(red_image_rgb.getpixel((x,(y*2)+1))[3]))
            if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:    used_values[r[2:] + g[2:] + b[2:]] += 1
            except: used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
        data += "\\"
        perc = round((y/floor(size[1]/2))*100)
        print("["+"#"*perc+"-"*int(100-perc)+"] 1/1",end="\r")
    print("[" + "#"*100 + "] 1/1",end="\r")

    for item in used_values:
        if used_values[item] > 1: temp[item] = used_values[item]
        
    used_values = temp
    sorted_dict = {}; sorted_keys = sorted(used_values, key=used_values.get, reverse=True)
    for w in sorted_keys: sorted_dict[w] = used_values[w]

    # Unusable in shorters: 0123456789abcdef:@"{}\!#$%&()*
    shorters = "+,-./;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`ghijklmnopqrstuvwxyz|~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

    for item in sorted_dict:
        if t + 1 > len(shorters): to_delete.append(item)
        else: sorted_dict[item] = shorters[t]; t += 1
    for item in to_delete: del sorted_dict[item]
    for item in sorted_dict: data = data.replace(item, sorted_dict[item])

    data = data.replace(":", "")

    n_data = ""

    x = 0
    y = 0
    t_data = ""
    num = "!#$%&()*"
    while x < len(data):
        if data[x] in shorters:
            n_data += data[x]
            count = 0
            for z in range(9):
                if data[x+z+1] == data[x]:
                    count += 1
                else:
                    break
            if count > 1:
                n_data += str(num[count-2])
                x += count + 1
            else:
                x += 1
        elif data[x] == "\\":
            n_data += "\\\n"
            x += 1
        else:
            n_data += data[x]
            x += 1
        y += 1
        if y == 100000:
            t_data += n_data
            n_data = ""
            y = 0
            perc = round(((x)/len(data))*100)
            print("["+"#"*perc+"-"*int(100-perc)+"] " + str(x) + "/" + str(len(data)),end="\r")
    print("["+"#"*100+"] " + str(x) + "/" + str(len(data)))
    t_data += n_data

    data = t_data

    sorted_dict = str(sorted_dict).replace("{", "").replace("}", "").replace("'", "").replace(": ", "").replace(", ", ":")

    data = "2x256" + str(sorted_dict) + "\n" + data
    a = open("images/" + name + ".remage", "w"); a.write(data)

def x2256_Convert_lossy(name):
    try:
        red_image = Image.open(name + ".png")
    except:
        red_image = Image.open(name + ".jpg")
    
    red_image_rgb = red_image.convert("RGBA"); size = red_image.size; used_values = {}; x = size[0];  y = size[1]; x = x/238; y = y/126; data = ""; temp = {}; t = 0; to_delete = []

    if x > 1 or y > 1:
        if x > y: x = round(red_image_rgb.width/x); y = round(red_image_rgb.height/x)
        else:     x = round(red_image_rgb.width/y); y = round(red_image_rgb.height/y)
        red_image_rgb = red_image_rgb.resize((x,y)); size = red_image_rgb.size

    for y in range(floor(size[1]/2)):
        for x in range(size[0]):
            r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[0]/5)*5))
            g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[1]/5)*5))
            b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[2]/5)*5))
            a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[3]/5)*5))
            if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:    used_values[r[2:] + g[2:] + b[2:]] += 1
            except: used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
            r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[0]/5)*5))
            g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[1]/5)*5))
            b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[2]/5)*5))
            a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[3]/5)*5))
            if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:    used_values[r[2:] + g[2:] + b[2:]] += 1
            except: used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
        data += "\\"
        perc = round((y/floor(size[1]/2))*100)
        print("["+"#"*perc+"-"*int(100-perc)+"] 1/1",end="\r")
    print("[" + "#"*100 + "] 1/1",end="\r")

    for item in used_values:
        if used_values[item] > 1: temp[item] = used_values[item]
        
    used_values = temp
    sorted_dict = {}; sorted_keys = sorted(used_values, key=used_values.get, reverse=True)
    for w in sorted_keys: sorted_dict[w] = used_values[w]

    # Unusable in shorters: 0123456789abcdef:@"{}\!#$%&()*
    shorters = "+,-./;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`ghijklmnopqrstuvwxyz|~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

    for item in sorted_dict:
        if t + 1 > len(shorters): to_delete.append(item)
        else: sorted_dict[item] = shorters[t]; t += 1
    for item in to_delete: del sorted_dict[item]
    for item in sorted_dict: data = data.replace(item, sorted_dict[item])

    data = data.replace(":", "")

    n_data = ""

    x = 0
    y = 0
    t_data = ""
    num = "!#$%&()*"
    while x < len(data):
        if data[x] in shorters:
            n_data += data[x]
            count = 0
            for z in range(9):
                if data[x+z+1] == data[x]:
                    count += 1
                else:
                    break
            if count > 1:
                n_data += str(num[count-2])
                x += count + 1
            else:
                x += 1
        elif data[x] == "\\":
            n_data += "\\\n"
            x += 1
        else:
            n_data += data[x]
            x += 1
        y += 1
        if y == 100000:
            t_data += n_data
            n_data = ""
            y = 0
            perc = round(((x)/len(data))*100)
            print("["+"#"*perc+"-"*int(100-perc)+"] " + str(x) + "/" + str(len(data)),end="\r")
    print("["+"#"*100+"] " + str(x) + "/" + str(len(data)))
    t_data += n_data

    data = t_data

    sorted_dict = str(sorted_dict).replace("{", "").replace("}", "").replace("'", "").replace(": ", "").replace(", ", ":")

    data = "2x256" + str(sorted_dict) + "\n" + data
    a = open("images/" + name + ".remage", "w"); a.write(data)

def x2256_anim_Convert(name):
    red_image = Image.open(name + ".gif"); red_image_rgb = red_image.convert("RGBA"); size = red_image.size; used_values = {}; xx = size[0];  yy = size[1]; xx = xx/238; yy = yy/126; data = ""; temp = {}; t = 0; to_delete = []

    if xx > 1 or yy > 1:
        if xx > yy: xx = round(red_image_rgb.width/xx); yy = round(red_image_rgb.height/xx)
        else:     xx = round(red_image_rgb.width/yy); yy = round(red_image_rgb.height/yy)
        red_image_rgb = red_image_rgb.resize((xx,yy)); size = red_image_rgb.size

    length = red_image.n_frames
    c = 1
    t_data = ""

    for frame in range(red_image.n_frames):
        red_image.seek(frame); red_image.save("frame.png"); _red_image = Image.open("frame.png"); red_image_rgb = _red_image.convert("RGBA")
        red_image_rgb = red_image_rgb.resize((size[0],size[1]))
        for y in range(floor(size[1]/2)):
            for x in range(size[0]):
                r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[0])))
                g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[1])))
                b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[2])))
                a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[3])))
                if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
                else:
                    while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                    while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                    while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
                try:    used_values[r[2:] + g[2:] + b[2:]] += 1
                except: used_values[r[2:] + g[2:] + b[2:]] = 1
                data += ":" + r[2:] + g[2:] + b[2:]
                r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[0])))
                g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[1])))
                b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[2])))
                a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[3])))
                if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
                else:
                    while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                    while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                    while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
                try:    used_values[r[2:] + g[2:] + b[2:]] += 1
                except: used_values[r[2:] + g[2:] + b[2:]] = 1
                data += ":" + r[2:] + g[2:] + b[2:]
            data += "\\"
            perc = round((y/floor(size[1]/2))*100)
            print("["+"#"*perc+"-"*int(100-perc)+"] " + str(c) + "/" + str(length),end="\r")
        print("[" + "#"*100 + "] " + str(c) + "/" + str(length), end="\r")
        c += 1
        data += "@\n"
        t_data += data
        data = ""
    data = t_data

    for item in used_values:
        if used_values[item] > 1: temp[item] = used_values[item]
        
    used_values = temp
    sorted_dict = {}; sorted_keys = sorted(used_values, key=used_values.get, reverse=True)
    for w in sorted_keys: sorted_dict[w] = used_values[w]

    # Unusable in shorters: 0123456789abcdef:@"{}\!#$%&()*
    shorters = "+,-./;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`ghijklmnopqrstuvwxyz|~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

    for item in sorted_dict:
        if t + 1 > len(shorters): to_delete.append(item)
        else: sorted_dict[item] = shorters[t]; t += 1
    for item in to_delete: del sorted_dict[item]
    for item in sorted_dict: data = data.replace(item, sorted_dict[item])

    data = data.replace(":", "")

    n_data = ""

    x = 0
    y = 0
    t_data = ""
    num = "!#$%&()*"
    while x < len(data):
        if data[x] in shorters:
            n_data += data[x]
            count = 0
            for z in range(9):
                if data[x+z+1] == data[x]:
                    count += 1
                else:
                    break
            if count > 1:
                n_data += str(num[count-2])
                x += count + 1
            else:
                x += 1
        elif data[x] == "\\":
            n_data += "\\\n"
            x += 1
        else:
            n_data += data[x]
            x += 1
        y += 1
        if y == 100000:
            t_data += n_data
            n_data = ""
            y = 0
            perc = round(((x)/len(data))*100)
            print("["+"#"*perc+"-"*int(100-perc)+"] " + str(x) + "/" + str(len(data)),end="\r")
    print("["+"#"*100+"] " + str(x) + "/" + str(len(data)))
    t_data += n_data

    data = t_data

    sorted_dict = str(sorted_dict).replace("{", "").replace("}", "").replace("'", "").replace(": ", "").replace(", ", ":")

    data = "256AN" + str(sorted_dict) + "\n" + data
    a = open("images/" + name + ".remage", "w"); a.write(data)

def x2256_anim_Convert_lossy(name):
    red_image = Image.open(name + ".gif"); red_image_rgb = red_image.convert("RGBA"); size = red_image.size; used_values = {}; xx = size[0];  yy = size[1]; xx = xx/238; yy = yy/126; data = ""; temp = {}; t = 0; to_delete = []

    if xx > 1 or yy > 1:
        if xx > yy: xx = round(red_image_rgb.width/xx); yy = round(red_image_rgb.height/xx)
        else:     xx = round(red_image_rgb.width/yy); yy = round(red_image_rgb.height/yy)
        red_image_rgb = red_image_rgb.resize((xx,yy)); size = red_image_rgb.size

    length = red_image.n_frames
    c = 1
    t_data = ""

    for frame in range(red_image.n_frames):
        red_image.seek(frame); red_image.save("frame.png"); _red_image = Image.open("frame.png"); red_image_rgb = _red_image.convert("RGBA")
        red_image_rgb = red_image_rgb.resize((size[0],size[1]))
        for y in range(floor(size[1]/2)):
            for x in range(size[0]):
                r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[0]/5)*5))
                g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[1]/5)*5))
                b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[2]/5)*5))
                a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[3]/5)*5))
                if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
                else:
                    while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                    while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                    while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
                try:    used_values[r[2:] + g[2:] + b[2:]] += 1
                except: used_values[r[2:] + g[2:] + b[2:]] = 1
                data += ":" + r[2:] + g[2:] + b[2:]
                r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[0]/5)*5))
                g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[1]/5)*5))
                b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[2]/5)*5))
                a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[3]/5)*5))
                if a != "0xff": r = "0xff"; g = "0xff"; b = "0xff"
                else:
                    while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                    while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                    while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
                try:    used_values[r[2:] + g[2:] + b[2:]] += 1
                except: used_values[r[2:] + g[2:] + b[2:]] = 1
                data += ":" + r[2:] + g[2:] + b[2:]
            data += "\\"
            perc = floor((y/floor(size[1]/2))*100)
            print("["+"#"*perc+"-"*int(100-perc)+"] " + str(c) + "/" + str(length),end="\r")
        print("[" + "#"*100 + "] " + str(c) + "/" + str(length), end="\r")
        c += 1
        data += "@\n"
        t_data += data
        data = ""
    data = t_data
    print("")

    for item in used_values:
        if used_values[item] > 1: temp[item] = used_values[item]
        
    used_values = temp
    sorted_dict = {}; sorted_keys = sorted(used_values, key=used_values.get, reverse=True)
    for w in sorted_keys: sorted_dict[w] = used_values[w]

    # Unusable in shorters: 0123456789abcdef:@"{}\!#$%&()*
    shorters = "+,-./;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`ghijklmnopqrstuvwxyz|~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

    for item in sorted_dict:
        if t + 1 > len(shorters): to_delete.append(item)
        else: sorted_dict[item] = shorters[t]; t += 1
    for item in to_delete: del sorted_dict[item]
    for item in sorted_dict: data = data.replace(item, sorted_dict[item])

    data = data.replace(":", "")

    n_data = ""

    x = 0
    y = 0
    t_data = ""
    num = "!#$%&()*"
    while x < len(data):
        if data[x] in shorters:
            n_data += data[x]
            count = 0
            for z in range(9):
                if data[x+z+1] == data[x]:
                    count += 1
                else:
                    break
            if count > 1:
                n_data += str(num[count-2])
                x += count + 1
            else:
                x += 1
        elif data[x] == "\\":
            n_data += "\\\n"
            x += 1
        else:
            n_data += data[x]
            x += 1
        y += 1
        if y == 100000:
            t_data += n_data
            n_data = ""
            y = 0
            perc = round(((x)/len(data))*100)
            print("["+"#"*perc+"-"*int(100-perc)+"] " + str(x) + "/" + str(len(data)),end="\r")
    print("["+"#"*100+"] " + str(x) + "/" + str(len(data)))
    t_data += n_data

    data = t_data

    sorted_dict = str(sorted_dict).replace("{", "").replace("}", "").replace("'", "").replace(": ", "").replace(", ", ":")

    data = "256AN" + str(sorted_dict) + "\n" + data
    a = open("images/" + name + ".remage", "w"); a.write(data)

while True:
    mode = ""
    while mode not in ["A", "S"]:
        image = input("Input the .png, .jpg or .gif name. (Without file extension)\nor type \"all\" to convert all images in the root directory\n>>> ")
        dir = os.listdir()
        if image == "frame":
            print("Invalid image.")

        elif image.startswith("all"):
            args = image.split(" ")
            del args[0]
            while mode not in ["-", "+"]:
                mode = input("Lossy (-) or Lossless (+)?\n>>> ")
            for item in dir:
                if "-" + item[:-4] in args:
                    print("Image " + item + " skipped due to filters.")
                elif "-" + item[-3:] in args:
                    print("Image " + item + " skipped due to filters.")
                elif item[:-4] == "frame":
                    pass
                elif item[-3:] == "png":
                    if mode == "-": x2256_Convert_lossy(item[:-4])
                    else:           x2256_Convert(item[:-4])
                elif item[-3:] == "jpg":
                    if mode == "-": x2256_Convert_lossy(item[:-4])
                    else:           x2256_Convert(item[:-4])
                elif item[-3:] == "gif":
                    if mode == "-": x2256_anim_Convert_lossy(item[:-4])
                    else:           x2256_anim_Convert(item[:-4])
            exit()
        else:
            for item in dir:
                if image == item[:-4]:
                    if item[-3:] == "png":
                        mode = "S"
                    elif item[-3:] == "gif":
                        mode = "A"
                    else:
                        print("Invalid image.")
    
    if mode == "A":
        while mode not in ["-", "+"]:
            mode = input("Lossy (-) or Lossless (+)?\n>>> ")
        if mode == "-": x2256_anim_Convert_lossy(image)
        else:           x2256_anim_Convert(image)
    else:
        while mode not in ["-", "+"]:
            mode = input("Lossy (-) or Lossless (+)?\n>>> ")
        if mode == "-": x2256_Convert_lossy(image)
        else:           x2256_Convert(image)
    again = ""
    while again not in ["y", "n"]:
        again = input("Again? (y/n)\n>>> ")
    if again == "n":
        break