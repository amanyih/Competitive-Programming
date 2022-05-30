class Solution(object):
    def rearrangeArray(self,arr):
        li=[]
        arr.sort()
        first=0
        last=len(arr)-1
        while len(li)<len(arr):
            li.append(arr[first])
            first+=1
            if first<last:
                li.append(arr[last])
                last -=1
        return li