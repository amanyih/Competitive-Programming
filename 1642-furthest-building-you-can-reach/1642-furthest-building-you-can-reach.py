class Solution:
    def furthestBuilding(self, heights: List[int], b: int, l: int) -> int:
        
        
        ladders = []
        bricks = 0
        i = 0
        
        
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                heappush(ladders,heights[i]-heights[i-1])
                
                if len(ladders) > l:
                    bricks += heappop(ladders)
                
                if bricks > b:
                    return i - 1
        return i
        