class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        distance = [inf for i  in range(n+1)]
        
        for s,e,w in times:
            graph[s].append((e,w))
        
        heap = [(0,k)]
        heapify(heap)
        visited = set()
        visited.add(k)
        
        while heap:
            dist,node = heappop(heap)
            # print(dist,node)
            distance[node] = min(dist,distance[node])
            visited.add(node)
            
            for child in graph[node]:
                nxt,w = child
                if nxt not in visited:
                    heappush(heap,(w+dist,nxt))
                    
        ans = -inf
        # print(distance)
        for i in range(1,n+1):
            if distance[i] == inf:
                return -1
            ans = max(distance[i],ans)
        return ans
            
        
        