# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
       
        even = head
        odd_head = odd = head.next
        while odd and odd.next:
            even.next = even.next.next
            even = even.next
            odd.next = odd.next.next
            odd = odd.next
        even.next = odd_head
        return head