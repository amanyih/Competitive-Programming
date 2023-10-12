# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def findPeek():
            left  = 0
            right = mountain_arr.length()-1

            while left <= right:
                mid = (left + right)//2
                cur = mountain_arr.get(mid)
                prev = -inf
                nxt = inf
                if mid -1 >= 0:
                    prev = mountain_arr.get(mid-1)
                if mid+1 < mountain_arr.length():
                    nxt = mountain_arr.get(mid+1)
                isPeek = prev < cur and nxt < cur
                isIncreasing = prev < cur < nxt
                

                if isPeek:
                    return mid
                elif isIncreasing:
                    left= mid+1
                else:
                    right = mid -1
            return left
        def searchBeforePeek(peek):
            left = 0
            right = peek
            res = 0
            while left <= right:
                mid = (right + left)//2
                if mountain_arr.get(mid) < target:
                    left = mid + 1
                elif mountain_arr.get(mid) > target:
                    right = mid -1
                else:
                    right = mid -1
                    res = mid
            if mountain_arr.get(res) == target:
                return res
            return -1
        def searchAfterPeek(peek):
            left = peek
            right = mountain_arr.length() - 1
            res = 0
            while left <= right:
                mid = (right + left)//2
                if mountain_arr.get(mid) < target:
                    right = mid - 1
                elif mountain_arr.get(mid) > target:
                    left = mid + 1
                else:
                    right = mid -1
                    res = mid
            if mountain_arr.get(res) == target:
                return res
            return -1
        peek = findPeek()
        # print(peek)
        # return peek
        left = searchBeforePeek(peek)
        # print(left) 
        # return left
        right = searchAfterPeek(peek)
        # print("right",right)
        
        if left == -1 and right == -1:
            return -1
        elif left == -1 or right == -1:
            return max(left,right)
        return min(left,right)
            
                
        