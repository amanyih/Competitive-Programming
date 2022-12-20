class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
             l                         l
        """
        nums = nums1.copy()
        l = 0
        r = 0
        k = 0
        while l < m and r < n:
            if nums[l] < nums2[r]:
                nums1[k] = nums[l]
                l += 1
            else:
                nums1[k] = nums2[r]
                r += 1
            k += 1
        while l < m:
            nums1[k] = nums[l]
            l += 1
            k += 1
        while r < n:
            nums1[k] = nums2[r]
            r += 1
            k += 1
                