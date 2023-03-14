class Solution:
    def countAnagrams(self, s: str) -> int:
        
        lst = s.split()
        res =1
        
        for word in lst:
            # print(word)
            count = Counter(word)
            countSum = len(word)
            fac = factorial(countSum)
            for key in count:
                fac = fac // factorial(count[key])
            res *= fac
        return res % (10**9+7)