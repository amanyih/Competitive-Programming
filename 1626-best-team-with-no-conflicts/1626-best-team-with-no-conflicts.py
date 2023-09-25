class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(ages)
        lst = [(ages[i],scores[i]) for i in range(n)]
        # lst.sort(key = lambda x : x[0])
        lst.sort()
        
        dp = [lst[i][1] for i in range(n)]
        # print("org",dp)
        
        for i in range(n):
            for j in range(i):
                cur = lst[i][1]
                # print(lst[j])
                
                if (lst[j][1] <= cur)  or (lst[i][0] == lst[j][0]):
        
                    dp[i] = max(dp[i],lst[i][1] + dp[j])
                    # print("dp up",dp)
        # print(dp)
        # print(lst)
        return max(dp)
        
                    
                
            