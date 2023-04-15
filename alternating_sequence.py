
t = int(input())
 
for _ in range(t):
    n = int(input())
    numbers = [int(x) for x in input().split()]
    
    maxSum = 0
    
    cur = numbers[0]
 
    for i in range(1, n):
        if numbers[i] * numbers[i-1] < 0:
            maxSum += cur
            cur = numbers[i]
        else: 
            cur = max(cur, numbers[i])
    maxSum += cur
    print(maxSum)
