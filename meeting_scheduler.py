import csv #csv
import copy #deepcopy
import functools #reduce

## HELPER FUNCTIONS

def selectionSort(A):
    # Traverse through all array elements 
    for i in range(len(A)): 
      
        # Find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx].numberUnavailable > A[j].numberUnavailable: 
                min_idx = j 
              
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]
        
    return

def combineSchedules(schedule1, schedule2):
    combinedSchedule = []
    for pair in zip(schedule1, schedule2):
        combinedSchedule.append(pair[0] + pair[1])
    return combinedSchedule
        
## CLASSES

class TimeSlot:
    def __init__(self, day, time, availability):
        self.day = day
        self.time = time
        self.availability = availability

class MatchResult:
    def __init__(self, days, times, availabilities):
        self.dayA = days[0]
        self.dayB = days[1]
        self.timeA = times[0]
        self.timeB = times[1]
        combinedSchedules = combineSchedules(availabilities[0], availabilities[1])
        unavailablePeople = []
        for i in range(0, len(combinedSchedules)):
            if combinedSchedules[i] == 0:
                unavailablePeople.append(NAMES[i])
        self.combinedSchedules = combinedSchedules
        self.unavailablePeople = unavailablePeople
        self.numberUnavailable = len(unavailablePeople)

## SCRIPT

fileObject = open('bible_study_schedules.csv')
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
        match = MatchResult((scheduleA.day, scheduleB.day), (scheduleA.time, scheduleB.time), (scheduleA.availability, scheduleB.availability))
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
    
    

    




