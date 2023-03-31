class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        n = 1
        k = 0
        while (n << k )<=num:
            mask += 1 << k
            k += 1
        return num ^ mask
        