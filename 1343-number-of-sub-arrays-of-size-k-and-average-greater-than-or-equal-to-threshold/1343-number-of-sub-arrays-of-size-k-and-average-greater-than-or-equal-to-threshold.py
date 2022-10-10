class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        ans = 0
        left = 0
        cur = 0
        
        
        for right in range(len(arr)):
            cur += arr[right]
            
            if right - left + 1 == k:
                curAve = cur / k
                if curAve  >= threshold:
                    ans += 1
                
                cur -= arr[left]
                left += 1
        
        return ans
            
        
        
        