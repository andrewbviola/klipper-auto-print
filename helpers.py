import requests
import calendar
import variables
import random
import time
from datetime import date


def whatTime(current_day):
    match current_day:
        case "Monday":
            return variables.Monday

        case "Tuesday":
            return variables.Tuesday

        case "Wednesday":
            return variables.Wednesday

        case "Thursday":
            return variables.Thursday

        case "Friday":
            return variables.Friday

        case "Saturday":
            return variables.Saturday

        case "Sunday":
            return variables.Sunday

    return 0


def whatDay():
    d = date.today()
    current_day = calendar.day_name[d.weekday()]
    return current_day


def time2min(current):
    if current == 0:
        return 0
    time = current.split(":")
    minutes = 0
    if len(time) == 3:
        minutes = minutes + int(time[0]) * 60
        minutes = minutes + int(time[1])
        minutes = minutes + int(time[2]) / 60
    elif len(time) == 2:
        minutes = minutes + int(time[0]) * 60
        minutes = minutes + int(time[1])
    elif len(time) == 1:
        minutes = minutes + int(time[0]) * 60

    return minutes


def nextDay():
    current_day = whatDay()
    match current_day:
        case "Monday":
            return "Tuesday"
        case "Tuesday":
            return "Wednesday"
        case "Wednesday":
            return "Thursday"
        case "Thursday":
            return "Friday"
        case "Friday":
            return "Saturday"
        case "Saturday":
            return "Sunday"
        case "Sunday":
            return "Monday"
    return 0


def gcodeInfo():

    rawdata = requests.get(variables.grabGcode)
    printscall = rawdata.json()
    printerInfo = {
        "gcode": printscall['result'],
        "length": len(printscall['result'])
    }

    return printerInfo


def printIterated():

    gcodes = gcodeInfo()
    printGcode = "{}printer/print/start?filename={}".format(
        variables.URL, gcodes["gcode"][variables.startingIndex]['path'])
    requests.post(printGcode)
    variables.startingIndex = (variables.startingIndex + 1) % gcodes["length"]


def printMemory():
    gcodes = gcodeInfo()
    randomIndex = random.randint(0, gcodes["length"]-1)
    if randomIndex == variables.previousIndex:
        randomIndex = (randomIndex + 1) % (gcodes["length"])
    printGcode = "{}printer/print/start?filename={}".format(
        variables.URL, gcodes["gcode"][randomIndex]['path'])
    requests.post(printGcode)
    variables.previousIndex = randomIndex


def printRandom():
    gcodes = gcodeInfo()
    randomIndex = random.randint(0, gcodes["length"]-1)
    printGcode = "{}printer/print/start?filename={}".format(
        variables.URL, gcodes["gcode"][randomIndex]['path'])
    requests.post(printGcode)


def choosePrintType():
    if variables.iteratedListPrint == True:
        printIterated()
        return
    elif variables.memoryPrint == True:
        printMemory()
        return
    elif variables.trueRandom == True:
        printRandom()
        return
    return


def searchForDay():
    current_day = whatDay()
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    index = days.index(current_day)
    nextDayFound = True
    count = 0

    x = time.localtime()
    current_time = time.strftime("%H:%M", x)
    current_day = whatTime(whatDay())

    if time2min(current_time) > time2min(current_day):
        index = index + 1

    while nextDayFound:
        check = whatTime(days[index])
        if check != "0":
            nextDayFound = False
            return days[index]
        else:
            index = (index + 1) % 7
            count = count + 1
        if count == 6:
            nextDayFound = False
    return

def calculateSleep(today, scheduledDay):
    x = time.localtime()
    current_time = time.strftime("%H:%M", x)
    current_minutes = time2min(current_time)
    scheduled_time = time2min(whatTime(today))
    if scheduledDay == None:
        sleep = ((7 * 1440)-current_minutes) + scheduled_time
    else: 
        scheduled_time = time2min(whatTime(scheduledDay))
        days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
        num1 = days.index(today)
        num2 = days.index(scheduledDay)
        sleepFound = True
        count = 0

        while sleepFound:
            if days[num2] == days[num1]:
                sleepFound = False
            else:
                num1 = (num1 + 1) % 7
                count = count + 1
            difference = count

        if difference == 0:
            sleep = scheduled_time - current_minutes
        else:
            sleep = ((difference * 1440)-current_minutes) + scheduled_time

    return sleep

def checkSchedule():
    if variables.Monday== "1" or variables.Tuesday== "1" or variables.Wednesday== "1" or variables.Thursday== "1" or variables.Friday== "1" or variables.Saturday == "1" or variables.Sunday == "1":
        print("Set up your schedule in variables.py")
        return True
    return False