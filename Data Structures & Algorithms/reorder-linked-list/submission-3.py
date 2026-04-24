# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        s, f = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        # separate middle into 2
        head2 = s.next
        s.next = None

        rev = None
        while head2:
            tmp = head2.next
            head2.next = rev
            rev = head2
            head2 = tmp

        while head and rev:
            tmp = head.next
            tmp2 = rev.next
            head.next = rev
            rev.next = tmp
            head = tmp
            rev = tmp2

