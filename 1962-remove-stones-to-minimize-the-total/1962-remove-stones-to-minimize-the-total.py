class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        
        _piles = [-pile for pile in piles]
        
        
        heapify(_piles)
        # print(_piles)
        for _ in range(k):
            # print(_piles)
            
            cur = -heappop(_piles)
            sub = cur// 2
            cur = cur - sub
            
            heappush(_piles,-cur)
        
        return -sum(_piles)