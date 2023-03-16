class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        def find(level,path):
            
            if level == len(nums):
                ans.append(path[:])
                return
            
            path.append(nums[level])
            find(level+1,path)
            path.pop()
            find(level+1,path)
                
        find(0,[])
        return ans