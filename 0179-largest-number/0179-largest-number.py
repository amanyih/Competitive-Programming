class Solution(object):
    def largestNumber(self,arr):
        strr=""
        str_sum=lambda x,y: int(str(x)+str(y))
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if str_sum(arr[i],arr[j]) < str_sum(arr[j],arr[i]):
                    arr[i],arr[j]=arr[j],arr[i]
        flag=0
        for i in arr:
            if i==0:
                flag+=1
        if flag ==len(arr):
            strr="0"
        else:
            for i in arr:
                strr=strr+str(i)
        return strr
        