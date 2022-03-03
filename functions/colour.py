# Jacob A. G. Taylor, 2022

def colour(style: int, text_colour: int, bg_colour: int, text: str) -> str:
    """
    colour()

    Colours text, pretty simple.\n
    Style can only be between 1 - 9.\n
    Text colour can only be between 30 - 37 and 90 - 97.\n
    BG colour can only be between 40 - 47 or 100 - 107.
    """
    try:
        style = int(style)
    except:
        print(colour(1, 31, 40, "[ERROR]") + " Style is an invalid value, setting to default value: 0")
        style = 0
    
    try:
        text_colour = int(text_colour)
    except:
        print(colour(1, 31, 40, "[ERROR]") + " Text colour is an invalid value, setting to default value: 37")
        text_colour = 37

    try:
        bg_colour = int(bg_colour)
    except:
        print(colour(1, 31, 40, "[ERROR]") + " Background colour is an invalid value, setting to default value: 40")
        bg_colour = 40

    if style < 0 or style > 9:
        print(colour(1, 31, 40, "[ERROR]") + " Style out of range, setting to default value: 0")
        style = 0
    
    if text_colour < 30 or text_colour > 37 and text_colour < 90 or text_colour > 97:
        print(colour(1, 31, 40, "[ERROR]") + " Text colour out of range, setting to default value: 37")
        text_colour = 37
    
    if bg_colour < 40 or bg_colour > 47 and bg_colour < 100 or bg_colour > 107:
        print(colour(1, 31, 40, "[ERROR]") + " Background colour out of range, setting to default value: 40")
        bg_colour = 40
    
    coloured = "\033[" + str(style) + ";" + str(text_colour) + ";" + str(bg_colour) + "m" + str(text) + "\033[0m"
    return coloured

def colour_hex(r, g, b, text):
    if r < 0:
        print(colour(1, 31, 40, "[ERROR]") + " Colour " + colour_hex(255, 0, 0, "RED") + " cannot go below 0, now setting to 0.")
        r = 0

    if r > 255:
        print(colour(1, 31, 40, "[ERROR]") + " Colour " + colour_hex(255, 0, 0, "RED") + " cannot go above 255, now setting to 255.")
        r = 255
    
    if g < 0:
        print(colour(1, 31, 40, "[ERROR]") + " Colour " + colour_hex(0, 255, 0, "GREEN") + " cannot go below 0, now setting to 0.")
        g = 0

    if g > 255:
        print(colour(1, 31, 40, "[ERROR]") + " Colour " + colour_hex(0, 255, 0, "GREEN") + " cannot go above 255, now setting to 255.")
        g = 255
    
    if b < 0:
        print(colour(1, 31, 40, "[ERROR]") + " Colour " + colour_hex(0, 0, 255, "BLUE") + " cannot go below 0, now setting to 0.")
        b = 0

    if b > 255:
        print(colour(1, 31, 40, "[ERROR]") + " Colour " + colour_hex(0, 0, 255, "BLUE") + " cannot go above 255, now setting to 255.")
        b = 255

    coloured = "\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m" + str(text) + "\033[0m"
    return coloured