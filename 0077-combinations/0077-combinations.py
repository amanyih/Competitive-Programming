class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        solution = []
        
        def isValidState(state):
            if len(state) == k and len(set(state)) == k:
                return True
            return False
        
        def getNextCandidates(state):
            lastNum = state[-1] if state else 0
            return [x for x in range(lastNum+1,n+1)]
        
        def search(state):
            if isValidState(state):
                solution.append(state[:])
                return
            elif len(state) == k:
                return
            
            for candidate in getNextCandidates(state):
                state.append(candidate)
                search(state)
                state.pop()
        
        def solve():
            state = []
            search(state)
        solve()
        return solution
        