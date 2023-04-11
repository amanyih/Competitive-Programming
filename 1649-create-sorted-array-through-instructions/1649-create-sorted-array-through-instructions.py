class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        newArr = [[ins,0,0] for ins in instructions]
        # (num,smaller,greater)
        MOD = (10 ** 9) + 7
        
        def merge(left,right):
            res = []
            
            l = 0
            
            for r in range(len(right)):
                while l < len(left) and left[l][0] <= right[r][0]:
                    l += 1
                right[r][2] += len(left) - l
            
            l=r = 0
            
                        
                        
            while l < len(left) and r < len(right):
                if left[l][0] < right[r][0]:
                    res.append(left[l])
                    l += 1
                else:
                    right[r][1] += l
                    res.append(right[r])
                    r += 1
            if l < len(left):
                res.extend(left[l:])
            while r < len(right):
                right[r][1] += l
                res.append(right[r])
                r += 1
            return res
                       
        def split(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2
            
            left = split(arr[:mid])
            right = split(arr[mid:])
            
            
            return merge(left,right)
        sortt = split(newArr)
        ans = 0
        for num,s,l in sortt:
            ans += min(s,l)
        return ans % MOD
        