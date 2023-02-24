class RecentCounter:

    def __init__(self):
        self.queue= deque()
        

    def ping(self, t: int) -> int:
        left = t - 3000
        while self.queue and self.queue[0] < left:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)