class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        
        totalCards = sum(cardPoints)
        
        ans = 0
        cur = 0
        
        
        left = 0
        winSize = len(cardPoints) - k
        
        for right in range(len(cardPoints)):
            
            cur += cardPoints[right]
            
            if right - left +  1 == winSize:
                ans = max(totalCards-cur,ans) if totalCards - cur != 0 else totalCards
                cur -= cardPoints[left]
                left += 1
        
        return ans
            