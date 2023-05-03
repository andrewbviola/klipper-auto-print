import requests, datetime, time, calendar, helpers, variables, random
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
    time = whatTime(current_day)
    match time:
        case variables.Monday:
            return "Monday"
        case variables.Tuesday:
            return "Tuesday"
        case variables.Wednesday:
            return "Wednesday"
        case variables.Thursday:
            return "Thursday"
        case variables.Friday:
            return "Friday"
        case variables.Saturday:
            return "Saturday"
        case variables.Sunday:
            return "Sunday"
    return 0


def time2min(current):
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
    printGcode = "{}printer/print/start?filename={}".format(variables.URL,gcodes["gcode"][variables.startingIndex]['path'])
    requests.post(printGcode)
    variables.startingIndex = (variables.startingIndex + 1) % gcodes["length"]

def printMemory():
    gcodes = gcodeInfo()
    randomIndex = random.randint(0, gcodes["length"]-1)
    if randomIndex == variables.previousIndex:
        randomIndex = (randomIndex + 1) % (gcodes["length"])
    printGcode = "{}printer/print/start?filename={}".format(variables.URL,gcodes["gcode"][randomIndex]['path'])
    requests.post(printGcode)
    variables.previousIndex = randomIndex

def printRandom():
    gcodes = gcodeInfo()
    randomIndex = random.randint(0, gcodes["length"]-1)
    printGcode = "{}printer/print/start?filename={}".format(variables.URL,gcodes["gcode"][randomIndex]['path'])
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


    

