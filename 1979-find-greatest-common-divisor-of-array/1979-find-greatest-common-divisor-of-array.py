class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        minNum = inf
        maxNum = -inf
        for num in nums:
            minNum = min(minNum,num)
            maxNum = max(maxNum,num)
        
        return gcd(minNum,maxNum)
        