class Solution(object):
    def isHappy(self, n):
        
        sett = set()
        
        
        while True:
            if n==1:
                return True
            elif n in sett:
                return False
            else:
                sett.add(n)
                tn = str(n)
                n = 0 
                for i in tn:
                    n += (int(i))**2
                
        
        