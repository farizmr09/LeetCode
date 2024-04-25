# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = set()
        hmap = {}
        curr = head
        while curr:
            if curr.val in c:
                if hmap.get(curr.val):
                    hmap.pop(curr.val)
            else:
                c.add(curr.val)
                hmap[curr.val] = curr
            curr = curr.next
        prev = None
        if len(hmap.values()) == 0:
            return None
        for n in hmap.values():
            if not prev:
                head = n
            else:
                prev.next = n
            prev = n
            n.next = None
        return head