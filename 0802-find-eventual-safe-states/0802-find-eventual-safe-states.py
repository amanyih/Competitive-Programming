class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        lst = defaultdict(list)
        terminals = set()
        isTerminal = {}
        for i,g in enumerate(graph):
            lst[i] = g
            if not len(g):
                terminals.add(i)
        
        
        visited = set()
        
        def dfs(node):
            if node in isTerminal:
                return isTerminal[node]
            elif node in terminals:
                return True
            visited.add(node)
            cur = []
            
            for n in lst[node]:
                
                if n in isTerminal:
                    cur.append(isTerminal[n])
                elif n in terminals:
                    cur.append(True)
            
                elif n in visited:
                    cur.append(False)
                else:
                    cur.append(dfs(n))
            
            val = all(cur)
            isTerminal[node]  = val
            return val
        ans = []
        for node in lst:
            if dfs(node):
                ans.append(node)
        
        ans.sort()
        
        return ans
                
        
                    
            
            
            

            
            
        
        
            
        
        