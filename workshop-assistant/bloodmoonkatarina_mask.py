import datetime

class Mask:
    def __init__(self, id, startDate, endDate, notes, gapPrevious):
        self.id = id
        self.startDate = startDate
        self.endDate = endDate
        self.notes = notes
        self.gapPrevious = gapPrevious


