class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        ans= 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        
        return ans
        