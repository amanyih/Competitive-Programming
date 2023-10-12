class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        cache = {-1:0}
        
        
        def search(index,prev1=inf,prev2=inf):
            if (index,prev1,prev2) in cache:
                return cache[(index,prev1,prev2)]
            
            if index < 0 :
                return 0
            
            cur = inf
            
            if nums2[index] < prev1 and nums1[index] < prev2:
                whatIfISwap =1+ search(index-1,nums2[index],nums1[index])
                
                cur = min(whatIfISwap,cur)
            if nums1[index] < prev1 and nums2[index] < prev2:
                
                whatIfIdont = search(index-1,nums1[index],nums2[index])
                cur = min(cur,whatIfIdont)
            cache[(index,prev1,prev2)] = cur
            return cur
        return search(len(nums1)-1)
                
                
            
            
            
            
        