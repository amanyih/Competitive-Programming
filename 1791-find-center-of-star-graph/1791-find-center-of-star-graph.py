class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        st = set(edges[0])
        
        for i in range(1,len(edges)):
            st = st.intersection(set(edges[i]))
        
        for k in st:
            return k
        