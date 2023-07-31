class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        scores = defaultdict(int)
        
        for i in range(len(questions)-1,-1,-1):
            jump = scores[i+1]
            take = questions[i][0] + scores[i+questions[i][1]+1]
            # print(i,jump,take)
            
            scores[i] = max(jump,take)
        
        
        # print(scores.keys())
        return max(scores.values())