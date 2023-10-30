class UndergroundSystem:
    
    """
    a check in at 5
    b check in at 6
    getAverage ? if so what's the expected answer?
    """

    def __init__(self):
        self.check_in = {}
        self.total_time = defaultdict(int)
        self.no_people = defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station,start_time = self.check_in[id]
        self.total_time[(station,stationName)] += t - start_time
        self.no_people[(station,stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total_time[(startStation,endStation)] / self.no_people[(startStation,endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)