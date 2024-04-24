# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            res = ListNode()
            head = res
            
            l1 = list1
            l2 = list2
            
            if l1 == None:
                return list2
            if l2 == None:
                return list1
            
            while l1 or l2:
                res.next = ListNode()
                res = res.next

                if l1 is None:
                    res.val = l2.val
                    l2 = l2.next
                    continue
                if l2 is None:
                    res.val = l1.val
                    l1 = l1.next
                    continue

                if l1.val > l2.val:
                    res.val = l2.val
                    l2 = l2.next
                elif l1.val < l2.val:
                    res.val = l1.val
                    l1 = l1.next
                else:
                    res.val = l1.val
                    res.next = ListNode(l1.val)
                    res = res.next
                    l1 = l1.next
                    l2 = l2.next
                    
            return(head.next)