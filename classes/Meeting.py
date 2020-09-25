class Meeting:
    def __init__(self, day, time, peopleAvailable):
        self.day = day
        self.time = time
        self.peopleAvailable = peopleAvailable

    def addPerson(self, person):
        self.peopleAvailable.append(person)
