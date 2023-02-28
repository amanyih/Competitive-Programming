class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        
        count = {0:0}

        cur = 0
        ans = 0

        for num in nums:
            cur += num

            if cur == k:
                ans += 1
            ans += count.get(cur-k,0)
            count[cur] = count.get(cur,0) + 1
        
        return ans