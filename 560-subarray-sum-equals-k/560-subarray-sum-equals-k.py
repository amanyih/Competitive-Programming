class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict_ = {0:1}
        count = 0
        totalSum = 0
        
        for num in nums:
            totalSum += num
            if totalSum - k in dict_:
                count += dict_[totalSum-k]
            if totalSum in dict_:
                dict_[totalSum] += 1
            else:
                dict_[totalSum] = 1
        
        return count
            
        