class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}
        self.journeyTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.checkIns[id]
        del self.checkIns[id]

        journey = (startStation, stationName)
        journeyTime = t - checkInTime

        if journey in self.journeyTimes:
            totalTime, tripCount = self.journeyTimes[journey]
            self.journeyTimes[journey] = (totalTime + journeyTime, tripCount + 1)
        else:
            self.journeyTimes[journey] = (journeyTime, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = (startStation, endStation)
        totalTime, tripCount = self.journeyTimes[journey]
        return totalTime / tripCount


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)