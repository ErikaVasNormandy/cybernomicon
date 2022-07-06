import sys
import calendar
import datetime
import time
import re
import csv

current_year = datetime.datetime.now().year
calendar.setfirstweekday(calendar.SUNDAY)


#Print Out Menu Options
#a) View calendar
#b) Get next anticipated date
#c) Add in new entry
#d) Modify Entry
#e) Delete Entry
LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

channelDirectory = {
    1: "View Calendar",
    2: "Guestimate Next Date",
    3: "Add New Entry",
    4: "Modify"
}

monthDictionary = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


def justLoadUpCalendars():
#    print("LocalTimezone_ ", LOCAL_TIMEZONE)
    yy = 2022
    mm = 7
    dd = 3
    print("datetime.timezone:::", datetime.timezone)
    print(calendar.calendar(current_year))
    return 0;
    

def displayCurrentDate(listInput):
    today = datetime.date.today()
    year  = today.year
    month = today.month
    ###this is where things get executed
    thism = calendar.month(year,month)    # current month
    date  = today.day.__str__().rjust(2)
    rday  = ('\\b' + date + '\\b').replace('\\b ', '\\s')
    rdayc = "\033[7m" + date + "\033[0m"
    print( re.sub(rday,rdayc,thism))
    
def displayCalendar(arrayInput):
    placeholderfirstdate = ''
    placeholderseconddate = ''
    placeholdernotes = ""
    
    # 1. Loop through our array input of CSV columns
    for i in arrayInput:
    
    # 2. Get the start and the end dates respectively, splitting them in order to get an array of year, month, date
        placeholderfirstdate = i[0].split("-")
        placeholderseconddate = i[1].split("-")
        
    # 3. Start working on the start date mainly reformatting it to have the highlight effect
        placeholderfirstdateMONTH = placeholderfirstdate[1]
        placeholderfirstdateDAY = placeholderfirstdate[2].__str__().rjust(2)
        if(placeholderfirstdateDAY[0] == "0"):
            placeholderfirstdateDAY = placeholderfirstdateDAY.replace("0", "")
    
        rday = ('\\b' + placeholderfirstdateDAY + '\\b').replace('\\b ', '\\s')
        rdayc = "\033[91m" + placeholderfirstdateDAY + "\033[0m"

        placeholderseconddateMONTH = placeholderseconddate[1]
        placeholderseconddateDAY = placeholderseconddate[2]
        if(placeholderseconddateDAY[0] == "0"):
            placeholderseconddateDAY = placeholderseconddateDAY.replace("0", "")
        rday2 = ('\\b' + placeholderseconddateDAY + '\\b').replace('\\b ', '\\s')
        rdayc2 = "\033[91m" + placeholderseconddateDAY + "\033[0m"
        
        stufftoPrint = calendar.month(current_year, int(placeholderfirstdateMONTH))
        
        fullcalendar = re.sub(rday,rdayc,stufftoPrint)
        newfullcalendar = re.sub(rday2,rdayc2,fullcalendar)
        print("-----------------------------------------------------------------")
        print("Month of %s:" % monthDictionary[placeholderfirstdateMONTH])
        print("-----------------------------------------------------------------\n")

        print(newfullcalendar)
        print("Date Started: ", i[0])
        print("Date Ended: %s " % i[1])
        print("Approx Duration: %s \n" % i[3])
        print("Notes: %s\n" % i[2])
        
    return 0;
    
    
    
#https://www.geeksforgeeks.org/get-yesterdays-date-using-python/

def createCSV( ):
    #prototype of adding
    today = datetime.datetime.today()
    datestringformat =  datetime.datetime(2018, 6, 1)
    yesterday= today - datetime.timedelta(days = 1)
    print("createcsv")
    print(yesterday)
    testList = [1, datestringformat, yesterday, "blah"]
    
    with open('testdata/localtestdata/bloodmoon-test-data.csv', 'a', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(testList)
    f.close()
    
    
def displayAllDates():
#    today = datetime.date.today()
#    year  = today.year
#    month = today.month
    thism = calendar.calendar(current_year)    # gets the wholeeeee calendar
#    date  = today.day.__str__().rjust(2) #what even is this for, it just right aligns the string
#    rday  = ('\\b' + date + '\\b').replace('\\b ', '\\s')
    rdayc = "\033[7m" + date + "\033[0m"
    print( re.sub(rday,rdayc,thism)) #so like this literally is just looking for the string match
    return 0;


def createNewEntry():
    datestringformat =  datetime.datetime(2018, 6, 1)

#    startDate = input('\nStart Date (print in format of \"YEAR, MONTHNUMBER, DAY\"\nex. 2018, 6, 1\n')
    startDateMonth = int(input("\nenter the start month (1-12):\n"))
    startDateDay = int(input("\nenter the start day (1-31):\n"))
    startDate = datetime.date(int(current_year), startDateMonth, startDateDay)
    
    #endDate = input('End Date (print in format of \"YEAR, MONTHNUMBER, DAY\"\nex. 2018, 6, 1\n')
    endDateMonth = int(input("\nenter the end month (1-12):\n"))
    endDateDay = int(input("\nenter the end day (1-31):\n"))
    endDate = datetime.date(int(current_year), endDateMonth, endDateDay)
    print("Starting Date: %s" % startDate)
    print("Ending Date: %s\n" % endDate)
    notes = input("Notes: \n")
    
    gapPrevious =  endDate - startDate
    print(gapPrevious.days)

    MaskEntry = [startDate, endDate, notes, gapPrevious.days]
    print(MaskEntry)
    return MaskEntry

#this function just reads entries and returns an array of the objects in the csv file
def readEntries():
    rows = []
    with open('testdata/localtestdata/bloodmoon-test-data.csv', 'r', newline='') as f:
        csvreader = csv.reader(f)
        header = []
        header = next(csvreader)
        print(header)
    
        for row in csvreader:
            rows.append(row)
#        csvwriter = csv.writer(f)
#        csvwriter.writerow(testList)
    f.close()
    return rows

def main():
    try:
        print("\n--------------------------------------------\nBlood Moon Akali \n--------------------------------------------\n")
        print("A slightly handstitched app at the moment")
    #Continuous While loop in the terminal
        while True:
#            displayAllDates()

    #0. Display Directory
            print("\n--------------------------------------------\nMake a Selection Below: \n--------------------------------------------\n")
            for i in channelDirectory:
                print("[%s]: %s" % (i,channelDirectory[i]))
             
    #0. User Selection
            menuSelection=''
            while(menuSelection==''):
                menuSelection=input('\nMenu Selection::\n')
            menuSelection=int(menuSelection)
    #1. Display Dates
            if(menuSelection == 1):
                print("[%s]: %s" % (1,channelDirectory[1]))
                rows = readEntries()
                for i in rows:
                    print(i)
                #time to display the calendar
                displayCalendar(rows)
                
                #displayFullCalendar(rows)
    #2. Guestimate
            elif(menuSelection == 2):
                print("coming soon")
    #3. Add in a new entry
            elif(menuSelection == 3):
                print("[%s]: %s" % (3,channelDirectory[3]))
                #Create a new array with info to append to csv file
                newsession = createNewEntry()
                #Open the csv file and append to it
                csvfile = open(sys.argv[1], 'a', newline='')
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(newsession)
                csvfile.close()
            elif(menuSelection == 4):
                print("Coming soon, although you could just edit the csv directly provided that the formatting fits with the rest of it")
    except:
        print("Interrupted!")


        
if __name__ == "__main__":
    main()
