class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums1 = [nums1[i]-nums2[i] for i in range(len(nums1))]
        # x <= y + diff
        global ans
        ans = 0
        def merge(left,right,diff):
            global ans
            
            p1 = 0
            
            for p2 in range(len(right)):
                while p1 < len(left) and left[p1] <= right[p2] + diff:
                    p1+= 1
                ans += p1

            
            
            
            l = r = 0
            res = []
            
            while l < len(left) and r < len(right):
                if left[l]  <= right[r]:
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
        def split(arr,diff):
            if len(arr) == 1:
                return arr
            
            
            mid = len(arr) // 2
            
            left = split(arr[:mid],diff)
            right = split(arr[mid:],diff)
            
            return merge(left,right,diff)
        split(nums1,diff)
        return ans
                    
                
        