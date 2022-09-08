class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        
        low = 0
        high = len(numbers)-1
        
        while low < high:
            if numbers[low] + numbers[high] == target:
                ans.append(low+1)
                ans.append(high+1)
                return ans
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                high -=1
        
        return ans
                