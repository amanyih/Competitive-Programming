class Solution(object):
    def checkArithmeticSubarrays(self, n, l, r):
        ansArray=[]
        for i in range(len(l)):
            copySubArray = n[l[i]:r[i]+1]
            copySubArray.sort()
            dif = copySubArray[1] - copySubArray[0]
            if len(copySubArray)>2:
                j = 1
                count = 0
                while j<=len(copySubArray)-2:
                    if copySubArray[j+1] - copySubArray[j] != dif:
                        count+=1
                    j+=1
                if count!=0:
                    ansArray.append(False)
                else:
                    ansArray.append(True)
            else:
                ansArray.append(True)
        return ansArray