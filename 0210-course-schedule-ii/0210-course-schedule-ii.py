class Solution:
    def findOrder(self, num: int, preq: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        inde = defaultdict(int)
        
        for pre in preq:
            a,b = pre
            graph[b].append(a)
            inde[a] += 1
        
        starts = []
        
        for i in range(num):
            if not inde[i]:
                starts.append(i)
        
        q = deque(starts)
        
        res = []
        
        while q:
            print(q)
            
            cur = q.popleft()
            res.append(cur)
            
            for c in graph[cur]:
                
                inde[c] -= 1
                if inde[c] == 0:
                    q.append(c)
        
        
        return res if len(res) == num else []
            