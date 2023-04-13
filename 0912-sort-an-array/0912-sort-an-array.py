class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left,right):
            
            l = 0
            r = 0
            res = []
            
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            if l < len(left):
                res.extend(left[l:])
            elif r < len(right):
                res.extend(right[r:])
            
            return res
                
            
        
        def mergeSort(lst):
            if len(lst) == 1:
                return lst
        
            mid = len(lst) // 2
            left = mergeSort(lst[:mid])
            right = mergeSort(lst[mid:])
            
            return merge(left,right)
        
        return mergeSort(nums)
        
            
                         
                         
                    
            
        