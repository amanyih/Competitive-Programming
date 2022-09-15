class Solution:
    def goodDaysToRobBank(self, sec: List[int], time: int) -> List[int]:
        pre = [0]
        for i in range(1,len(sec)):
            if sec[i] <= sec[i-1]:
                pre.append(pre[-1]+1)
            else:
                pre.append(0)
        post = [0] * len(sec)
        
        for i in range(len(sec)-2,-1,-1):
            if sec[i] <= sec[i+1]:
                post[i] = post[i+1] +1
        ans = []
        for i in range(len(sec)):
            if pre[i] >= time and post[i] >= time:
                ans.append(i)
        
        return ans
            
        