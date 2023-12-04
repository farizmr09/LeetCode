class Solution:
    def romanToInt(self, s: str) -> int:
        rn = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        holder = 0
        for i in range(len(s) - 1, 0, -1):
            holder = (holder + rn[s[i]]) if rn[s[i]] - rn[s[i - 1]] not in [4, 9, 40, 90, 400, 900] else holder + rn[s[i]] - (2 * rn[s[i - 1]])
        return holder + rn[s[0]]