class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        p = 0
        n = 0
        ans = []
        while p < len(nums) and n < len(nums):
            if nums[p] < 0:
                p += 1
            elif nums[n] > 0:
                n += 1
            else:
                ans.append(nums[p])
                ans.append(nums[n])
                p += 1
                n += 1
        
        return ans

