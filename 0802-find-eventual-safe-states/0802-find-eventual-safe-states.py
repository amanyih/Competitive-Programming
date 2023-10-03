class Solution:
    def eventualSafeNodes(self, lst: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for i,nodes in enumerate(lst):
            for node in nodes:
                graph[node].append(i)
                indegree[i] += 1
        q = deque()
        for node in range(len(lst)):
            if indegree[node] == 0:
                q.append(node)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegree[node] -=1
                if indegree[node] == 0:
                    q.append(node)
        return sorted(res)
                
            
        