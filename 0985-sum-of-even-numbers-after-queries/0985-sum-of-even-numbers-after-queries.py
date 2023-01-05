class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        
        """     0 1 2 3   cur = 2
        nums = [2,-1,3,3], queries = [[1,0],[-3,1],[-4,0],[2,3]]
        [8,6,2,4]                                             q
        
        [2,-1,3,4]
        6
        """
        
        ans = []
        curSum = 0
        
        for num in nums:
            if num % 2 == 0:
                curSum += num
        for query in queries:
            val,index = query
            
            if nums[index] % 2 == 0 and val % 2 == 0:
                curSum += val
            elif nums[index] % 2 ==0:
                curSum -= nums[index]
            elif nums[index] % 2 and val % 2:
                curSum += (val+nums[index])
            nums[index] += val
            ans.append(curSum)
        return ans
            