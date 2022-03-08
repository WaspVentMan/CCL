# Jacob A. G. Taylor, https://github.com/WaspVentMan, 2022

from functions.colour import *
from functions.date_time import date_time
from functions.faux_random import randint
from commands.rem import remage

def help(module: str) -> None:
    """
    help()

    Gives help on some of the things [I](https://github.com/WaspVentMan) have made.
    """
    module = module.lower()

    print("="*40 + "[Help]" + "="*40)

    if module == "":
        print("help [thing] - This will give you help on anything you put after the help command.\nReplace thing with something like \"colour\" or \"remage\"")
        print("\nAll commands (that have documentation):")
        print("ACE\nColour\nClear\nDate_Time\nExit\nFaux_Random\nRemage")

    elif module == "colour":
        print("import: \033[1;35;40mfrom \033[1;33;40mfunctions.colour \033[1;35;40mimport \033[1;34;40mcolour\033[0m")
        print("Colour values:\nText: (style/colour)")
        print("\033[1;30;40m Dark Gray      \033[0m 1/30    \033[0;30;47m Black      \033[0m 0/30")
        print("\033[1;31;40m Bright Red     \033[0m 1/31    \033[0;31;40m Red        \033[0m 0/31")
        print("\033[1;32;40m Bright Green   \033[0m 1/32    \033[0;32;40m Green      \033[0m 0/32")
        print("\033[1;33;40m Yellow         \033[0m 1/33    \033[0;33;40m Brown      \033[0m 0/33")
        print("\033[1;34;40m Bright Blue    \033[0m 1/34    \033[0;34;40m Blue       \033[0m 0/34")
        print("\033[1;35;40m Bright Magenta \033[0m 1/35    \033[0;35;40m Magenta    \033[0m 0/35")
        print("\033[1;36;40m Bright Cyan    \033[0m 1/36    \033[0;36;40m Cyan       \033[0m 0/36")
        print("\033[1;37;40m White          \033[0m 1/37    \033[0;37;40m Light Grey \033[0m 0/37")
        print("\nBackgrounds:              Styles:")
        print("\033[1;37;40m 40 (black)  \033[0m             \033[0;37;40m 0 (no effect) \033[0m ")
        print("\033[1;37;41m 41 (red)    \033[0m             \033[1;37;40m 1 (bold)      \033[0m ")
        print("\033[1;37;42m 42 (green)  \033[0m             \033[3;37;40m 3 (italics)   \033[0m ")
        print("\033[1;37;43m 43 (yellow) \033[0m             \033[4;37;40m 4 (underline) \033[0m ")
        print("\033[1;37;44m 44 (blue)   \033[0m ")
        print("\033[1;37;45m 45 (purple) \033[0m             Pallette:")
        print("\033[1;37;46m 46 (cyan)   \033[0m              \033[1;30;40m█\033[1;31;40m█\033[1;32;40m█\033[1;33;40m█\033[1;34;40m█\033[1;35;40m█\033[1;36;40m█\033[1;37;40m█")
        print("\033[1;30;47m 47 (white)  \033[0m              \033[0;30;47m█\033[0;31;40m█\033[0;32;40m█\033[0;33;40m█\033[0;34;40m█\033[0;35;40m█\033[0;36;40m█\033[0;37;40m█\033[0m")
        print("Created by Jacob A.G. Taylor, 2022")
    
    elif module == "remage":
        remage("logo2x")
        print("import: \033[1;35;40mfrom \033[1;33;40mfunctions.rem \033[1;35;40mimport \033[1;34;40mremage\033[0m")
        print("The \"remage\" image format has 5 different modes (4 of which are functional) each has a header.")
        print("\nRemage Headers:")
        print("R.OLD: Basic remage format, \"0-f\" for colours \"\\\" for a new line. Max reccomended size: (119x63)\n")
        print("2xOLD: Double pixel density, \"0-f\" for colours \"\\\" for a new line. Max reccomended size: (238x126)\nIt is rendered in a way that means you need to lay out the data in a backwards N pattern (top pixel, bottom pixel, next row, repeat)\n")
        print("R.256: The same as R.OLD, but allows for all colours to be used. Max reccomended size: (118x62)\nColours are represented like this: \":255255255\" (white), new lines are still \"\\\".\n")
        print("2x256: The same as 2xOLD, but allows for all colours to be used. Max reccomended size: (236x124)\nColours are represented like this: \":255255255\" (white), new lines are still \"\\\", it still uses the funny backwards N pattern.\n")
        print("256AN: Uses the same method of data as 2x256, however it adds the @ symbol which will signify a new frame as 256AN allows for animation.\n")
        print("Remage and Remage2x Colour pallettes:")
        remage("pallette")
        print("0 1 2 3 4 5 6 7 8 9 a b c d e f")
        print("\nRemage256 and Remage2x256 Colour pallettes:")
        print("The Remage256 and Remage2x256 formats use base 10 hexadecimal values for colour allowing for more colours per image.\nFor example: black would be :000000000, white would be :255255255, etc.\nThere are 16,777,216 usable colours. That is way better than 16.")
        print("\nMax size assumes that you are using a 1920x1080 monitor and have the terminal full screened with a font size of 16.")
        print("Created by Jacob A.G. Taylor, 2022")

    elif module == "ace":
        print("A.C.E. (Arbitrary Code Execution). Execute one line python code in the terminal.\nYou could probably do some pretty cool stuff in this.")

    elif module == "exit":
        print("It exits the command line. (why do you need help with this???)")
    
    elif module == "faux_random":
        print("import: \033[1;35;40mfrom \033[1;33;40mfunctions.faux_random \033[1;35;40mimport \033[1;34;40mrandint\033[0m")
        print("Warning: Faux Random is very inefficient, bigger numbers (1,000,000+) take longer to\ngenerate than smaller numbers (0 - 999,999)")
        print("I'll probably explain how it works later...")
        print("Here is a random number, free of charge: " + str(randint(0, 999)))
    
    elif module == "clear":
        print("Clears the screen.")
    
    elif module == "date_time":
        print("Gives date and time information in the format:\nTime, Day of the Week, Day of the Month, Day Pronoun (st, nt, rd, th), Month, Year.\n" + str(date_time()))
        print("The day of the month and the year are integers.")
    
    else:
        print(colour(1, 31, 40, "[ERROR]") + " Unknown or undocumented command: " + colour(0, 30, 41, module))