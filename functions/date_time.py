# Jacob A. G. Taylor, https://github.com/WaspVentMan, 2022

import os
from functions.maths import *

# WHy the fuck was the 1st january 1970 a fucking thursday?????

def date_time() -> list:

    """
    date_time()

    Get the current date and time information in the format:\n
    [Time, Day of the Week, Day of the Month, Day Pronoun (st, nt, rd, th), Month, Year]
    """

    time_list   = []
    month_no    = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    os.system("echo > r")
    fileStatsObj = os.stat("r")
    os.remove("r")

    seconds = fileStatsObj[8]
    minutes = int(floor(seconds/60))
    hours   = int(floor(minutes/60)) 
    days    = int(floor(hours  /24))
    years   = int(floor(days   /365.25)) + 1970
        
    seconds = seconds - minutes*60
    minutes = minutes - hours*60
    hours   = hours   - days*24

    days_temp = days

    # Big bullshit \/
    # Ignore last comment, made code better :)

    while days_temp > 0:
        for y in range(4):
            if days_temp < 0: break
            for x in range(len(month_no)):
                if days_temp < 0:
                    month = x
                    break
                if x == 1 and y == 2: days_temp -= month_no[x] + 1
                else:                 days_temp -= month_no[x]
    
    month_day = month_no[month-1] + days_temp + 1
    month     = months_list[month-1]

    weekday = str((days + 4) / 7)

    if   ".14285714285" in weekday: weekday = "Mon"
    elif ".28571428571" in weekday: weekday = "Tue"
    elif ".42857142857" in weekday: weekday = "Wed"
    elif ".57142857142" in weekday: weekday = "Thu"
    elif ".71428571428" in weekday: weekday = "Fri"
    elif ".85714285714" in weekday: weekday = "Sat"
    else:                           weekday = "Sun"

    if len(str(hours))   == 1: hours   = "0" + str(hours)
    if len(str(minutes)) == 1: minutes = "0" + str(minutes)
    if len(str(seconds)) == 1: seconds = "0" + str(seconds)

    h_m_s = str(hours) + ":" + str(minutes) + ":" + str(seconds)

    if   month_day in [1, 21, 31]: day_pronoun = "st"
    elif month_day in [2, 22]:     day_pronoun = "nd"
    elif month_day in [3, 23]:     day_pronoun = "rd"
    else:                          day_pronoun = "th"

    time_list.append(h_m_s)
    time_list.append(weekday)
    time_list.append(month_day)
    time_list.append(day_pronoun)
    time_list.append(month)
    time_list.append(years)

    return time_list