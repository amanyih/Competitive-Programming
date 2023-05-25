class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        adjList = {i:[] for i in range(n)}  
        for i in range(n):
            x1 = points[i][0]; y1 = points[i][1]
            for j in range(i+1, n):
                x2 = points[j][0]; y2 = points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
          
        visited = set()
        res = 0
        minHeap = [(0, 0)] 
        while len(visited) < n: 
            dist, node = heapq.heappop(minHeap)
            if node in visited: continue
            visited.add(node)
            res += dist
            for dn in adjList[node]:  
                if dn[1] not in visited:
                    heapq.heappush(minHeap, dn)
        
        return res