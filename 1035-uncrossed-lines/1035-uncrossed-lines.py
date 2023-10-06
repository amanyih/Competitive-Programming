class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        locations = defaultdict(list)
        
        for i,num in enumerate(nums2):
            locations[num].append(i)
        
        cache = {}
        
        
        def count_intersecting_lines(index,lastChoosen):
            if (index,lastChoosen) in cache:
                return cache[(index,lastChoosen)]
            
            if index < 0 :
                return 0
            
            cur = 0
            for i in locations[nums1[index]]:
                if i < lastChoosen:
                    nxt = count_intersecting_lines(index-1,i)
                    cur = max(cur,nxt+1)
                    
            jump = count_intersecting_lines(index-1,lastChoosen)
            cur = max(cur,jump)
            cache[(index,lastChoosen)] = cur
            return cur
        return count_intersecting_lines(len(nums1)-1,inf)
                
                
            
        