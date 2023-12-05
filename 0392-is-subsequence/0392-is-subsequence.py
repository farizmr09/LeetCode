class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while j < len(t):
            if i >= len(s): 
                break
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        return(i == len(s))