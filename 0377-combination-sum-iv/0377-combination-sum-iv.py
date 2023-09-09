class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        cache = defaultdict(int)
        cache[0] = 1
        
        for val in range(1,target+1):
            for num in nums:
                cache[val] += cache[val-num]
        
        return cache[target]
        