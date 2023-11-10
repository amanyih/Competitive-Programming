class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_q = deque()
        d_q = deque()
        
        index = 0
        while index < len(senate):
            if senate[index] == "R":
                r_q.append(index)
            else:
                d_q.append(index)
            index += 1
        
        while r_q and d_q:
            r = r_q.popleft()
            d = d_q.popleft()
            
            if r < d:
                r_q.append(index)
            else:
                d_q.append(index)
            index += 1
        
        return "Radiant" if r_q else "Dire"
        
        
        
        
        
                    
        