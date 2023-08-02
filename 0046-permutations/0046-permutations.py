class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        global bt
        bt = 0
        
        def isOn(bt,index):
            res = 1<<index & bt
            
            return res != 0
            
        
        def backtrack(cur):
            # print(cur)
            global bt
            if len(cur) == len(nums):
                # print(cur)
                ans.append(cur[:])
                return
            
            for i in range(len(nums)):
                if not isOn(bt,i):
                    bt += 1<<i
                    cur.append(nums[i])
                    backtrack(cur)
                    cur.pop()
                    bt -= 1<<i
                    
        
        backtrack([])
        
        return ans
                    
                    
                
            
            
                    
        
        
        
        
        