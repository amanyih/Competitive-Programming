class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        locations = {}
        for i,val in enumerate(nums):
            locations[val] = i
        
        for operation in operations:
            oldVal,newVal = operation
            index = locations[oldVal]
            nums[index] = newVal
            del locations[oldVal]
            locations[newVal] = index
        return nums
            