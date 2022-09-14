class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).most_common(k)
        
        ans = []
        
        for num in count:
            ans.append(num[0])
        return ans
        
        
        
            
                
        