class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        for i in range(len(s)):
            if (s[i] not in s_map and t[i] in t_map) or (s[i] in s_map and t[i] not in t_map):
                return False
            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]] = [i]
                t_map[t[i]] = [i]
                continue
            s_map[s[i]].append(i)
            t_map[t[i]].append(i)
        
        return(list(s_map.values()) == list(t_map.values()))