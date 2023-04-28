class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        
        ans = 0
        graph = defaultdict(list)
        visited = set()
        
        for edge in edges:
            a,b = edge
            graph[a].append(b)
            graph[b].append(a)
    
        
        def dfs(cur):
            # print(cur)
            nonlocal ans
            
            visited.add(cur)
            
            response = []
            
            for neigh in graph[cur]:
                if neigh not in visited:
                    
                    response.append(dfs(neigh))
            
            count = response.count(True)
            ans += count * 2
            
            return any(response) or hasApple[cur]
        dfs(0)
        return ans
        