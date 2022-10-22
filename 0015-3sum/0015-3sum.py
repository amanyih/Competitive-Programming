class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        
        ans = []
        sett =set()
        
        for i in range(len(nums)):
            
            if nums[i] not in sett:
                sett.add(nums[i])
                
                target = 0 - nums[i]
                left = i + 1
                right = len(nums) - 1
                
                while left < right:
                    if nums[left] + nums[right] == target:
                        ans.append([nums[i],nums[left],nums[right]])
                        left += 1
                        
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
                        
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return ans
            
            
        