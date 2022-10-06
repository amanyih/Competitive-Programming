class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        score = 0
        cur_score = 0
        
        left = 0
        right = len(tokens) - 1
        
        
        while left <= right:
            if tokens[left] <= power:
                cur_score += 1
                power -= tokens[left]
                left += 1
            elif cur_score >=1:
                cur_score -= 1
                power += tokens[right]
                right -= 1
            else:
                return score
            
            score = max(score,cur_score)
        
        return score
                
            
        
        
        