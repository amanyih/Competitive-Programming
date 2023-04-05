class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        count = set()
        maxN = 0

        for num in nums:
            count.add(num)
            maxN = max(maxN,num)
        
        for i in range(1,maxN+5):
            if i not in count:
                return i