class RandomizedSet:

    def __init__(self):
        self.indexes = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.indexes: return False
        self.nums.append(val)
        self.indexes[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.indexes: return False
        
        i = self.indexes[val]
        self.nums[i],self.nums[len(self.nums)-1] = self.nums[len(self.nums)-1],self.nums[i]
        self.indexes[val] = len(self.nums) -1
        self.indexes[self.nums[i]] = i
        self.nums.pop()
        del self.indexes[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()