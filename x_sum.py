t = int(input())


def calculateSum(grid, row, col):
    r = len(grid)
    c = len(grid[0])

    res = 0
    nwr, nwc = row-1, col-1
    while nwr >= 0 and nwc >= 0:
        res += grid[nwr][nwc]
        nwr -= 1
        nwc -= 1
    ner, nec = row - 1, col + 1

    while ner >= 0 and nec < c:
        res += grid[ner][nec]
        ner -= 1
        nec += 1
    ser, sec = row+1, col + 1

    while ser < r and sec < c:
        res += grid[ser][sec]
        ser += 1
        sec += 1
    swr, swc = row + 1, col - 1

    while swr < r and swc >= 0:
        res += grid[swr][swc]
        swr += 1
        swc -= 1

    return res + grid[row][col]


for _ in range(t):
    n, m = list(map(int, input().split()))
    grid = []

    for i in range(n):
        grid.append(list(map(int, input().split())))
    ans = 0
    for row in range(n):
        for col in range(m):
            ans = max(ans, calculateSum(grid, row, col))
    print(ans)
