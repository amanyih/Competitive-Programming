class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        ans = 0
        count = 0
        for i in range(len(piles[:-1])-1,-1,-2):
            if count == len(piles)/3:
                break
            ans += piles[i]
            count+=1
        return ans
        
        