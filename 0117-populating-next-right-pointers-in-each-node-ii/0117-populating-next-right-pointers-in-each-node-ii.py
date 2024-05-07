"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [[root, 0]]
        prev = None
        currLevel = 1
        while stack:
            curr, level  = stack.pop()
            if level != currLevel:
                prev = curr
                prev.next = None
                currLevel = level
            else:
                prev.next = curr
                prev = curr
            if curr.left:
                stack.insert(0, [curr.left, level + 1])
            if curr.right:
                stack.insert(0, [curr.right, level + 1])
        return root