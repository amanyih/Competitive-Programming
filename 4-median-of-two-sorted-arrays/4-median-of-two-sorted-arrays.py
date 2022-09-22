class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        l1 = 0
        l2 = 0
        
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                merged.append(nums1[l1])
                l1 += 1
            else:
                merged.append(nums2[l2])
                l2 += 1
        
        if l1 < len(nums1):
            merged += nums1[l1:]
        elif l2 < len(nums2):
            merged += nums2[l2:]
        
        if len(merged) % 2 != 0:
            mid = len(merged) //  2
            return float(merged[mid])
        else:
            mid = len(merged) // 2
            return (merged[mid]+merged[mid-1])/2
            