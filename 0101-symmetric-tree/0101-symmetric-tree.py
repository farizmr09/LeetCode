# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True 

        def checker(left: Optional[TreeNode], right: Optional[TreeNode]):
            if (left is None and right is None):
                return True
            # print(left.val, right.val)
            if (left is not None and right is not None) and left.val == right.val:
                return checker(left.left, right.right) and checker(left.right, right.left)
            return False
        
        return checker(root.left, root.right)