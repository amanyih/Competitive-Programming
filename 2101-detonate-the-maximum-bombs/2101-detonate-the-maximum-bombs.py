class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            x1,y1,r1 = bombs[i]
            
            for j in range(i+1,len(bombs)):
                x2,y2,r2 = bombs[j]
                radius = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                # print("x",x1,x2)
                # print("y",y1,y2)
                # pritn(radius)
                if r1 >= radius:
                    graph[i].append(j)
                if r2 >= radius:
                    graph[j].append(i)
        
        # print(graph)
        def explode(cur,visited):
            
            visited.add(cur)
            
            for nxt in graph[cur]:
                if nxt not in visited:
                    explode(nxt,visited)
            
            return len(visited)
        ans = 0
        
        for i in range(len(bombs)):
            curLen = explode(i,set())
            ans = max(ans,curLen)
        return ans
            