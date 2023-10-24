class Solution:
    def myAtoi(self, s: str) -> int:
        
        nums = []
        s = s.strip()
        # dot_found = False
        
        for char in s:
            
            if char in {"+","-"}:
                if nums:
                    break
            elif not (0 <= ord(char)-ord("0")<=9):
                break
            nums.append(char)
        if not nums:
            return 0
        if nums[0] in {"+","-"} and len(nums) == 1 or nums[0] == ".":
            return 0

        ans = int("".join(nums))
        if ans <= 0:
            return max(ans,-(2**31))
        return min(ans,2**31-1)
            