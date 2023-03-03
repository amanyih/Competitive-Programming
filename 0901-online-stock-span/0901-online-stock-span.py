class StockSpanner:

    def __init__(self):
        self.stack = []

        
    def next(self, price: int) -> int:
        cur = 0
        while self.stack and self.stack[-1][0] <= price:
            cur += self.stack.pop()[-1]
        
        self.stack.append([price,cur+1])
        return cur+1
    
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)