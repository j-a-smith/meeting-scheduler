import csv #csv
import copy #deepcopy
from classes.MatchResult import MatchResult
from classes.TimeSlot import TimeSlot
from functions.helperFunctions import selectionSort

fileName = input('Enter the name of the schedule file: ')

fileObject = open(fileName)
csvObject = csv.reader(fileObject)

rowNumber = 0
schedules = []
pairedSchedules = []

#Prepare data
for row in csvObject:
    if rowNumber == 0:
        NAMES = copy.deepcopy(row)
        NAMES.pop(0)    #remove day
        NAMES.pop(0)    #remove time
    else:               #collect availability data
        day = row[0]
        time = row[1]
        availability = copy.deepcopy(row)
        availability.pop(0) #remove day
        availability.pop(0) #remove time
        for i in range(0, len(availability)):   # change chars to ints
            availability[i] = int(availability[i])
        schedules.append( TimeSlot(day, time, availability) )
    rowNumber = rowNumber + 1

## Making every 
for i in range(len(schedules)):
    scheduleA = schedules[i]
    for j in range(i+1, len(schedules)):
        scheduleB = schedules[j]
        match = MatchResult((scheduleA.day, scheduleB.day), (scheduleA.time, scheduleB.time), (scheduleA.availability, scheduleB.availability), NAMES)
        pairedSchedules.append(match)

selectionSort(pairedSchedules)

optionNumber = 1
print('Schedule Report')
print('---------------')
for result in pairedSchedules:
    print(str(optionNumber) + ') ' + result.dayA + ' ' + result.timeA + ' and ' + result.dayB + ' ' + result.timeB)
    print('Number unavailable: ' + str(result.numberUnavailable))
    print('People unavailable: ', end='')
    for name in result.unavailablePeople:
        print(name + ', ', end='')
    print()
    print('---------------')
    optionNumber = optionNumber + 1
    
    

    




