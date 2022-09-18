class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())
        ans = (maxFreq - 1)* (n + 1)
        
        for i in count.values():
            if i == maxFreq:
                ans += 1
        
        ans = max(ans,len(tasks))
        
        return ans
        
        
        
        