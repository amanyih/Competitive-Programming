from collections import defaultdict
n = int(input())

grid = []
graph = defaultdict(list)

for _ in range(n):
    grid.append(list(map(int, input().split())))

count = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            if i not in graph[j]:
                count += 1
            graph[i].append(j)
            graph[j].append(i)


print(count)
