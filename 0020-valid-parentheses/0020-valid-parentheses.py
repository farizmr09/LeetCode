class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        pair = {"(": ")", "{":"}", "[":"]"}
        st = []
        ls = list(s)
        while ls:
            if ls[0] == "]" or ls[0] == ")" or ls[0] == "}":
                if len(st) == 0:
                    return False
                if pair[st.pop()] != ls[0]:
                    return False
                    break
                ls.pop(0)
                continue
            st.append(ls.pop(0))
        if len(st) != 0:
            return False
        return True