# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        if n == len(stack):
            head = head.next
        elif n == 1:
            stack[-2].next = None
        else:
            stack[n * -1 - 1].next = stack[(n - 1) * - 1]
        return head