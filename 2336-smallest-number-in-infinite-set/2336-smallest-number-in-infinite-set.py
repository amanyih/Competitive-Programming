class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [True] * 1001
        self.heap = [i for i in range(1, 1001)]
        
        heapify(self.heap)

    def popSmallest(self) -> int:
        val = heappop(self.heap)
        self.nums[val] = False

        return val
        
    def addBack(self, num: int) -> None:
        if not self.nums[num]:
            heappush(self.heap, num)
            self.nums[num] = True
        
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)