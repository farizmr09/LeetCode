# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")
        def inorder(root):
            nonlocal prev, res
            if not root:
                return
            inorder(root.left)
            if not prev:
                prev = root
            else:
                res = min(res, abs(prev.val - root.val))
                prev = root
            inorder(root.right)  
        inorder(root)
        return res