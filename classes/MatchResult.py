class MatchResult:
    def __init__(self, days, times, unavailable):
        self.dayA = days[0]
        self.dayB = days[1]
        self.timeA = times[0]
        self.timeB = times[1]
        self.unavailablePeople = unavailable
        self.numberUnavailable = len(unavailable)
