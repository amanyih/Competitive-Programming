class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        
        graph = defaultdict(list)
        
        for a,b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        q = deque()
        ans = []
        
        for key in graph:
            # print(key,graph[key])
            if len(graph[key]) == 1:
                q.append(key)
                break
        
        visited = set()
        while q:
            # print("adfsad")
            cur = q.popleft()
            visited.add(cur)
            ans.append(cur)
            
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
        
        return ans
            
        
        
        