class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        container = [[] for str in strs[0]]
        
        def isSorted(arr):
            
            for i in range(1,len(arr)):
                if arr[i] < arr[i-1]:
                    return 1
            return 0
            
        for str in strs:
            for i in range(len(str)):
                container[i].append(str[i])
        
        count = 0
        
        for c in container:
            
            count += isSorted(c)
        
        return count
        