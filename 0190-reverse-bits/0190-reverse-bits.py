class Solution:
    def reverseBits(self, n: int) -> int:
        n_r = list(bin(n))
        n_r = n_r[2:]
        n_r.reverse()
        if len(n_r) < 32:
            n_r.append("0" * (32 - len(n_r)))
        return(int("".join(n_r), 2))