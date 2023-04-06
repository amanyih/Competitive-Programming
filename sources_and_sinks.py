from collections import defaultdict
n = int(input())

grid = []

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

fromgraph = defaultdict(list)
intograph = defaultdict(list)

for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            intograph[j+1].append(i+1)
            fromgraph[i+1].append(j+1)

sources = []
for i in range(1, n+1):
    if i not in intograph:
        sources.append(i)
sinks = []
for i in range(1, n+1):
    if i not in fromgraph:
        sinks.append(i)
print(len(sources), *sources)
print(len(sinks), *sinks)
