# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        reverse = []
        holder = []
        res = ListNode()
        counter = 0
        while head:
            if counter >= left - 1 and counter <= right - 1:
                reverse.insert(0, head)
            else:
                holder.append(head)
            head = head.next
            counter += 1
            
        holder[left - 1:left - 1] = reverse
        
        res_head = res
        for i in range(len(holder)):
            res.val = holder[i].val
            if i + 1 < len(holder):
                res.next = ListNode(holder[i + 1].next)
            res = res.next            
        
        return(res_head)
