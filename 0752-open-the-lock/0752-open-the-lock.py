class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        deadends = set(deadends)
        if "0000" in deadends: return -1
            
        graph = defaultdict(set)
        
        def build(num):
            nums = str(num)
            
            lst = []
            
            for i in range(4-len(nums)):
                lst.append("0")
            
            for c in nums:
                lst.append(c)
            org = "".join(lst)
            for i,c in enumerate(lst):
                
                lst[i] = str(int(c)+1) if int(c) < 9 else "0"
                graph[org].add("".join(lst))
                graph["".join(lst)].add(org)
                
                lst[i] = str(int(c)-1) if int(c) > 0 else "9"
                graph[org].add("".join(lst))
                graph["".join(lst)].add(org)  
                lst[i] = c
        for i in range(10000):
            build(i)
        
        q = deque([("0000",0)])
        visited = set()
        
        while q:
            cur,count = q.popleft()
            if cur == target:
                return count
            
            for nxt in graph[cur]:
                if nxt not in visited and nxt not in deadends:
                    visited.add(nxt)
                    q.append((nxt,count + 1))
        return -1
                
                
            
        