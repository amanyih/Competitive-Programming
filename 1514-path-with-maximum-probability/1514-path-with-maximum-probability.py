class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        graph = defaultdict(list)
        for i,node in enumerate(edges):
            a,b = node
            graph[a].append((b,succProb[i]))
            graph[b].append((a,succProb[i]))
            
        heap = [(0,start_node)]
        visited = set()
        
        while heap:
            
            cur_prob,cur_node = heappop(heap)
            # print(cur_prob,cur_node)
            if cur_node == end_node:
                return 1-cur_prob
            if cur_node in visited:
                continue
            visited.add(cur_node)
            
            for child in graph[cur_node]:
                nxt,prob = child
                nxt_probablity = 1- ((1 - cur_prob) * prob)
                heappush(heap,(nxt_probablity,nxt))
        return 0