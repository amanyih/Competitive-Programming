class Solution(object):
    def maxFrequency(self,nums,k):
        nums.sort()
        ans=0
        sum = 0
        j=0
        for i in range(len(nums)):
            sum += nums[i]
            while (nums[i] * (i-j+1)) > (sum + k):
                sum-=nums[j]
                j+=1
            if (i-j+1)>ans:
                ans=i-j+1

        return ans
        