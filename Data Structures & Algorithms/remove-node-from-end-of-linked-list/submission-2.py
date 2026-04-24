# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        rev = None
        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp
        
        if n == 1:
            rev = rev.next
        else:
            i = 1
            curr = rev
            while curr and i < n - 1:
                curr = curr.next
                i += 1
            if curr and curr.next:
                curr.next = curr.next.next

        curr = rev
        rev = None
        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp

        return rev

