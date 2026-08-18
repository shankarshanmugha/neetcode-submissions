# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resHead=head
        if not head:
            return head
        vals=[head.val]
        while head.next:
            head=head.next
            vals.append(head.val)
        vals.reverse()
        retrunres=resHead
        for i in vals:
            resHead.val=i
            resHead=resHead.next

        return retrunres

