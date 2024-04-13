class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        holder = ""
        jump = (numRows - 1) * 2
        for i in range(numRows):
            for j in range(i, len(s), jump):
                holder += s[j]
                if (i != 0 and i != numRows - 1 and j + jump - 2 * i < len(s)):
                    holder += s[j + jump - 2 * i]
        return holder