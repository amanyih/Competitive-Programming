class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10 ** 9 + 7
        ans = [1] * len(arr)
        prev = defaultdict(int)
        
        for i in range(len(arr)):
            prev[arr[i]] = 1
            cur = 0
            for j in range(i):
                new = prev[arr[j]] * prev[arr[i]/arr[j]]
                cur += new
            prev[arr[i]] += cur
            ans[i] += cur
        return sum(ans) % MOD
                
                
            
        