class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        global ans
        ans = 0
        def merge(left,right):
            # print("left",left,"right",right)
            global ans
            l =r = 0
            res = []
            
            p1 = p2 = 0
            while p1 < len(left) and p2 < len(right):
                if right[p2]*2 < left[p1]:
                    ans += len(left) - p1
                    p2 += 1
                else:
                    p1 += 1
                    
            
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
        
        def split(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2
            left = split(arr[:mid])
            right = split(arr[mid:])
            
            return merge(left,right)
        split(nums)
        return ans