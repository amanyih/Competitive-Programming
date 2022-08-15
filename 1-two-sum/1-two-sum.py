class Solution(object):
    def twoSum(self,nums,target):
        myDict = dict()
        for i in range(len(nums)):
            if nums[i] in myDict:
                return [myDict[nums[i]],i]
            else:
                myDict[target-nums[i]]=i
        
        