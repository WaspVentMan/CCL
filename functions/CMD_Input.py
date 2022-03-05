# Jacob A. G. Taylor, 2022

from functions.colour import *
from functions.ace import ace
from commands.help import help
from commands.rem import remage
import os

def CMD_Input(input):
    windows_cmd = ["ASSOC", "ATTRIB", "BREAK", "BCDEDIT", "CACLS", "CALL", "CD", "CHCP", "CHDIR", "CHKDSK", "CHKNTFS", "CLS", "CMD", "COLOR", "COMP", "COMPACT", "CONVERT", "COPY", "DATE", "DEL", "DIR", "DISKPART", "DOSKEY", "DRIVERQUERY", "ECHO", "ENDLOCAL", "ERASE", "EXIT", "FC", "FIND", "FINDSTR", "FOR", "FORMAT", "FSUTIL", "FTYPE", "GOTO", "GPRESULT", "GRAFTABL", "HELP", "ICACLS", "IF", "LABEL", "MD", "MKDIR", "MKLINK", "MODE", "MORE", "MOVE", "OPENFILES", "PATH", "PAUSE", "POPD", "PRINT", "PROMPT", "PUSHD", "RD", "RECOVER", "REM", "REN", "RENAME", "REPLACE", "RMDIR", "ROBOCOPY", "SET", "SETLOCAL", "SC", "SCHTASKS", "SHIFT", "SHUTDOWN", "SORT", "START", "SUBST", "SYSTEMINFO", "TASKLIST", "TASKKILL", "TIME", "TITLE", "TREE", "TYPE", "VER", "VERIFY", "VOL", "XCOPY", "WMIC"]
    
    try:
        if input.startswith("help"):
            input = input.split(" ")
            if len(input) == 1:
                input.append("")
            help(input[1])
        
        elif input.startswith("exit"):
            return True

        elif input.startswith("clear"):
            print(colour(1, 36, 40, "[DEBUG]") + " Clearing screen.")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif input.startswith("remage"):
            if len(input.split(" ")) != 2:
                remage()
            else:
                remage(input.split(" ")[1])

        elif input.startswith("ace"):
            ace(input)

        elif input.split()[0].upper() in windows_cmd:
            os.system(input)
            
        else:
            print(colour(1, 31, 40, "[ERROR]") + " Unknown command " + colour(0, 30, 41, input.split()[0]))

    except Exception as e:
        print(e)
        print(colour(1, 31, 40, "[ERROR]") + " An error occured.")