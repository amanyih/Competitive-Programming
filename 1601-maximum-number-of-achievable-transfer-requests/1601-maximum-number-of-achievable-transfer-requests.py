class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        global ans
        ans = 0
        
        count = defaultdict(int)
        
        def isValid(count):
            
            for value in count.values():
                if value != 0:
                    return False
            return True
        
        def backtrack(path,index):
            global ans
            
            if index == len(requests):
                if isValid(count):
                    ans = max(ans,len(path))
                return
            
            start,end = requests[index]
            count[start] -= 1
            count[end] += 1
            path.append(1)
            backtrack(path,index+1)
            count[start] += 1
            count[end] -= 1
            path.pop()
            backtrack(path,index+1)
        
        backtrack([],0)
        return ans
            
                    