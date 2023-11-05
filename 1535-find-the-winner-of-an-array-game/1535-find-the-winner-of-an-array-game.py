class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k >= len(arr):
            return max(arr)
        
        
        cur = arr[0]
        q = deque(arr[1:])
        streak = 0
        
        
        while q:
            op = q.popleft()
            
            if op > cur:
                q.append(cur)
                cur = op
                streak = 1
            else:
                streak += 1
                q.append(op)
            
            if streak == k:
                return cur
                
            
            
            
        
        
        