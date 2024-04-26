# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        stack = []
        i = 0
        while curr:
            stack.append(curr)
            i += 1
            curr = curr.next
        k = k % i
        stack[-1].next = stack[0]
        stack[-1 * k - 1].next = None
        return stack[-1 * k]
    