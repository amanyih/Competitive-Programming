class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        cache = {}
        sett = set(nums)
        
        def dp(num):
            # print(num)
            if num in cache:
                return cache[num]
            if num not in sett:
                # print("not in sett",num)
                return 0
            cur = 1 + dp(num-1)
            cache[num] = cur
            return cur
        ans = 0
        for num in nums:
            # print("calling")
            ans = max(ans,dp(num))
        return ans
        
        
        
        