class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        l1 = l2 = 0
        
        ans = []
        
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                ans.append(nums1[l1])
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2] :
                l1 += 1
            else:
                l2 += 1
        return ans
        