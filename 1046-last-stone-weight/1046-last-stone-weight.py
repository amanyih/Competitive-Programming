class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapify(stones)
        
        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            
            if abs(x-y) != 0:
                heappush(stones,-abs(x-y))
        
        return -sum(stones)
            
