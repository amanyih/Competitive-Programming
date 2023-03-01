class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n = len(nums)
        prefix = [0] * n
        
        for request in requests:
            i,j = request
            prefix[i] += 1
            if j+1  < n:
                prefix[j+1] -= 1
            
        for i in range(1,n):
            prefix[i] = prefix[i-1] + prefix[i]
        
        nums.sort()
        prefix.sort()
        
        ans = 0
        
        for i in range(n):
            ans += prefix[i] * nums[i]
        return ans % (10**9 + 7)
            
        