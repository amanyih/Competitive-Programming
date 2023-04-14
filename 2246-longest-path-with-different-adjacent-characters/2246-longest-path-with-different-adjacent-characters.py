class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        
        graph = defaultdict(list)
        
        for p,c in enumerate(parent):
            graph[c].append(p)
        
        ans = 0
        def dfs(node):
            nonlocal s
            nonlocal ans
            
            cur_max = []
            for child in graph[node]:
                cur = dfs(child)
                
                if s[child] != s[node]:
                    cur_max.append(cur)
                    cur_max.sort(reverse=True)
                    if len(cur_max) > 2:
                        cur_max.pop()
            pos = sum(cur_max) + 1
            
            ans = max(ans,pos)
            return (cur_max[0] + 1) if cur_max else 1
        dfs(0)
        return ans
                        
                        
                        
                    
                
                
                
            
        
            
            
        