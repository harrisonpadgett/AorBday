from calendar import monthrange
from datetime import date, datetime, timedelta
from pytz import timezone
import requests
import os



clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


response = input("Welcome! For a list of commands, enter 'help'. When you are done, enter 'done'. \n\nYour response: ")
response = response.lower()
response = response.split(" ")


while response[0] != 'done':

    # Function to check if a given date is an A or B day. Must be in m/d/y format.
    # This function also accounts for holidays
    def checkDay(givenDate):
        
        # {Day : Name of Event, 0 if event does not take up entire day, 1 if event takes up entire day}
        specialDays = {"1/21/2022" : ["Second Marking Period Ends - Half Day", 0] , "2/07/2022" : ["Second Marking Period Report Cards Distributed", 0], "2/21/2022" : ["Presidents' Day, Washington's Birthday - No School", 1],  "3/25/2022" : ["Maryland Day", 0],  "4/01/2022" : ["Third Marking Period Ends - Half Day", 0],  "4/09/2022" : ["Spring Break - No School", 1],  "4/10/2022" : ["Spring Break - No School", 1],  "4/11/2022" : ["Spring Break - No School", 1],  "4/12/2022" : ["Spring Break - No School", 1],  "4/13/2022" : ["Spring Break - No School", 1],  "4/14/2022" : ["Spring Break - No School", 1],  "4/15/2022" : ["Spring Break - No School", 1],  "4/16/2022" : ["Spring Break - No School", 1],  "4/17/2022" : ["Spring Break - No School", 1],  "4/18/2022" : ["State Mandated Holiday - No School", 1],  "4/25/2022" : ["Report Cards Distributed", 0],  "5/03/2022" : ["Professional Development Day - No School", 1],  "5/20/2022" : ["Last Day for Seniors", 0],  "5/30/2022" : ["Memorial Day - No School", 1],  "6/15/2022" : ["Assessment Day - Half Day", 0],  "6/16/2022" : ["Assessment Day - Half Day", 0]}
        
        # Numbers correlate to the day and month of the appropriate specialDays key
        specialDaysNumbers = [121, 207, 221, 325, 401, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 425, 503, 520, 530, 615, 616]


        tz = timezone('EST')
        rn = datetime.now(tz)
        today = str(rn.strftime("%m/%d/%Y"))


        dayAdjust = 0

        startDayFull = ['1', '20', '2022'] # Testing date, is an A day

        startMonth = startDayFull[0]
        startDay = startDayFull[1]
        startYear = startDayFull[2]



        parsedToday = givenDate.split('/')

        month = parsedToday[0]
        day = parsedToday[1]
        year = parsedToday[2]


        currentDayCheckNumber = str(month) + str(day)
        currentDayCheckNumber = int(currentDayCheckNumber)


        numDaysInCurrentMonth = monthrange(2019, int(startMonth))[1]

        daysDifference = int(day) - int(startDay)



        if int(month) != int(startMonth):

            dayAdjust = int(month) - int(startMonth)
            dayAdjust = abs(dayAdjust)
            dayAdjust = dayAdjust * numDaysInCurrentMonth


        for index, key in enumerate(specialDays):


            if currentDayCheckNumber >= specialDaysNumbers[index]:

                #print(str(key) + " has occured. Subtracting appropriate amount from total days.")
                dayAdjust = dayAdjust - specialDays[key][1]
                #print("Value of dayAdjust after subtracting: " + str(dayAdjust))
                #print("")



        daysDifference = daysDifference + dayAdjust

        #aDay = "{} is an A day.".format(givenDate)
        #bDay = "{} is a B day.".format(givenDate)

        aDay = " is an A day."
        bDay = " is a B day."

        if (daysDifference % 2) == 0:
            return(aDay)
        else:
            return(bDay)



    if response[0] == 'help':

        clearConsole()
        response = input("Commands: \n\n'today' : returns if today is an A day or B day \n'tomorrow' : returns if tomorrow is an A day or B day \n'day m/d/y' : returns if specified date is an A day or B day \n'restart' : restart to the starting message \n\nYour response: ")
        response = response.lower()
        response = response.split(" ")


    if response[0] == 'restart':

        clearConsole()
        response = input("Welcome! For a list of commands, enter 'help'. When you are done, enter 'done'. \n\nYour response: ")
        response = response.lower()
        response = response.split(" ")



    if response[0] == 'today':

        clearConsole()
        tz = timezone('EST')
        today = datetime.now(tz)
        today = str(today.strftime("%m/%d/%Y"))
        result = checkDay(today)

        response = input("Today (" + str(today) + ")" + result + "\n\nYour response: ")
        response = response.lower()
        response = response.split(" ")

    if response[0] == 'tomorrow':

        clearConsole()
        tz = timezone('EST')
        today = datetime.now(tz)
        tomorrow = today + timedelta(days = 1)
        tomorrow = str(tomorrow.strftime("%m/%d/%Y"))
        
        result = checkDay(tomorrow)

        response = input("Tomorrow (" + str(tomorrow) + ")" + result + "\n\nYour response: ")
        response = response.lower()
        response = response.split(" ")
 
    if response[0] == 'day':

        clearConsole()
                
        result = checkDay(response[1])

        response = input("The date " + str(response[1]) + result + "\n\nYour response: ")
        response = response.lower()
        response = response.split(" ")


clearConsole()





