n, k = [int(x) for x in input().split()]

rating = [int(x) for x in input().split()]


def split(arr):
    if len(arr) == 1:
        return arr
    newArr = []
    n = len(arr)//2
    # print(arr)
    left = split(arr[:n])
    right = split(arr[n:])

    minLeft = rating[left[0]]

    for i in range(1, len(left)):
        minLeft = min(minLeft, rating[left[i]])
    minRight = rating[right[0]]

    for i in range(1, len(right)):
        minRight = min(minRight, rating[right[i]])

    # print("left", left)
    # print("right", right)
    for i in range(len(left)):
        if abs(rating[left[i]] - minRight) <= k:
            newArr.append(left[i])
        elif rating[left[i]] > minRight:
            newArr.append(left[i])
    # print(newArr)
    for i in range(len(right)):
        if abs(rating[right[i]] - minLeft) <= k:
            newArr.append(right[i])
        elif rating[right[i]] > minLeft:
            newArr.append(right[i])
    # print(newArr)
    return newArr


arr = [x for x in range(2**n)]
newArr = split(arr)
ans = [x+1 for x in newArr]

print(*ans)
