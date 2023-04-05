n = int(input())
nums = list(map(int, input().split()))

oddCount = 0
evenCount = 0

for num in nums:
    if num % 2:
        evenCount += 1
    else:
        oddCount += 1
if oddCount > 0 and evenCount > 0:
    nums.sort()
print(*nums)
