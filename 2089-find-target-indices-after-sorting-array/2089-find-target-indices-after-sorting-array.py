class Solution(object):
    def targetIndices(self,nums,target):
        lis =[]
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j]>=nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        for i in range(len(nums)):
            if nums[i]==target:
                lis.append(i)
        return lis
        
        