t = int(input())

for _ in range(t):
    shift = 0
    n = int(input())

    while not ((1 << shift) & n):
        shift += 1
    if n >> (shift + 1):
        print(1 << shift)
    else:
        newShift = 0
        while ((1 << newShift) & n):
            newShift += 1
        print((1 << newShift) + (1 << shift))
