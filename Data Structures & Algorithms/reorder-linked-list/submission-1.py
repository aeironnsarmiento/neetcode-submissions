# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        head2 = s.next
        s.next = None

        curr1 = head
        curr2 = head2
        rev = None
        while curr2:
            temp = curr2.next
            curr2.next = rev
            rev = curr2
            curr2 = temp

        while curr1 and rev:
            temp = curr1.next
            temp2 = rev.next
            curr1.next = rev
            rev.next = temp
            curr1 = temp
            rev = temp2
        