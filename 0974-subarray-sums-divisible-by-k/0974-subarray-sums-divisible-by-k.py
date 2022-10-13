class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        
        remainders = {0:1}
        prefix = 0
        ans = 0
        
        
        for num in nums:
            prefix += num
            remainder = prefix % k
            
            if remainder in remainders:
                ans += remainders[remainder]
            
            remainders[remainder] = remainders.get(remainder,0) +1
            
        return ans
        