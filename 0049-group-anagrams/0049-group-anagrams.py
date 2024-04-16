class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            if d.get(tuple(count)) == None:
                d[tuple(count)] = [w]
                continue
            d[tuple(count)].append(w)
        return(d.values())  