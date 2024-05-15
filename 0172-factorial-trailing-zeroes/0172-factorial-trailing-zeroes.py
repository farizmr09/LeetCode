class Solution:
    def trailingZeroes(self, n: int) -> int:
        res, start = 0, 5
        while start <= n:
            res += n // start
            start *= 5
        return res