class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        ans = 0
        max_before = values[0]
        
        for i in range(1,len(values)):
            ans = max(ans,max_before + values[i]-i)
            max_before = max(max_before,values[i]+i)
        
        return ans
        