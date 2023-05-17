class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        p = 0
        start = tasks[p][0]
        time = start
        cur = []
        ans = []
        # print(start)
        
        while cur or p < len(tasks):
            # print(time,cur,ans)
            # print("was here")
            while p < len(tasks) and time >= tasks[p][0]:
                # print("here")
                en,pro,index = tasks[p]
                # print(tasks[p],pro,p)
                heappush(cur,(pro,index))
                p += 1
            if cur:
                t,i = heappop(cur)
                time += t
                ans.append(i)
            elif p < len(tasks):
                en,pro,index= tasks[p]
                p += 1
                
                heappush(cur,(pro,index))
                time = en
            
        
        return ans
                
            
                
                
            
        
        
            
            
        