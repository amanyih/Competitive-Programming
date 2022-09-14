class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        dict_ = {}
        currentSum = 0
        ans = 0
        
        for num in nums:
            num = 0 if num % 2 == 0 else 1
            currentSum += num
            if currentSum == k:
                ans += 1
            if (currentSum - k) in dict_:
                ans += dict_[currentSum - k]
            if currentSum in dict_:
                dict_[currentSum] += 1
            else:
                dict_[currentSum] = 1
        
        return ans
        
        