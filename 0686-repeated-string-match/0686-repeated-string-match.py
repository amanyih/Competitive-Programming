class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        string = a * ((len(b) //len(a))+2)
        lps = [0] * len(b)
        suf = 1
        pre = 0

        while suf < len(b):
            if b[suf] == b[pre]:
                lps[suf] = pre + 1
                pre += 1
                suf += 1
            elif pre == 0:
                suf += 1
            else:
                pre = lps[pre-1]
        
        s_p = 0
        a_p = 0
        # print(string)
        # print(lps)
        
        # return 0

        while s_p < len(string):
            if string[s_p] == b[a_p]:
                s_p += 1
                a_p += 1
            elif a_p == 0:
                s_p += 1
            else:
                a_p = lps[a_p-1]
            
            if a_p == len(b):
                
                return ceil(s_p/len(a))
        
        return -1
        