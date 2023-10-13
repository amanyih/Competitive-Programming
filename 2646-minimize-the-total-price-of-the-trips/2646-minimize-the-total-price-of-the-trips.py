class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        
        count = defaultdict(int)
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def bfs_count(start,end):
            q = deque([(start,[start])])
            visited = set()
            res  = []
       
            while q:
                node,path = q.pop()
                if node == end:
                    res = path
                    break
                
                for nxt in graph[node]:
                    if nxt not in visited:
                        q.append((nxt,path+[nxt]))
                        visited.add(nxt)
            # print(start,end,res)
            for node in res:
                count[node] += 1

        for a,b in trips:
            bfs_count(a,b)
        
        cache = {}
        def halve_prices(node,prev,visited = set()):
            
            if (node,prev) in cache:
                return cache[(node,prev)]

            visited.add(node)
            others = 0
            for nxt in graph[node]:
                if nxt not in visited:
                    others += halve_prices(nxt,0,visited)
            
            others += price[node] * count[node]
            
            if not prev:
                others_halved = 0
                for nxt in graph[node]:
                    if nxt not in visited:
                        others_halved += halve_prices(nxt,1,visited)
                
                others_halved += price[node]//2 * count[node]
                others = min(others,others_halved)
            
                
            visited.remove(node)
            
            cache[(node,prev)] = others
            return others
        return halve_prices(0,0)
                
                
                
            
            
            
            
            
                    
            
            
                
            
            
            
        
                
            
            
            
        