class Solution:
    def PredictTheWinner(self, nums: List[int],turn = 0,left=0,right = 0) -> bool:
        
        if len(nums) == 1:
            if not turn % 2:
                left += nums[0]
            else:
                right += nums[0]
            return left >= right
        elif len(nums) == 0:
            return left >= right
        
        if turn % 2 == 0:
            left1 = left + nums[0]
            left2= left + nums[-1]
            turn += 1
            
            choice1 = self.PredictTheWinner(nums[1:],turn,left1,right)
            choice2 = self.PredictTheWinner(nums[:-1],turn,left2,right)
            return choice1 or choice2
        else:
            right1 = right + nums[0]
            right2= right + nums[-1]
            turn += 1
            
            choice1 = self.PredictTheWinner(nums[1:],turn,left,right1)
            choice2 = self.PredictTheWinner(nums[:-1],turn,left,right2)
            return choice1 and choice2
            
            
            
        