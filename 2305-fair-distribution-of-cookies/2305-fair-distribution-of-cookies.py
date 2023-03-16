class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        global unfairness
        unfairness = inf
        
        people = [0] * k
        
        def distribute(c):
            global unfairness
            if c == len(cookies):
                unfairness = min(max(people),unfairness)
                return
            
            for i in range(len(people)):
                if people[i] + cookies[c] < unfairness:
                    people[i] += cookies[c]
                    distribute(c+1)
                    people[i] -= cookies[c]
        distribute(0)
        return unfairness
            
            
        