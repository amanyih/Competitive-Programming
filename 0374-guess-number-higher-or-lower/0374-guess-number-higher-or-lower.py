# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            guessed = guess(mid)
            
            if guessed == 0:
                return mid
            if guessed == 1:
                left = mid + 1
            else:
                right = mid - 1
        
        