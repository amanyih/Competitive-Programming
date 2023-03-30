class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        
        def find(nums,k):
            if len(nums) == 1:
                return nums[0]
            
            pivot = nums[len(nums) // 2]
            less = []
            equal = []
            more  = []
            
            for num in nums:
                if num < pivot:
                    less.append(num)
                elif num > pivot:
                    more.append(num)
                else:
                    equal.append(num)
            if len(more) >= k:
                return find(more,k)
            elif len(equal) + len(more) >= k:
                return equal[0]
            else:
                return find(less,k-len(equal)-len(more))
        
        return find(nums,k)
            
            
            
            