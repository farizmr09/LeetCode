# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        stack = [[root, 0]]
        the_map = defaultdict(list)
        while stack:
            curr, currLevel = stack.pop()
            the_map[currLevel].append(curr.val)
            if curr.left:
                stack.append([curr.left, currLevel + 1])
            if curr.right:
                stack.append([curr.right, currLevel + 1])
        for keys in the_map:
            the_map[keys] = sum(the_map[keys])/len(the_map[keys])
        return list(the_map.values())