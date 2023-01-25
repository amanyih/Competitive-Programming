class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        count = set()
        
        for num in nums:
            count.add(num)
            new = 0
            
            while num > 0:
                new = new * 10 + num%10
                num = num // 10
            
            count.add(new)
        return len(count)
        