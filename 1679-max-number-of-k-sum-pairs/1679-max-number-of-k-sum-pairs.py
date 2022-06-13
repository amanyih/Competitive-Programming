class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        f =0
        l=len(nums)-1
        count =0
        while f<l:
            if (nums[f] + nums[l])<k:
                f+=1
            elif (nums[f] + nums[l])>k:
                l-=1
            else:
                f+=1
                l-=1
                count+=1
        return count
        