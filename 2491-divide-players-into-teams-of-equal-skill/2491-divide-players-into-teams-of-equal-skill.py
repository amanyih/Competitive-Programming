class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        totallSkill = skill[0] + skill[-1]
        
        ans = 0
        
        left = 0
        right = len(skill) - 1
        
        while left < right:
            
            if skill[left] + skill[right] != totallSkill:
                return -1
            ans += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return ans
        
        
        
        
        