class Solution:
    def longestPrefix(self, s: str) -> str:
        
        lps = [0] * len(s)
        suf = 1
        pre = 0

        while suf < len(s):
            if s[suf] == s[pre]:
                lps[suf] = pre + 1
                pre += 1
                suf += 1
            elif pre == 0:
                suf += 1
            else:
                pre = lps[pre-1]
        i = lps[-1]
        return s[:i]