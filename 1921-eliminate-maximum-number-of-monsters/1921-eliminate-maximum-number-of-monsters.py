class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        heap = []
        for i in range(len(dist)):
            time = dist[i] / speed[i]
            heappush(heap,(time,dist[i],-speed[i]))
        
        time = 0
        while heap:
            t,s,v = heappop(heap)
            
            if s + (v*time) <= 0:
                return time
            
            time += 1
        return time
            
        