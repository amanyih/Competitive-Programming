class Solution(object):
    def majorityElement(self, nums):
        fre = {}
        
        for num in nums:
            if fre and num in fre:
                fre[num] += 1
            else:
                fre[num] = 1
        
        for key in fre:
            if fre[key] > len(nums) / 2:
                return key
        