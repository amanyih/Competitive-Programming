class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        
        i = len(nums) - 1
        st = set()

        while i >= 0 and len(st) != k:
            # print(st,i)
            if nums[i] <= k:
                st.add(nums[i])
            i -= 1
        return len(nums) - i -1
            
            
            
        