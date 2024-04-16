class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        f = s.split()
        hmap = {}
        if len(pattern) != len(f):
            return False
        for i in range(len(f)):
            if (pattern[i] in hmap and hmap[pattern[i]] != f[i]):
                return False
            hmap[pattern[i]] = f[i]
            if (list(hmap.values()).count(f[i]) > 1):
                return False
        return True