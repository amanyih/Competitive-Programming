class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        left = 0
        
        ans = []
        while left < len(intervals):
            start = intervals[left][0]
            end = intervals[left][1]
            right = left + 1
            
            while right < len(intervals) and end >= intervals[right][0]:
                end = max(end,intervals[right][1])
                right += 1
            
            ans.append([start,end])
            left = right
        
        return ans
            
        