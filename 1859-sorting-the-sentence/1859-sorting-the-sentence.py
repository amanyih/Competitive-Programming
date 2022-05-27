class Solution(object):
    def sortSentence(self,s):
        sp=s.split()
        li=[]
        st=""
        k=""
        for i in sp:
            li.append(int(i[-1]))
        for j in range(len(li)-1):
            for k in range(0,len(li)-j-1):
                if li[k]>li[k+1]:
                    li[k],li[k+1] = li[k+1],li[k]
                    sp[k],sp[k+1]=sp[k+1],sp[k]
        for i in sp:
            x=i.replace(i[-1],"")
            st = st+x+" "
        return st[:len(st)-1]
        
        