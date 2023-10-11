class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique = list(set(nums))
        unique.sort()
        def findIndex(num):
            left = 0
            right = len(unique) -1
            while left <= right:
                mid = (right+left)//2
                
                if unique[mid] <= num:
                    left = mid + 1
                else:
                    right = mid-1
            return left
                
                
            
        
        ans = inf
        for i,num in enumerate(unique):
            last = findIndex(num+len(nums)-1)
            ans = min(ans,len(nums)-last+i)
            # print(num,last,ans)
        return ans
            
        
        