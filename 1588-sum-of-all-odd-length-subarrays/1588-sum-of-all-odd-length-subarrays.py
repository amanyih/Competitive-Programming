class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefixSum = [0]
        for num in arr:
            prefixSum.append(prefixSum[-1] + num)
        ans = 0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                
                ans += prefixSum[j+1] - prefixSum[i]
        return ans
        