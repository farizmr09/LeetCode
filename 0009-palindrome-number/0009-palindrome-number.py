class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        sr = s.copy()
        sr.reverse()
        return s == sr