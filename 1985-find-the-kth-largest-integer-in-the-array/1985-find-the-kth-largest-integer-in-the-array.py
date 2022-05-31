class Solution(object):
    def kthLargestNumber(self, nums, k):
        comp=lambda arr: int(arr)
        nums.sort(key=comp,reverse=True)
        return nums[k-1]
        