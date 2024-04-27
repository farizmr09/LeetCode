# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        counter = 1
        visit = [[root, counter]]
        while visit:
            curr, currCounter = visit.pop()
            counter = max(currCounter, counter)
            if curr and curr.left:
                visit.append([curr.left, currCounter + 1])
            if curr and curr.right:
                visit.append([curr.right, currCounter + 1])
            
        return(counter)