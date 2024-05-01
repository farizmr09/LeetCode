# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, [])]
        sum = 0
        while stack:
            curr, number = stack.pop()
            temp = number.copy()
            temp.append(curr.val)
            
            if curr.left:
                stack.append((curr.left, temp))
            if curr.right:
                stack.append((curr.right, temp))
            if not curr.left and not curr.right:
                sum += int("".join(map(str, temp)))

        return(sum)