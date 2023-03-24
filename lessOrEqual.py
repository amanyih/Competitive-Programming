length,count=list(map(int,input().split()))
nums=list(map(int,input().split()))
nums.sort()
if count<length and nums[count]-nums[count-1]>0:
    print(nums[count-1])
elif count==length:
    print(nums[-1])
elif count==0  and nums[0]!=1:
    print(nums[0]-1)
elif count==0 and nums[0]==1:
    print(-1)
else:
    print(-1)
