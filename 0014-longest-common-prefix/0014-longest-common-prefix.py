class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        holder = 0
        for i in range(0, len(strs[0])):
            for s in strs:
                if s.startswith(strs[0][0:holder + 1]) == False:
                    return strs[0][0:holder]
            holder = holder + 1
        return strs[0][0:holder]