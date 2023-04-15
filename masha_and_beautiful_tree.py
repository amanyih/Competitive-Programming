import sys
import threading


def main():

    t = int(input())
    count = 0

    def beautify(nums):
        nonlocal count
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = beautify(nums[:mid])
        right = beautify(nums[mid:])

        if left[0] > right[0]:
            count += 1
            return right + left
        return left + right

    def check(nums, count):

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                return -1
        return count

    for _ in range(t):
        n = int(input())
        nums = [int(x) for x in input().split()]
        count = 0

        newNums = beautify(nums)
        print(check(newNums, count))


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
