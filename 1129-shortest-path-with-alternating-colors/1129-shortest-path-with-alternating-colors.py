class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for a,b in redEdges:
            graph[a].append((b,1,0))
        for a,b in blueEdges:
            graph[a].append((b,0,0))
        
        def bfs(destination,prevColor):
            # print("target",destination)
            q = deque([(0,prevColor,0)])
            visited = set()
            visited.add((0,prevColor))
            
            
            while q:
                cur = q.popleft()
                # print(cur)
                node,color,distance = cur
                if node == destination:
                    return distance
                
                
                for nxt in graph[node]:
                    # print("herehher")
                    n,c,d = nxt
                    if (n,c) not in visited and c == 1 - color:
                        q.append((n,c,distance + 1))
                        visited.add((n,c))
            return -1
        ans = []
        for i in range(n):
            red,blue = bfs(i,0),bfs(i,1)
            # print(i,red,blue)
            res = min(red,blue) if min(red,blue) != -1 else max(red,blue)
            ans.append(res)
        
        return ans
                
                
            
        
        
        