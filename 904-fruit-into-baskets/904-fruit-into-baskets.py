class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        dict_ = {}
        
        left = 0
        
        ans = 0
        
        for right in range(len(fruits)):
            if fruits[right] in dict_:
                dict_[fruits[right]]+= 1
            else:
                dict_[fruits[right]] = 1
                
            while len(dict_) > 2:
                dict_[fruits[left]] -= 1
                
                if dict_[fruits[left]] == 0:
                    del dict_[fruits[left]]
                
                left += 1
            ans = max(ans,right-left+1)
        
        return ans