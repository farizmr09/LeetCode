# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        stack = [[root, 0]]
        the_map = {}
        while stack:
            curr, currLevel = stack.pop()
            the_map[currLevel] = curr.val
            if curr.right:
                stack.append([curr.right, currLevel + 1])
            if curr.left:
                stack.append([curr.left, currLevel + 1])
        return list(the_map.values())