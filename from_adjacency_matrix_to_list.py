from collections import defaultdict

n = int(input())

grid = []

for i in range(n):
    row = list(map(int, input().split()))
    cur = []
    for j in range(n):
        if row[j]:
            cur.append(j+1)
    print(len(cur), *cur)
