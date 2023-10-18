class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        even_indexes = defaultdict(int)
        odd_indexes = defaultdict(int)
        
        for i in range(len(nums)):
            if i %2:
                odd_indexes[nums[i]] += 1
            else:
                even_indexes[nums[i]] += 1
        
        topOdd,secondOdd = (None,0),(None,0)
        
        for num in odd_indexes:
            if odd_indexes[num] > topOdd[-1]:
                secondOdd = topOdd
                topOdd = (num,odd_indexes[num])
            elif odd_indexes[num] > secondOdd[-1]:
                secondOdd = (num,odd_indexes[num])
        topEven,secondEven = (None,0),(None,0)
        
        for num in even_indexes:
            if even_indexes[num] > topEven[-1]:
                secondEven = topEven
                topEven = (num,even_indexes[num])
            elif even_indexes[num] > secondEven[-1]:
                secondEven = (num,even_indexes[num])
                
        
        if topOdd[0] != topEven[0]:
            return len(nums) - topOdd[1] - topEven[1]
        else:
            return len(nums) - max(secondOdd[1] + topEven[1], secondEven[1] + topOdd[1])
        
        
        
        
        
                
        
        
        
        
            
        
        
        
            