class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        stack = []
        for i in range(len(l)):
            if l[i] == '' or l[i] == ".":
                continue
            if l[i] == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(l[i])

        return("/" + "/".join(stack))