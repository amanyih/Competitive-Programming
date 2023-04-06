class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        
        count = Counter(deck)
        arr = [count[key] for key in count]
        
        cur = arr[0]
        
        for i in range(1,len(arr)):
            g = gcd(cur,arr[i])
            if g == 1:
                return False
            cur = min(cur,g)
        
        if cur == 1:
            return False
        
        return True