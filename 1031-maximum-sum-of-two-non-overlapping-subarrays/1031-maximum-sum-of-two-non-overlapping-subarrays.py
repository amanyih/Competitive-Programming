class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ans = 0
        l = 0
        cur = 0
        for rightt in range(len(nums)):
            cur += nums[rightt]
            if rightt - l + 1 > secondLen:
                cur -= nums[l]
                l += 1
            before = Solution.firstLenn(nums[:l],firstLen)
            after = Solution.firstLenn(nums[rightt+1:],firstLen)
            ans = max(ans,cur+before,cur+after)
        
        return ans
        
        
        
        
    def firstLenn(nums,size):
        left = 0
        current = 0
        maxSum = 0
        
        for right in range(len(nums)):
            current += nums[right]
            
            if right - left + 1 > size:
                current -= nums[left]
                left +=1
            
            maxSum = max(maxSum,current)
        
        return maxSum
            
            
            