class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        left = 0
        
        while left < len(chars):
            right = left + 1
            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            
            length = right - left
            chars[ans] = chars[left]
            ans += 1
            if length != 1:
                for i in str(length):
                    chars[ans] = i
                    ans += 1
            left = right
        
        return ans
                    
                
                
                
        