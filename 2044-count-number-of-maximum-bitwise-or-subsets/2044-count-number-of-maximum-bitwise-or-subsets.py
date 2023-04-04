class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        _or = 0
        for num in nums:
            _or |= num
        global count
        count = 0
        
        def backtrack(index,cur,maxOr):
            global count
            if index == len(nums):
                if cur == maxOr:
                    count += 1
                return
            backtrack(index+1,cur|nums[index],maxOr)
            backtrack(index+1,cur,maxOr)
        backtrack(0,0,_or)
        
        return count
                
            
        