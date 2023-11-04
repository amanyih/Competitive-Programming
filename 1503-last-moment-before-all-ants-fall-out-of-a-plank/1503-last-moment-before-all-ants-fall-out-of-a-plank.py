class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        
        
        for ant in left:
            ans = max(ans,ant)
        
        for ant in right:
            ans = max(ans,n-ant)
        
        return ans