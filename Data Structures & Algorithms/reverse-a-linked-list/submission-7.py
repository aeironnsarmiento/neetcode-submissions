# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        rev = None

        while curr:
            tmp = curr.next
            curr.next = rev
            rev = curr
            curr = tmp

        return rev