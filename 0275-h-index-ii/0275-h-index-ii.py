class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n
        
        while left <= right:
            mid = (left+right) // 2
            index = n - mid
            
            if citations[-mid] >= mid:
                left = mid + 1
            else:
                right = mid -1
        return right
            
            

        
                
                