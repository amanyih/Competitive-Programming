class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        nums = [[num,i] for i,num in enumerate(nums)]
        
        def merge(left,right):
            
            l = r = 0
            res = []
            
            while l<len(left) and r < len(right):
                
                if left[l][0] <= right[r][0]:
                    res.append(left[l])
                    ans[left[l][1]] += r
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            while l < len(left):
                res.append(left[l])
                ans[left[l][1]] += r
                l += 1
            if r < len(right):
                res.extend(right[r:])
            return res
        def split(arr):
            if len(arr) ==  1:
                return arr
            mid = len(arr) // 2
            
            left = split(arr[:mid])
            right = split(arr[mid:])
            
            return merge(left,right)
        split(nums)

        return ans
                    