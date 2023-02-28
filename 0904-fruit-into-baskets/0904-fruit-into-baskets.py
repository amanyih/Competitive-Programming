class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        curCount = {}
        
        ans = 0
        
        for right in range(len(fruits)):
            curCount[fruits[right]] = curCount.get(fruits[right],0) + 1
            
            while len(curCount) > 2:
                curCount[fruits[left]] -= 1
                if curCount[fruits[left]] == 0:
                    del curCount[fruits[left]]
                left += 1
            ans = max(ans,right-left+1)
        
        return ans
                
        