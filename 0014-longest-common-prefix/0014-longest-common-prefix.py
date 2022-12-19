class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minLen = float("inf")

        for str in strs:
            minLen = min(minLen,len(str))
        
        for i in range(minLen):
            for str in strs:
                if str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:minLen]

        

        