class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        cache = {0 : 1}
    
        
        def find(target):
            # print(target)
            
            if target in cache:
                return cache[target]
            elif target < 0:
                return 0
            
            count = 0
            
            for num in nums:
                count += find(target - num)
            
            cache[target] = count
            
            
            return count
        
        return find(target)
        
        