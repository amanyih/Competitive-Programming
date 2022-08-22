class Solution(object):
    def singleNumber(self, nums):
        sett = {}
        
        for num in nums:
            if sett and num in sett:
                sett[num] += 1
            else:
                sett[num] = 1
        for key in sett:
            if sett[key] == 1:
                return key
        
        