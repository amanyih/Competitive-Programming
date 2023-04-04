class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left == right:
            return [-1,-1]
        
        
        
        def findPrimes(left,right):
            prime = [True for i in range(right + 1)]
            p = 2
            
            while(p * p <= right):
                if prime[p]:
                    for i in range(p * p, right + 1, p):
                        prime[i] = False 
                p += 1
            ans = []
            diff= float("inf")
            queue = deque()
            start = max(2,left)
            end = right + 1
            
            for i in range(start,end):
                if prime[i]:
                    queue.append(i)
                    if len(queue) == 2:
                        if queue[1] - queue[0] < diff:
                            ans = [queue[0],queue[1]]
                            diff = queue[1] - queue[0]
                        queue.popleft()
            if ans:
                return ans
            return [-1,-1]
        
        return findPrimes(left,right)
                        
                
                
                
            
        