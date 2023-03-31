class Solution:
    def countPrimes(self, n: int) -> int:
        
        nums = [0] * n
        
        count = 0
        
        for i in range(2,n):
            # print(nums[i-1],i)
            if nums[i-1] == 0:
                # print("here",i)
                count += 1
                for j in range(i,len(nums),i):
                    
                    nums[j-1] += 1
        # print(nums)
        return count
        