class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        count = defaultdict(int)
        
        for domain in cpdomains:
            
            lst = domain.split()
            freq = int(lst[0])
            newDomain = lst[1].split(".")
            
            while newDomain:
                dom = ".".join(newDomain)
                count[dom] += freq
                newDomain.pop(0)
        ans = []
        
        for key in count:
            temp = [str(count[key]),key]
            ans.append(" ".join(temp))
        
        return ans
            
            
        