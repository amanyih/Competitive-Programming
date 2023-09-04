class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        
        
        line = [0 for num in nums]
        
        for a,b in requests:
            line[a] += 1
            # print(a,line)
            
            if b+1 < len(nums):
                line[b+1] -= 1
        
                
        for i in range(1,len(line)):
            line[i] += line[i-1]
        
        line.sort()
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            ans += nums[i] * line[i]
        
        return ans % MOD
        