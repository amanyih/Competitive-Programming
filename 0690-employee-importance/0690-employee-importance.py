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
        
        totalImportance = 0
        ids = {}
        for i in range(len(employees)):
            ids[employees[i].id] = i
        
        stack = [employees[ids[id]]]
        while stack:
            emp = stack.pop()
            totalImportance += emp.importance
            
            for sub in emp.subordinates:
                stack.append(employees[ids[sub]])
        
        return totalImportance
        