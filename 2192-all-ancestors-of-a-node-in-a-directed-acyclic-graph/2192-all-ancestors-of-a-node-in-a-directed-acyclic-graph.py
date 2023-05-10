class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        graph = defaultdict(list)
        ind = defaultdict(int)
        q = deque([])
        for a,b in edges:
            graph[a].append(b)
            
            ind[b] += 1
        
        for i in range(n):
            if ind[i] == 0:
                q.append(i)
              
        ans = [set() for _ in range(n)]
        
        
        while q:
            
            # for _ in range(len(q)):
            cur = q.popleft()

            for c in graph[cur]:
                ind[c] -= 1

                ans[c].update(ans[cur])
                ans[c].add(cur)

                if  ind[c] == 0:
                    q.append(c)
        
        return [sorted(list(ans[i])) for i in range(n)]
            