# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [[root, 0]]
        the_map = defaultdict(list)
        while stack:
            curr, currLevel = stack.pop()
            the_map[currLevel].append(curr.val)
            if curr.left:
                stack.insert(0, [curr.left, currLevel + 1])
            if curr.right:
                stack.insert(0, [curr.right, currLevel + 1])
        
        return list(the_map.values())