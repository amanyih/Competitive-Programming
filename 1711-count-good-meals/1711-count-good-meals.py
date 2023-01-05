class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness.sort()
        
        possibleScores = [2**i for i in range(22)]
        
        ans = 0
        
        for target in possibleScores:
            count = defaultdict(int)
            
            for taste in deliciousness:
                
                targetScore = target - taste
                ans += count[targetScore]
                count[taste] += 1
        
        return ans % (10**9 + 7)
                    
                
            
            
        