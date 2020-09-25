import csv #csv
import copy #deepcopy
from classes.Meeting import Meeting
from classes.MatchResult import MatchResult
from functions.helperFunctions import selectionSort
from functions.helperFunctions import FindDifference

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
dailySchedules = {}
people = []

fileName = input('Enter the name of the schedule file: ')
try:
    fileObject = open(fileName)
except:
    print('File not found')
    exit(1)

csvObject = csv.reader(fileObject)

rowNumber = 0
#Prepare data
for row in csvObject:
    if rowNumber == 0:
        MEETING_TIMES = copy.deepcopy(row)
        MEETING_TIMES.pop(0)    #remove 'Timestamp'
        MEETING_TIMES.pop(0)    #remove 'Names'
        for day in DAYS:
            dailySchedules[day] = []
            for time in MEETING_TIMES:
                ##print(day, time)
                newMeeting = Meeting (day, time, [])
                dailySchedules[day].append(newMeeting)
        ##print(dailySchedules.keys())
            
    else:   #collect availability data
        availability = copy.deepcopy(row)
        timestamp = availability.pop(0)
        person = availability.pop(0)
        people.append(person)
        ##print(people)
        for i in range(len(availability)):
            delimiter = ';' if ";" in availability[i] else ','
            daysAvailable = [day.strip() for day in availability[i].split(delimiter)]
            ##print(daysAvailable)
            if daysAvailable != ['']:
                for day in daysAvailable:
                    ##print(day)
                    meeting = dailySchedules[day][i]
                    meeting.addPerson(person)

    rowNumber = rowNumber + 1

potentialMeetings = sum(dailySchedules.values(), [])


## Making every combination of meetings
pairedSchedules = []
for i in range(len(potentialMeetings)):
    meetingA = potentialMeetings[i]
    for j in range(i+1, len(potentialMeetings)):
        meetingB = potentialMeetings[j]
        peopleAvailable = meetingA.peopleAvailable + meetingB.peopleAvailable
        peopleUnavailable = FindDifference(people, peopleAvailable)
        match = MatchResult((meetingA.day, meetingB.day), (meetingA.time, meetingB.time), peopleUnavailable)
        pairedSchedules.append(match)

selectionSort(pairedSchedules)

outFileName = input('Enter the name for the report file: ')
with open(outFileName, 'w') as outFile:
    optionNumber = 1
    outFile.write('Schedule Report\n\n')
    for result in pairedSchedules:
        outFile.write('{number}) {dayA} {timeA} and {dayB} {timeB}\n'.format(number=optionNumber, dayA=result.dayA, timeA=result.timeA, dayB=result.dayB, timeB=result.timeB))
        outFile.write('Number  of people unavailable: {unavailable}\n'.format(unavailable=result.numberUnavailable))
        outFile.write('People who are unavailable: ')
        for name in result.unavailablePeople:
            outFile.write(name + ', ')
        outFile.write('\n\n')
        optionNumber = optionNumber + 1




    
    

    




