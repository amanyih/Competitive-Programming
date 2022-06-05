class Solution(object):
    def findOriginalArray(self,changed):
        if len(changed)%2 !=0 or len(changed)==0:return []
        changed.sort()
        double=[changed[0]*2]
        single=[changed[0]]
        for i in range(1,len(changed)):
            if len(double)==0:
                single.append(changed[i])
                double.append(changed[i]*2)
            elif changed[i] == double[0]:
                double.remove(double[0])
            else:
                single.append(changed[i])
                double.append(changed[i]*2)
        if len(double)==0:return single
        else:return []
        