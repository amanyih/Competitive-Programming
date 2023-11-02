class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_candy = max(candies)
        
        ans = []
        for candy in candies:
            ans.append((candy+extraCandies) >= max_candy )
        
        return ans
        