class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = 0
        ans= 0
        for num in gain:
            prefixSum += num
            ans = max(ans,prefixSum)
        
        return ans