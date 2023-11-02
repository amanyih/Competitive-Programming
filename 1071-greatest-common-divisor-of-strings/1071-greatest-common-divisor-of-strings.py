class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
            
        if str1 + str2 != str2 + str1:
            return ""
        
        l = gcd(len(str1),len(str2))
        # print(l)
        return str1[:l]
        
        