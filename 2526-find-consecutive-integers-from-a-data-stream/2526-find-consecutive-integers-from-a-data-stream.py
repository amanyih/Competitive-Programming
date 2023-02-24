class DataStream:

    def __init__(self, value: int, k: int):
        self.stack =[]
        self.value = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.stack.append(num)
        else:
            self.stack = []
        if len(self.stack) >= self.k:
            return True
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)