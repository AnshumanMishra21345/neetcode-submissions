# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        fast=head
        while fast:
            curr=curr.next
            if curr is None:
                return False
            if fast.next is None:
                return False
            fast=fast.next.next
            if fast is curr:
                return True
        else:
            return False
        