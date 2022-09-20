class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            
        prefixFreq = {0:1}
        
        prefix = 0
        ans = 0
        for num in nums:
            
            prefix += num
            
            if (prefix - k) in prefixFreq:
                ans += prefixFreq[prefix - k]
            
            if prefix in prefixFreq:
                prefixFreq[prefix] += 1
            else:
                prefixFreq[prefix] = 1
        
        return ans
    """
    {0:1, 1:1, 3:1, 6:1}   ans = 1 + 1
    """
    