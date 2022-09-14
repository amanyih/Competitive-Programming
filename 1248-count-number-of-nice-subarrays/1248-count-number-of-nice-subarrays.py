class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        dict_ = {}
        
        for i in range(len(nums)):
            if nums[i] %2 ==0:
                nums[i] = 0
            else:
                nums[i] = 1
        currentSum = 0
        ans = 0
        
        for num in nums:
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
        
        