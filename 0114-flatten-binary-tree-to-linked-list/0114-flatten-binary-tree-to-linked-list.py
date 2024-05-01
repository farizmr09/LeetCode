# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        queue = [root]
        while queue:
            curr = queue.pop(0)
            root.val = curr.val
            if curr.right:
                queue.insert(0, curr.right) 
            if curr.left:
                queue.insert(0, curr.left)
            if not queue:
                continue
            root.left = None
            root.right = TreeNode(0)
            root = root.right