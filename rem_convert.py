from PIL import Image

from functions.maths import *
from commands.rem import remage

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
    red_image = Image.open(name + ".png")
    red_image_rgb = red_image.convert("RGBA")
    size = red_image.size

    used_values = {}

    x = size[0]
    y = size[1]

    x = x/238
    y = y/126

    if x > 1 or y > 1:
        confirm = ""
        while confirm not in ["y", "n"]:
            confirm = input("Image is larger than the max recommended size (238x126).\nKeeping it at this size will greatly increase load times.\nDo you want to auto compress the image? (y/n)\n>>> ")
        if confirm == "n":
            pass
        else:
            if x > y:
                x = round(red_image_rgb.width/x)
                y = round(red_image_rgb.height/x)
            else:
                x = round(red_image_rgb.width/y)
                y = round(red_image_rgb.height/y)
            red_image_rgb = red_image_rgb.resize((x,y))
            size = red_image_rgb.size

    data = ""

    for y in range(floor(size[1]/2)):
        for x in range(size[0]):
            r = str(hex(red_image_rgb.getpixel((x,(y*2)))[0]))
            g = str(hex(red_image_rgb.getpixel((x,(y*2)))[1]))
            b = str(hex(red_image_rgb.getpixel((x,(y*2)))[2]))
            a = str(hex(red_image_rgb.getpixel((x,(y*2)))[3]))
            if a != "0xff":
                r == "0xff"
                g == "0xff"
                b == "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:
                used_values[r[2:] + g[2:] + b[2:]] += 1
            except:
                used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
            r = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[0]))
            g = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[1]))
            b = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[2]))
            a = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[3]))
            if a != "0xff":
                r == "0xff"
                g == "0xff"
                b == "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:
                used_values[r[2:] + g[2:] + b[2:]] += 1
            except:
                used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
            
        data += "\\\n"
        perc = round((y/floor(size[1]/2))*100)
        print("[" + "#"*perc + "-"*int(100-perc) + "] " + str(perc) + "%", end="\r")
    print("[" + "#"*100 + "] 100%")

    temp = {}

    for item in used_values:
        if used_values[item] > 1:
            temp[item] = used_values[item]
        
    used_values = temp

    sorted_dict = {}
    sorted_keys = sorted(used_values, key=used_values.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = used_values[w]

    shorters = ["A", "B", "C", "D", "E", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
    
    x = 0
    to_delete = []
    for item in sorted_dict:
        if x + 1 > len(shorters):
            to_delete.append(item)
        else:
            sorted_dict[item] = shorters[x]
            x += 1
        
    for item in to_delete:
        del sorted_dict[item]

    for item in sorted_dict:
        data = data.replace(item, sorted_dict[item])

    data = "2x256" + str(sorted_dict) + "\n" + data

    a = open("images/" + name + ".remage", "w")
    a.write(data)
    
    return data

def x2256_Convert_lossy(name):
    red_image = Image.open(name + ".png")
    red_image_rgb = red_image.convert("RGBA")
    size = red_image.size

    used_values = {}

    x = size[0]
    y = size[1]

    x = x/238
    y = y/126

    if x > 1 or y > 1:
        confirm = ""
        while confirm not in ["y", "n"]:
            confirm = input("Image is larger than the max recommended size (238x126).\nKeeping it at this size will greatly increase load times.\nDo you want to auto compress the image? (y/n)\n>>> ")
        if confirm == "n":
            pass
        else:
            if x > y:
                x = round(red_image_rgb.width/x)
                y = round(red_image_rgb.height/x)
            else:
                x = round(red_image_rgb.width/y)
                y = round(red_image_rgb.height/y)
            red_image_rgb = red_image_rgb.resize((x,y))
            size = red_image_rgb.size

    data = ""

    for y in range(floor(size[1]/2)):
        for x in range(size[0]):
            r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[0]/5)*5))
            g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[1]/5)*5))
            b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[2]/5)*5))
            a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)))[3]/5)*5))
            if a != "0xff":
                r == "0xff"
                g == "0xff"
                b == "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:
                used_values[r[2:] + g[2:] + b[2:]] += 1
            except:
                used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
            r = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[0]/5)*5))
            g = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[1]/5)*5))
            b = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[2]/5)*5))
            a = str(hex(floor(red_image_rgb.getpixel((x,(y*2)+1))[3]/5)*5))
            if a != "0xff":
                r == "0xff"
                g == "0xff"
                b == "0xff"
            else:
                while len(r[2:]) < 2: r = r[-2:] + "0" + r[2:]
                while len(g[2:]) < 2: g = g[-2:] + "0" + g[2:]
                while len(b[2:]) < 2: b = b[-2:] + "0" + b[2:]
            try:
                used_values[r[2:] + g[2:] + b[2:]] += 1
            except:
                used_values[r[2:] + g[2:] + b[2:]] = 1
            data += ":" + r[2:] + g[2:] + b[2:]
            
        data += "\\\n"
        perc = round((y/floor(size[1]/2))*100)
        print("[" + "#"*perc + "-"*int(100-perc) + "] " + str(perc) + "%", end="\r")
    print("[" + "#"*100 + "] 100%")

    temp = {}

    for item in used_values:
        if used_values[item] > 1:
            temp[item] = used_values[item]
        
    used_values = temp

    sorted_dict = {}
    sorted_keys = sorted(used_values, key=used_values.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = used_values[w]

    shorters = ["A", "B", "C", "D", "E", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
    
    x = 0
    to_delete = []
    for item in sorted_dict:
        if x + 1 > len(shorters):
            to_delete.append(item)
        else:
            sorted_dict[item] = shorters[x]
            x += 1
        
    for item in to_delete:
        del sorted_dict[item]

    for item in sorted_dict:
        data = data.replace(item, sorted_dict[item])

    data = "2x256" + str(sorted_dict) + "\n" + data

    a = open("images/" + name + ".remage", "w")
    a.write(data)
    
    return data

# BROKEN!!!!
def x2256_anim_Convert(name):
    red_image = Image.open(name + ".gif")
    red_image_rgb = red_image.convert("RGBA")
    size = red_image.size

    data = "256AN\n"

    for frame in range(red_image.n_frames):
        red_image.seek(frame)
        red_image.save("frame.png")
        _red_image = Image.open("frame.png")
        red_image_rgb = _red_image.convert("RGBA")
        for y in range(floor(size[1]/2)):
            for x in range(size[0]):
                r = str(hex(red_image_rgb.getpixel((x,(y*2)))[0]))
                g = str(hex(red_image_rgb.getpixel((x,(y*2)))[1]))
                b = str(hex(red_image_rgb.getpixel((x,(y*2)))[2]))
                a = str(hex(red_image_rgb.getpixel((x,(y*2)))[3]))
                if a != "0xff":
                    r = "ff"
                    g = "ff"
                    b = "ff"
                while len(r[2:]) < 2: r = "0" + r
                while len(g[2:]) < 2: g = "0" + g
                while len(b[2:]) < 2: b = "0" + b
                data += ":" + r[2:] + g[2:] + b[2:]
                r = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[0]))
                g = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[1]))
                b = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[2]))
                a = str(hex(red_image_rgb.getpixel((x,(y*2)+1))[3]))
                if a != "0xff":
                    r = "ff"
                    g = "ff"
                    b = "ff"
                while len(r[2:]) < 2: r = "0" + r
                while len(g[2:]) < 2: g = "0" + g
                while len(b[2:]) < 2: b = "0" + b
                data += ":" + r[2:] + g[2:] + b[2:]
            data += "\\\n"
        data += "@\n"
    a = open("images/" + name + ".remage", "w")
    a.write(data)
    return data

while True:
    image = input("Input the image name\n>>> ")
    mode = ""
    while mode not in ["-", "+"]:
        mode = input("Lossy (-) or Lossless (+)?\n>>> ")
    if mode == "-": x2256_Convert_lossy(image)
    else:           x2256_Convert(image)
    again = ""
    while again not in ["y", "n"]:
        again = input("Again? (y/n)\n>>> ")
    if again == "n":
        break