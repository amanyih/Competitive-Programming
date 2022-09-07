class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        elif n%4 != 0 or n == 0:
            return False
        else:
            return self.isPowerOfFour(n//4)