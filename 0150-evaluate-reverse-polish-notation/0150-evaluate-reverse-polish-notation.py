class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit() or i[1:].isdigit():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(b + a)
                elif i == "-":
                    stack.append(b - a)
                elif i == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
        return stack.pop()