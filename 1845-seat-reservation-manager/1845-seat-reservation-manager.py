class SeatManager:

    def __init__(self, n: int):
        
        self.seats = [i +1 for i in range(n)]
        heapify(self.seats)
        
    def reserve(self) -> int:
        x = heappop(self.seats)
        return x
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats,seatNumber)
        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)