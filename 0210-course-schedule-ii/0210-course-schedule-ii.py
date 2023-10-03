class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        q = deque()
        
        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)
        # print(q)
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)
            
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if not indegree[nxt]:
                    q.append(nxt)
        # print(order)
        if len(order) != numCourses:
            return []
        return order
            