class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        location = {}
        ansList = [-1] * len(nums1)
        stack =[]
        
        
        
        for i in range(len(nums1)):
            location[nums1[i]] = i
        
        for num in nums2:
            while stack and stack[-1] < num:
                if stack[-1] in location:
                    ansList[location[stack[-1]]] = num
                stack.pop()
            stack.append(num)
        
        return ansList
        
        