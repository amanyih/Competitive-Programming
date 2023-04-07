from collections import defaultdict

n = int(input())
k = int(input())


def addEdge(graph, first, second):
    graph[second].append(first)
    graph[first].append(second)


graph = defaultdict(list)

for _ in range(k):
    op = list(map(int, input().split()))

    if len(op) == 3:
        addEdge(graph, op[1], op[2])
    else:
        print(*graph[op[1]])
