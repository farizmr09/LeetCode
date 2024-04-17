class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        c, r = 0, 0
        for i in range(len(s)):
            if i > 0 and s[i] - s[i - 1] != 1:
                r = max(c, r)
                c = 0
            c += 1
        
        return(max(c, r))