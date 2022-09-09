class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = 0
        first = 1
        
        while first <len(nums):
            if nums[last] != 0:
                last += 1
                first+= 1
            elif nums[first] != 0:
                nums[last],nums[first] = nums[first],nums[last]
                last += 1
                first += 1
            else:
                first += 1
                
                
                
                    
            

                                                                                                           