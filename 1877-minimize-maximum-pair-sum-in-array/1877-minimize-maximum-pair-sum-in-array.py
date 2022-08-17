class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        left = 0
        right = len(nums) - 1
        sum = 0
        while right - left > 0:
            currentSum = nums[right] + nums[left]
            if currentSum >sum:
                sum = currentSum
            left += 1
            right -=1

        return sum