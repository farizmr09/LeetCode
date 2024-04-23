class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        stack = []
        for i in range(len(l)):
            if l[i] == '' or l[i] == ".":
                continue
            if l[i] == ".." and len(stack) == 0:
                continue
            if l[i] == "..":
                stack.pop()
                continue
            stack.append(l[i])

        return("/" + "/".join(stack))