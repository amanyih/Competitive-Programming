"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        
        graph = defaultdict(tuple)
        
        for em in employees:
            _id,imp,sub = em.id,em.importance,em.subordinates
            graph[_id] = (imp,sub)
        
        global total
        total = 0
        visited = set()
        
        def dfs(idd):
            global total
            
            visited.add(idd)
            imp,sub = graph[idd]
            total += imp
            
            for i in sub:
                if i not in visited:
                    dfs(i)
        dfs(id)
        return total
        
            
            
            
            
            
            
            