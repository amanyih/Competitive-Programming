class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary.sort()
        
        newSalary = salary[1:len(salary)-1]
        
        return sum(newSalary)/len(newSalary)
        