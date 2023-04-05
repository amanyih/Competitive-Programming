class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            while arr[i] != arr[arr[i] - 1]:
                nxt = arr[i]
                arr[i], arr[nxt-1] = arr[nxt-1], arr[i]
        
        ans = []
        
        for i,val in enumerate(arr):
            if i +1 != val:
                ans.append(val)
        return ans