# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            
            total = 0
            def checker(root: Optional[TreeNode], total: int):
                if root is None:
                    return False
                if total + root.val == targetSum and root.left is None and root.right is None:
                    return True
                return checker(root.left, total + root.val) or checker(root.right, total + root.val)

            return checker(root, total)