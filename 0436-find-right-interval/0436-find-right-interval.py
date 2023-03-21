class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        indices = {}
        for i,nums in enumerate(intervals):
            indices[nums[0]] = i
        arr = [interval[0] for interval in intervals]
        arr.sort()

        def binSearch(target):
            
            left = 0
            right = len(arr) - 1
            
            while left +1 <= right:
                mid = (left+right) // 2
                
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid +1
            
            return indices[arr[right]] if arr[right] >= target else -1
        res = []
        for interval in intervals:
            target = interval[1]
            res.append(binSearch(target))
        return res
            
        
            
            
        