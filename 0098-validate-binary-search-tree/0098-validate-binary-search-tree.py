# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        temp, check = [], True
        def inorder(root):
            nonlocal temp, check
            if not root:
                return
            inorder(root.left)
            if root.val in temp:
                check = False
                return
            temp.append(root.val)
            inorder(root.right)  
        inorder(root)
        return((temp == sorted(temp)) and check)