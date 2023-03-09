class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def helper(cur,stack):
            
            if len(stack) == k:
                newList = stack.copy()
                if len(set(newList)) == k:
                    ans.append(newList)
                return
            current = [x for x in range(cur+1,n+1)]
            
            for num in current:
                s = stack.copy()
                s.append(num)
                helper(num,s)
        
        for i in range(n):
            helper(i,[])
        
        res = []
        
        for a in ans:
            if a not in res:
                res.append(a)
        return res
        
        