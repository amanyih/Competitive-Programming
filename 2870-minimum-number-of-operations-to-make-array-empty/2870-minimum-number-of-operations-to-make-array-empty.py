class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        ans = 0
        
        # print(count)
        
        for key in count:
            
            cur = count[key]
            
            if cur == 1:
                return -1
            
            ans += ceil(cur/3)
            
        return ans