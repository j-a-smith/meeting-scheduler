from functions.helperFunctions import combineSchedules

class MatchResult:
    def __init__(self, days, times, availabilities, names):
        self.dayA = days[0]
        self.dayB = days[1]
        self.timeA = times[0]
        self.timeB = times[1]
        combinedSchedules = combineSchedules(availabilities[0], availabilities[1])
        unavailablePeople = []
        for i in range(0, len(combinedSchedules)):
            if combinedSchedules[i] == 0:
                unavailablePeople.append(names[i])
        self.combinedSchedules = combinedSchedules
        self.unavailablePeople = unavailablePeople
        self.numberUnavailable = len(unavailablePeople)
