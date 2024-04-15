class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0
        l = 0
        for r in range(len(s)):
            count = set(s[l:r])
            while s[r] in count:
                l += 1
                count = set(s[l:r])
            total = max(total, r - l + 1)    
        return total