class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        space = s.count(" ")
        counter = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            counter = counter + 1
        return counter
        