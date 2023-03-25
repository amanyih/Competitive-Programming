class Solution:
    def maxLength(self, arr: List[str]) -> int:
        global ans
        ans = 0
        
        def isUnique(path,string):
            if not path:
                if len(set(string)) == len(string):
                    return True
                else:
                    return False
            st = set()
            prev = 0
            for p in path:
                cur = set(p)
                st = st.union(cur)

                if len(st)-prev != len(p):
                    return False
                prev = len(st)
            # print("before",st,len(st),prev)
            st = st.union(set(string))
            # print("after",st,len(st),prev)
            if len(st)-prev != len(string):
                # print("False2")
                return False
            return True
            
        def length(path):
            total = 0
            for p in path:
                total += len(p)
            return total
        
        
        
        def backtrack(path,index):
            # print(path,index)
            global ans
            if index >= len(arr):
                ans = max(ans,length(path))
                return
            
            if isUnique(path,arr[index]):
                path.append(arr[index])
                ans = max(ans,length(path))
                backtrack(path,index+1)
                path.pop()
            backtrack(path,index+1)
        
        backtrack([],0)
        return ans
            
                
        