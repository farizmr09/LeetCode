# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [[root, 0]]
        the_map = defaultdict(list)
        while stack:
            curr, currLevel = stack.pop()
            if currLevel % 2 != 0:
                the_map[currLevel].append(curr.val)
            else:
                the_map[currLevel].insert(0, curr.val)
            if curr.left:
                stack.append([curr.left, currLevel + 1])
            if curr.right:
                stack.append([curr.right, currLevel + 1])  
        return list(the_map.values())   