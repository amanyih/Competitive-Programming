class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        dict_ = {}
        sett = set()
        left = 0
        
        ans = 0
        for right in range(len(s)):
            sett.add(s[right])
            dict_[s[right]] = dict_.get(s[right],0) + 1
            
            if right > 1:
                if len(sett) == 3:
                    ans += 1
                dict_[s[left]] = dict_.get(s[left]) - 1
                if dict_[s[left]] == 0:
                    sett.remove(s[left])
                
                left += 1
        
        return ans
            