class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        if not set(ransomNote).issubset(set(magazine)):
            return False

        for i in r:
            if r[i] > m[i]:
                return False
            
        return True