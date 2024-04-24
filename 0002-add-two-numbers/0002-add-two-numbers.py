# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            res = ListNode()
            head = res
            p1 = l1
            p2 = l2

            carry = 0
            while p1 or p2:
                res.next = ListNode()
                res = res.next

                if p1 == None:
                    total = p2.val + carry
                    p2 = p2.next
                elif p2 == None:
                    total = p1.val + carry
                    p1 = p1.next
                else:   
                    total = p1.val + p2.val + carry
                    p1 = p1.next
                    p2 = p2.next

                if total >= 10:
                    res.val = total % 10
                    carry = 1
                else:
                    res.val = total
                    carry = 0
                            
            if carry != 0:
                res.next = ListNode(1)
            
            return(head.next)