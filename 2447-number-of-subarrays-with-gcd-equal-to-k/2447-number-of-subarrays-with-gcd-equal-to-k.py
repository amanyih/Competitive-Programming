class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i,len(nums)):
                cur = nums[j] 
                
                _gcd= gcd(num,cur)
                count += 1 if _gcd == k else 0
                num = min(num,_gcd)
        return count
                
                
                
                