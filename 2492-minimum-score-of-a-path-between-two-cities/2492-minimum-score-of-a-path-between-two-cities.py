class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        
        graph = defaultdict(list)
        
        for a,b,c in roads:
            graph[a].append((b,c))
            graph[b].append((a,c))
        
        ans = inf
        visited = set()
        
        def dfs(a):
            nonlocal ans
            
            visited.add(a)
            
            for b,c in graph[a]:
                ans = min(c,ans)
                if b not in visited:
                    dfs(b)
        
        dfs(1)
        
        return ans
            