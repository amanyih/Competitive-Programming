class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def helper(cur,stack):
            
            if len(stack) == k:
                newList = stack.copy()
                # print(newList)
                # print(len(set(newList)))
                if len(set(newList)) == k:
                    # print("asdd")
                    # print(newList)
                    ans.append(newList)
                stack.pop()
                return
            current = [x for x in range(cur+1,n+1)]
            # print(current)
            # print(current)
            
            for num in current:
                s = stack.copy()
                s.append(num)
                # print(num,stack)
                helper(num,s)
        
        for i in range(n):
            helper(i,[])
        
        res = []
        
        for a in ans:
            if a not in res:
                res.append(a)
        return res
        
        