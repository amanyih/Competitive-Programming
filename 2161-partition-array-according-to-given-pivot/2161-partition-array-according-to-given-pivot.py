class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less = []
        p = []
        more = []
        
        for num in nums:
            if num > pivot:
                more.append(num)
            elif num < pivot:
                less.append(num)
            else:
                p.append(num)
        
        nums = less + p + more
        return nums